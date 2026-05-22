# Python 图像读取基础

学习如何读懂本地图片的「内在信息」。

## 图像的本质

一张图 = 一个数字矩阵

```
┌────────────────────────────────┐
│ (0,0)  ←──────── 宽度 ───────→ │
│  ┌─────┬─────┬─────┬─────┐    │
│  │ R G B│ R G B│ R G B│ ... │    │  每个格子 = 1个像素
│  │25,80,│30,90,│40,95,│     │    │
│  │  200 │  210 │  220 │     │    │
│  ├─────┼─────┼─────┼─────┤    │
│  │ R G B│ R G B│ R G B│ ... │    │
│  │ ...  │ ...  │ ...  │     │    │
│  └─────┴─────┴─────┴─────┘    │
│              ↓ 高度            │
└────────────────────────────────┘
```

## 三大核心信息

用 Pillow 一次性读取图像的所有关键信息：

```python
from PIL import Image
import os

img = Image.open("photo.jpg")

# 1. 基本信息
print(f"格式:   {img.format}")      # JPEG/PNG/GIF/BMP
print(f"模式:   {img.mode}")        # RGB/RGBA/L/CMYK
print(f"尺寸:   {img.size}")        # (宽, 高) 元组
print(f"宽:     {img.width}px")
print(f"高:     {img.height}px")
print(f"文件大小: {os.path.getsize('photo.jpg') / 1024:.1f} KB")

# 2. 元数据 (EXIF)
exif = img.getexif()
if exif:
    for k, v in exif.items():
        print(f"  EXIF {k}: {v}")
    # 常用 EXIF 字段
    print(f"拍摄时间: {exif.get(36867)}")   # DateTimeOriginal
    print(f"相机型号: {exif.get(272)}")     # Model
    print(f"GPS信息:  {exif.get(34853)}")  # GPSInfo

# 3. 像素数据
pixels = list(img.getdata())  # 所有像素的 (R,G,B) 元组列表
print(f"总像素数: {len(pixels)}")
print(f"第一个像素: {pixels[0]}")
```

## 颜色模式

| mode | 含义 | 通道 | 示例 |
|------|------|------|------|
| `RGB` | 红绿蓝 | 3 | 照片 |
| `RGBA` | RGB + 透明度 | 4 | PNG图标 |
| `L` | 灰度 | 1 | 黑白 |
| `CMYK` | 印刷四色 | 4 | 打印用 |
| `HSV` | 色相/饱和度/明度 | 3 | 调色 |
| `1` | 二值 | 1bit | 纯黑白 |

## 实战：读取一张图片的全部信息

```python
from PIL import Image
from PIL.ExifTags import TAGS
import os

def read_image_info(path: str) -> dict:
    """读取图片的所有可读信息"""
    img = Image.open(path)
    info = {
        "文件名": os.path.basename(path),
        "格式": img.format,
        "模式": img.mode,
        "尺寸": f"{img.width} x {img.height}",
        "文件大小": f"{os.path.getsize(path)/1024:.1f}KB",
        "宽高比": f"{img.width/img.height:.2f}:1",
        "总像素": f"{img.width * img.height / 1_000_000:.1f}MP",
    }

    # EXIF
    exif = img.getexif()
    if exif:
        for tag_id, value in exif.items():
            tag_name = TAGS.get(tag_id, tag_id)
            if isinstance(value, bytes):
                continue  # 跳过二进制
            info[tag_name] = str(value)

    return info


# 使用
if __name__ == "__main__":
    import sys
    for path in sys.argv[1:]:
        info = read_image_info(path)
        for k, v in info.items():
            print(f"  {k}: {v}")
        print()
```
