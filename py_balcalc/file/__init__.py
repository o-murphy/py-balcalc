from pathlib import Path

import a7p.protovalidate
from a7p import A7PFile


def save_file(file_name, payload):
    with open(file_name, 'wb') as fp:
        A7PFile.dump(payload, fp)


def save_file_stream(file_name, data):
    with open(file_name, 'wb') as fp:
        fp.write(data)


def open_files(*file_names):
    """opens ballistic profiles from a json formatted file and loads it to working list"""
    profiles = []
    for path in file_names:
        if Path(path).is_dir():
            profiles.extend(open_files(*(Path(path).iterdir())))

        if Path(path).suffix in ['.a7p', '.A7P']:
            try:
                with open(path, 'rb') as fp:
                    a7p_file = A7PFile.load(fp)
                profiles.append((path, a7p_file))
            except a7p.protovalidate.ValidationError as err:
                print(err.violations)
    return profiles
