#!/usr/bin/env python3
"""
图片信息读取器 — 一键查看图片的所有信息

用法: python image_info.py photo.jpg [photo2.png ...]
"""

import sys
import os
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS


def format_size(bytes_val: int) -> str:
    """字节转可读大小"""
    for unit in ["B", "KB", "MB", "GB"]:
        if bytes_val < 1024:
            return f"{bytes_val:.1f}{unit}"
        bytes_val /= 1024
    return f"{bytes_val:.1f}TB"


def read_image(path: str) -> dict:
    """读取图片完整信息"""
    img = Image.open(path)
    stat = os.stat(path)

    info = {
        "路径": path,
        "格式": img.format,
        "模式": img.mode,
        "尺寸": f"{img.width} × {img.height} px",
        "宽高比": f"{img.width/img.height:.2f}",
        "总像素": f"{img.width * img.height / 1e6:.2f} MP",
        "文件大小": format_size(stat.st_size),
        "创建时间": str(stat.st_ctime),
    }

    # EXIF
    try:
        exif = img.getexif()
        if exif:
            for tag_id, value in exif.items():
                if tag_id in TAGS:
                    tag = TAGS[tag_id]
                    if isinstance(value, bytes):
                        continue
                    info[f"EXIF.{tag}"] = str(value)
    except Exception:
        pass

    return info


def main():
    if len(sys.argv) < 2:
        print("用法: python image_info.py <图片路径> [...]")
        sys.exit(1)

    for path in sys.argv[1:]:
        if not Path(path).exists():
            print(f"[错误] 文件不存在: {path}\n")
            continue

        try:
            info = read_image(path)
            print("=" * 50)
            for key, value in info.items():
                print(f"  {key:12s}: {value}")
            print()
        except Exception as e:
            print(f"[错误] {path}: {e}\n")


if __name__ == "__main__":
    main()
