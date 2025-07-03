#!/usr/bin/env python3
"""
QR码生成MCP服务器
使用FastMCP实现标准MCP协议
"""

import logging
from typing import Any
from mcp.server.fastmcp import FastMCP
from mcp.types import ImageContent
from qrcode_utils import text_to_qr_base64

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("qrcode-mcp-server")

# 初始化FastMCP服务器
mcp = FastMCP("qrcode-mcp")


@mcp.tool()
async def generate_qr_code(
    text: str,
    box_size: int = 10,
    border: int = 4,
    fill_color: str = "black", 
    back_color: str = "white"
) -> dict:
    """Generate QR code(生成二维码图片) from text and return as image with description.

    Args:
        text: Text content to convert to QR code
        box_size: Size of each box in pixels (1-50)
        border: Number of boxes for border (0-20)
        fill_color: Foreground color
        back_color: Background color
    """
    if not text or not text.strip():
        raise ValueError("Text content cannot be empty")
    
    # 验证参数范围
    if not (1 <= box_size <= 50):
        raise ValueError("box_size must be between 1 and 50")
    
    if not (0 <= border <= 20):
        raise ValueError("border must be between 0 and 20")
    
    try:
        # 生成QR码的base64编码
        base64_result = text_to_qr_base64(
            text=text,
            box_size=box_size,
            border=border,
            fill_color=fill_color,
            back_color=back_color,
            image_format="JPEG"
        )
        
        # 按照MCP文档要求的格式返回图片
        return ImageContent(
            type="image",
            data=base64_result,
            mimeType="image/jpeg"
        )
    
    except Exception as e:
        logger.error(f"Failed to generate QR code: {e}")
        raise RuntimeError(f"Failed to generate QR code: {str(e)}")


def main_stdio():
    """STDIO传输模式入口点"""
    logger.info("启动QR码MCP服务器 (STDIO传输模式)")
    mcp.run(transport='stdio')


def main_http(host: str = "127.0.0.1", port: int = 8008):
    """HTTP传输模式入口点"""
    import uvicorn
    logger.info(f"启动QR码MCP服务器 (HTTP传输模式) - {host}:{port}")
    app = mcp.streamable_http_app()
    uvicorn.run(app, host=host, port=port)



def main_http_with_args():
    """带命令行参数解析的HTTP服务器启动器"""
    import argparse
    import sys
    
    # 如果从主脚本调用，需要过滤掉 --http 参数
    argv = sys.argv[1:]
    if argv and argv[0] == "--http":
        argv = argv[1:]
    
    parser = argparse.ArgumentParser(description="QR码MCP服务器 - HTTP传输模式")
    parser.add_argument("--host", default="127.0.0.1", help="绑定的主机地址")
    parser.add_argument("--port", type=int, default=8008, help="绑定的端口号")
    
    args = parser.parse_args(argv)
    main_http(args.host, args.port)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--http":
        # HTTP模式：python qrcode_mcp_server.py --http [--host HOST] [--port PORT]
        main_http_with_args()
    else:
        # 默认使用STDIO模式
        main_stdio() 