import json
import logging
from datetime import datetime
from pathlib import Path

from py_balcalc.logger import logger
from py_balcalc.settings import app_settings
from py_balcalc.signals_manager import appSignalMgr

TRANSLATION_VERSION = '0.0.1'
TR_PATH = Path(Path(__file__).parent, 'translations')

DEFAULT_TRANSLATION = {
    "meta": {
        "language": None,
        "author": None,
        "version": TRANSLATION_VERSION,
        "date": datetime.strftime(datetime.now(), "%d.%m.%Y")
    },
    "context": {

    }
}


class Translator:
    def __init__(self):
        self._lang = DEFAULT_TRANSLATION

        try:
            self.translations = list(lang.stem for lang in TR_PATH.iterdir())
        except Exception:
            self.translations = ['English']
        self.load_lang()
        appSignalMgr.settings_locale_updated.connect(self.load_lang)

    def load_lang(self):
        lang = app_settings.value("locale")
        if not lang:
            lang = 'English'
        try:
            path = Path(TR_PATH, f'{lang}.json').absolute().as_posix()
            with open(path, 'r', encoding='utf-8') as fp:
                self._lang = json.load(fp)
                _ = self._lang['context']
        except Exception as exc:
            logging.warning(exc)
        appSignalMgr.translator_updated.emit()

    def translate(self, ctx: str = 'root', text: str = "", ):
        context = self._lang['context'].get(ctx)
        if context is not None:
            translated_text = context.get(text)
            if translated_text:
                return translated_text

            logging.warning(f"Need translation: {ctx}: {text}")
            self._lang['context'][ctx][text] = text
            self._update_lang()
        else:
            logging.warning(f"Need translation: {ctx}: {text}")
            self._lang['context'][ctx] = {text: text}
            self._update_lang()
            return text

    def _update_lang(self):
        lang = app_settings.value("locale")
        if not lang:
            lang = 'English'
        try:
            path = Path(TR_PATH, f'{lang}.json').absolute().as_posix()
            with open(path, 'w', encoding='utf-8') as fp:
                json.dump(self._lang, fp, ensure_ascii=False)
        except Exception as exc:
            logger.exception(exc)


translator = Translator()
tr = translator.translate
