from pathlib import Path

from a7p import A7PFile


def save_file(file_name, payload):
    with open(file_name, 'wb') as fp:
        A7PFile.dump(payload, fp)


def open_files(*file_names):
    """opens ballistic profiles from a json formatted file and loads it to working list"""
    profiles = []
    for path in file_names:
        if Path(path).is_dir():
            profiles.extend(open_files(*(Path(path).iterdir())))

        if Path(path).suffix in ['.a7p', '.A7P']:
            with open(path, 'rb') as fp:
                a7p_file = A7PFile.load(fp)
            profiles.append((path, a7p_file))
    return profiles
