import sys
import os

# 获取当前文件目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取 package 目录 (当前目录的父目录)
package_dir = os.path.dirname(current_dir)

# 将 package 目录添加到 Python 路径，以便可以导入 backend 模块
sys.path.append(package_dir)

# 导入 FastAPI 应用
from backend.app.main import app
