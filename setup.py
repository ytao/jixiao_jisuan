#coding=utf8
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable(r'D:\快盘\cache\excel_js\excel_js.py', base=base)
]

setup(name='excel_js',
      version = '1.0',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)
