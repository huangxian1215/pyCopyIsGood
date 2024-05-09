# 导入所需的库
from distutils.core import setup
import py2exe

# 设置打包的选项
options = {
    'py2exe': {
        'bundle_files': 1,  # 打包成单个可执行文件
        'compressed': True,  # 压缩可执行文件
        'optimize': 2,  # 优化打包后的可执行文件
    }
}

# 要打包的Python脚本
scripts = ['main.py']

# 调用setup函数进行打包
setup(name='pic2txt',version='0.0',py_modules=[], console=scripts, options=options)