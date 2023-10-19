# -*- coding: utf-8 -*-

from py_balcalc.logger import logger


def load_qss(file_name):
    """use setStylesheet(load_qss(filename))"""
    try:
        with open(file_name, 'r') as fh:
            return fh.read()
    except FileNotFoundError as err:
        logger.exception(err)
        return ''


def main_app_qss():
    """use setStylesheet(main_app_qss())"""
    try:
        with open('./qss/application.qss', 'r') as fh:
            return fh.read()
    except FileNotFoundError as err:
        logger.exception(err)
        return ''
