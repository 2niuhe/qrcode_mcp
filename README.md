# QR Code Generation MCP Server

A QR code generation MCP server implemented using FastMCP, supporting text-to-QR code conversion with base64 encoding output.

## Features

- Support for any text to QR code conversion (including Chinese characters)
- Customizable colors and styles
- Base64 encoding
- Support for STDIO, HTTP, and SSE transport modes

## Installation

```bash
uv sync
# or
pip install qrcode Pillow mcp
```

## Usage

### 1. MCP Server Mode

#### Start Server
```bash
# STDIO mode (for Claude Desktop)
python qrcode_mcp_server.py

# HTTP mode
python qrcode_mcp_server.py --http --host 127.0.0.1 --port 8008

# SSE mode (Server-Sent Events) Deprecated
python qrcode_mcp_server.py --sse --host 127.0.0.1 --port 8008
```

#### Configure Claude Desktop
Add to `~/Library/Application Support/Claude/claude_desktop_config.json`:

**STDIO Mode (Local Use):**
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

**HTTP Mode (Network Deployment):**
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

**SSE Mode (Server-Sent Events):**
```json
{
  "mcpServers": {
    "qrcode-mcp": {
      "serverUrl": "http://127.0.0.1:8008/sse"
    }
  }
}
```

### 2. Direct Python API Usage

```python
from qrcode_utils import text_to_qr_base64

# Basic usage
base64_result = text_to_qr_base64("Hello, World!")

# Custom styling
base64_result = text_to_qr_base64(
    "Custom QR Code",
    box_size=15,
    fill_color="darkblue",
    back_color="lightgray"
)
```

## MCP Tools

### `generate_qr_code`
Generate QR code and return base64 encoding.

**Parameters:**
- `text` (required): Text content to convert
- `box_size` (optional): Pixel size of each box, default 10
- `border` (optional): Number of border boxes, default 4
- `fill_color` (optional): Foreground color, default "black"
- `back_color` (optional): Background color, default "white"
- `return_data_url` (optional): Whether to return Data URL format, default false

## Testing

```bash
python test_mcp_client.py
```

## License

MIT License 