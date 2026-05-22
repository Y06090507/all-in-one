# OCR 从图片提取文字

Optical Character Recognition — 把图片中的文字变成可复制的文本。

## Tesseract — 最常用开源 OCR

```python
import pytesseract
from PIL import Image

# 基础用法
img = Image.open("screenshot.png")
text = pytesseract.image_to_string(img)
print(text)

# 指定语言
text_cn = pytesseract.image_to_string(img, lang="chi_sim+eng")
# 中文需要下载: tesseract-lang-chi-sim

# 获取文字位置
data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
for i, word in enumerate(data["text"]):
    if word.strip():
        x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
        print(f"  '{word}' at ({x},{y}) {w}x{h}")
```

## 提高 OCR 准确率

原始图片 → 预处理 → OCR → 结果

```python
import cv2
import pytesseract

def preprocess_for_ocr(image_path: str) -> Image.Image:
    """图片预处理，提高识别率"""
    img = cv2.imread(image_path)

    # 1. 转灰度
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. 去噪
    denoised = cv2.fastNlMeansDenoising(gray)

    # 3. 二值化 (自适应阈值)
    binary = cv2.adaptiveThreshold(
        denoised, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )

    # 4. 去倾斜 (可选)
    # coords = np.column_stack(np.where(binary > 0))
    # angle = cv2.minAreaRect(coords)[-1]
    # ...

    return Image.fromarray(binary)


# 使用
img = preprocess_for_ocr("blurry_photo.jpg")
text = pytesseract.image_to_string(img, lang="eng")
print(text)
```

## 实战：截图文字提取器

```python
#!/usr/bin/env python3
"""从图片中提取文字并保存"""

import sys
from pathlib import Path
from PIL import Image
import pytesseract

def extract_text(image_path: str, lang: str = "eng") -> str:
    img = Image.open(image_path)

    # 获取原始尺寸
    w, h = img.size
    # 太小的图放大 (提高识别率)
    if w < 500:
        img = img.resize((w*2, h*2), Image.LANCZOS)

    text = pytesseract.image_to_string(img, lang=lang)
    return text.strip()


def main():
    for path in sys.argv[1:]:
        p = Path(path)
        if not p.exists():
            print(f"[跳过] 文件不存在: {path}")
            continue

        text = extract_text(str(p), lang="eng")
        out_path = p.with_suffix(".txt")
        out_path.write_text(text, encoding="utf-8")

        print(f"[{p.name}] → {out_path.name}")
        print(f"提取 {len(text)} 字符")
        print("-" * 40)
        print(text[:200] + ("..." if len(text) > 200 else ""))
        print()


if __name__ == "__main__":
    main()
```

## 中英文 OCR 安装

```bash
# Windows: 下载安装 tesseract
# https://github.com/UB-Mannheim/tesseract/wiki
# 安装时勾选中文语言包

# Linux:
sudo apt install tesseract-ocr tesseract-ocr-chi-sim

# 验证
tesseract --list-langs
```

## Tesseract 配置选项

| 参数 | 值 | 作用 |
|------|------|------|
| `--psm` | 3 | 自动检测 (默认) |
| | 6 | 单行文本 |
| | 4 | 单行可变大小 |
| | 7 | 单行 (视为一行) |
| | 8 | 单词 |
| | 10 | 单字符 |
| `--oem` | 3 | LSTM 引擎 (默认) |
| | 1 | LSTM only |
| | 0 | 传统引擎 |

```python
# PSM 配置
text = pytesseract.image_to_string(img, config='--psm 6')
```

## 常见准确率问题

| 问题 | 原因 | 解决 |
|------|------|------|
| 识别乱码 | 图片模糊/太小 | 放大2-3倍再识别 |
| 漏字 | 对比度低 | 调高对比度 |
| 多字 | 背景噪声 | 去噪+二值化 |
| 中文不识别 | 缺语言包 | 安装 chi_sim |
| 歪斜文字 | 拍摄角度 | 透视校正 |
