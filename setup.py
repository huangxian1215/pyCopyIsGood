# 导入所需的库
from distutils.core import setup

import PyQt5
import py2exe

APP = [{ 'script': 'main.py'}]
DATA_FILES = []
OPTIONS = {'iconfile':'src/ocr.ico'}
# OPTIONS = {'argv_emulation': True}
setup(
    windows=APP,
    data_files=DATA_FILES,
    options={'py2app':OPTIONS},
    setup_requires=['py2app'],
    )
