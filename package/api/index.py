import sys
import os
import traceback
from fastapi import FastAPI, Response

# 获取当前文件目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取 package 目录 (当前目录的父目录)
package_dir = os.path.dirname(current_dir)

# 将 package 目录添加到 Python 路径，以便可以导入 backend 模块
sys.path.append(package_dir)
# 将 backend 目录也添加到 Python 路径，以便内部模块可以使用 from app... 导入
sys.path.append(os.path.join(package_dir, 'backend'))

try:
    # 尝试导入 FastAPI 应用
    from backend.app.main import app
except Exception as e:
    # 如果导入失败，创建一个临时的 FastAPI 应用来显示错误
    error_msg = f"Failed to start application: {str(e)}\n\nTraceback:\n{traceback.format_exc()}"
    print(error_msg)
    
    app = FastAPI()
    
    @app.api_route("/{path_name:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "HEAD"])
    async def catch_all(path_name: str):
        return Response(content=error_msg, media_type="text/plain", status_code=500)
