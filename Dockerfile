FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装项目依赖
RUN pip install --no-cache-dir qrcode>=7.4.2 Pillow>=10.0.0 mcp>=1.0.0 uvicorn>=0.30.0

# 复制源代码
COPY qrcode_mcp_server.py qrcode_utils.py ./

# 暴露端口
EXPOSE 8008

# 以HTTP模式启动服务器，监听所有接口
CMD ["python", "qrcode_mcp_server.py", "--http", "--host", "0.0.0.0", "--port", "8008"] 