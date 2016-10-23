#coding=utf8
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable(r'D:\excel_js\excel_js.py', base=base,icon = 'logo.ico')
]

setup(name=r'计算软件',
      version = '1.1',
      description = r'杨涛的计算软件',
      options = dict(build_exe = buildOptions),
      executables = executables)
