import qrcode
import base64
import io
from PIL import Image


def text_to_qr_base64(
    text: str,
    error_correction: int = qrcode.constants.ERROR_CORRECT_M,
    box_size: int = 10,
    border: int = 4,
    fill_color: str = "black",
    back_color: str = "white",
    image_format: str = "PNG",
) -> str:
    """
    将输入的字符串转换成QR码图片，并返回base64编码的字符串

    Args:
        text (str): 要转换的文本内容
        error_correction (int): 错误纠正级别，默认为中等级别
        box_size (int): 每个方块的像素大小，默认为10
        border (int): 边框的方块数量，默认为4
        fill_color (str): 前景色，默认为黑色
        back_color (str): 背景色，默认为白色
        image_format (str): 图片格式，默认为PNG

    Returns:
        str: base64编码的图片字符串

    Raises:
        ValueError: 当输入文本为空时
        Exception: 其他处理异常
    """
    if not text or not text.strip():
        raise ValueError("输入文本不能为空")

    try:
        # 创建QR码实例
        qr = qrcode.QRCode(
            version=1,  # 控制QR码的大小，1是最小的
            error_correction=error_correction,
            box_size=box_size,
            border=border,
        )

        # 添加数据
        qr.add_data(text)
        qr.make(fit=True)

        # 创建图片
        img = qr.make_image(fill_color=fill_color, back_color=back_color)

        # 将图片转换为字节流
        img_buffer = io.BytesIO()
        img.save(img_buffer, format=image_format)
        img_buffer.seek(0)

        # 转换为base64
        img_base64 = base64.b64encode(img_buffer.getvalue()).decode("utf-8")

        return img_base64

    except Exception as e:
        raise Exception(f"生成QR码时发生错误: {str(e)}")


def save_qr_base64_to_file(
    base64_string: str, filename: str, image_format: str = "PNG"
) -> None:
    """
    将base64编码的图片保存到文件

    Args:
        base64_string (str): base64编码的图片字符串
        filename (str): 保存的文件名
        image_format (str): 图片格式，默认为PNG
    """
    try:
        # 解码base64字符串
        img_data = base64.b64decode(base64_string)

        # 创建图片对象
        img = Image.open(io.BytesIO(img_data))

        # 保存图片
        img.save(filename, format=image_format)
        print(f"图片已保存到: {filename}")

    except Exception as e:
        raise Exception(f"保存图片时发生错误: {str(e)}")


def get_data_url(base64_string: str, image_format: str = "PNG") -> str:
    """
    将base64字符串转换为Data URL格式，可以直接在HTML中使用

    Args:
        base64_string (str): base64编码的图片字符串
        image_format (str): 图片格式，默认为PNG

    Returns:
        str: Data URL格式的字符串
    """
    mime_type = f"image/{image_format.lower()}"
    return f"data:{mime_type};base64,{base64_string}"


if __name__ == "__main__":
    # 示例用法
    test_text = "Hello, World! 这是一个测试QR码"

    try:
        # 生成QR码的base64编码
        qr_base64 = text_to_qr_base64(test_text)
        print("QR码生成成功!")
        print(f"Base64长度: {len(qr_base64)}")
        print(f"Base64前50个字符: {qr_base64[:50]}...")

        # 生成Data URL
        data_url = get_data_url(qr_base64)
        print(f"Data URL前100个字符: {data_url[:100]}...")

        # 保存到文件（可选）
        save_qr_base64_to_file(qr_base64, "test_qr.png")

    except Exception as e:
        print(f"错误: {e}")
