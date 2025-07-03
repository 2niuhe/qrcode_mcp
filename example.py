#!/usr/bin/env python3
"""
QR码生成工具使用示例
"""

from qrcode_utils import text_to_qr_base64, save_qr_base64_to_file, get_data_url


def main():
    """主函数演示各种用法"""

    # 示例1: 简单文本
    print("=== 示例1: 简单文本 ===")
    text1 = "Hello, World!"
    base64_result1 = text_to_qr_base64(text1)
    print(f"文本: {text1}")
    print(f"Base64 (前50字符): {base64_result1[:50]}...")
    print()

    # 示例2: 中文文本
    print("=== 示例2: 中文文本 ===")
    text2 = "你好，世界！这是一个QR码测试"
    base64_result2 = text_to_qr_base64(text2)
    print(f"文本: {text2}")
    print(f"Base64 (前50字符): {base64_result2[:50]}...")
    print()

    # 示例3: URL
    print("=== 示例3: URL ===")
    text3 = "https://www.example.com"
    base64_result3 = text_to_qr_base64(text3)
    print(f"文本: {text3}")
    print(f"Base64 (前50字符): {base64_result3[:50]}...")
    print()

    # 示例4: 自定义样式
    print("=== 示例4: 自定义样式 ===")
    text4 = "Custom Style QR Code"
    base64_result4 = text_to_qr_base64(
        text4,
        box_size=15,  # 更大的方块
        border=2,  # 更小的边框
        fill_color="darkblue",  # 深蓝色前景
        back_color="lightgray",  # 浅灰色背景
    )
    print(f"文本: {text4}")
    print(f"Base64 (前50字符): {base64_result4[:50]}...")
    print()

    # 示例5: 生成Data URL
    print("=== 示例5: Data URL ===")
    data_url = get_data_url(base64_result1)
    print(f"Data URL (前100字符): {data_url[:100]}...")
    print("可以直接在HTML的<img>标签中使用此Data URL")
    print()

    # 示例6: 保存到文件
    print("=== 示例6: 保存到文件 ===")
    try:
        save_qr_base64_to_file(base64_result2, "chinese_qr.png")
        save_qr_base64_to_file(base64_result4, "custom_style_qr.png")
    except Exception as e:
        print(f"保存文件时出错: {e}")


if __name__ == "__main__":
    main()
