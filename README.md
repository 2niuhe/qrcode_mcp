# QR码生成MCP服务器

一个使用FastMCP实现的QR码生成MCP服务器，支持将文本转换为QR码图像并返回base64编码。

## 功能特性

- 支持任意文本转QR码（包括中文字符）
- 自定义颜色和样式
- 输出base64编码或Data URL格式
- 支持STDIO和HTTP传输模式

## 安装

```bash
uv sync
# 或者
pip install qrcode[pil] Pillow mcp
```

## 使用方法

### 1. MCP服务器模式

#### 启动服务器
```bash
# STDIO模式（用于Claude Desktop）
python qrcode_mcp_server.py

# HTTP模式（用于网络部署）
python qrcode_mcp_server.py --http --host 127.0.0.1 --port 8008
```

#### 配置Claude Desktop
在`~/Library/Application Support/Claude/claude_desktop_config.json`中添加：

**STDIO模式（本地使用）：**
```json
{
  "mcpServers": {
    "qrcode-mcp": {
      "command": "python",
      "args": ["/ABSOLUTE/PATH/TO/qrcode_mcp/qrcode_mcp_server.py"],
      "cwd": "/ABSOLUTE/PATH/TO/qrcode_mcp"
    }
  }
}
```

**HTTP模式（网络部署）：**
```json
{
  "mcpServers": {
    "qrcode-mcp": {
      "transport": "http",
      "url": "http://127.0.0.1:8008/mcp/"
    }
  }
}
```

### 2. 直接使用Python API

```python
from qrcode_utils import text_to_qr_base64

# 基本使用
base64_result = text_to_qr_base64("Hello, World!")

# 自定义样式
base64_result = text_to_qr_base64(
    "Custom QR Code",
    box_size=15,
    fill_color="darkblue",
    back_color="lightgray"
)
```

## MCP工具

### `generate_qr_code`
生成QR码并返回base64编码。

**参数：**
- `text` (required): 要转换的文本内容
- `box_size` (optional): 每个方块像素大小，默认10
- `border` (optional): 边框方块数量，默认4
- `fill_color` (optional): 前景色，默认"black"
- `back_color` (optional): 背景色，默认"white"
- `return_data_url` (optional): 是否返回Data URL格式，默认false

## 测试

```bash
python test_mcp_client.py
```

## 许可证

MIT License 