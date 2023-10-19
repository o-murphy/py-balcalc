# -*- coding: utf-8 -*-

from py_balcalc.logger import logger
import os


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
        qss_path = os.path.join(os.path.dirname(__file__), '../qss/application.qss')
        with open(qss_path, 'r') as fh:
            return fh.read()
    except FileNotFoundError as err:
        logger.exception(err)
        return ''
