import logging
from logging.handlers import TimedRotatingFileHandler
import os
import sys

from regression_model.config import config

# logging.getLogger（ 'someLogger'）を複数回呼び出すと、同じロガーオブジェクトへの参照が返されます。
# これは、同じモジュール内だけでなく、同じPythonインタープリタープロセス内にある限り、モジュール間でも同様です。

FORMATTER = logging.Formatter(
    "%(asctime)s — %(name)s — %(levelname)s —"
    "%(funcName)s:%(lineno)d — %(message)s")


def get_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler
