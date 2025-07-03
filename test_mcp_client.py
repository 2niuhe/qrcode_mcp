#!/usr/bin/env python3
"""
MCP客户端测试脚本
用于测试QR码MCP服务器功能
"""

import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def test_qrcode_mcp():
    """
    测试QR码MCP服务器
    """
    # 服务器参数 - 直接使用主服务器文件
    server_params = StdioServerParameters(
        command="python", args=["qrcode_mcp_server.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 初始化会话
            await session.initialize()

            print("🔌 MCP会话初始化成功")

            # 获取可用工具列表
            tools = await session.list_tools()
            print(f"📋 可用工具: {[tool.name for tool in tools.tools]}")

            # 测试基础QR码生成
            print("\n🧪 测试QR码生成")
            result = await session.call_tool(
                "generate_qr_code",
                {"text": "Hello MCP World!", "box_size": 10, "border": 4},
            )
            print("✅ QR码生成成功，类型:", result.content[0].type)

            print("\n✅ MCP QR码工具测试完成！")


if __name__ == "__main__":
    print("🚀 启动QR码MCP客户端测试")
    asyncio.run(test_qrcode_mcp())
