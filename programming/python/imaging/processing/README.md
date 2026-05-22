# 图像处理

不仅「看」图片，还要「理解」图片内容。

## 基础操作

```python
from PIL import Image, ImageFilter, ImageEnhance

img = Image.open("photo.jpg")

# 裁剪 — 提取 ROI (感兴趣区域)
# crop((左, 上, 右, 下))
face = img.crop((100, 50, 300, 300))
face.save("face.jpg")

# 缩放
thumb = img.resize((200, 200))          # 直接缩放
thumb2 = img.thumbnail((200, 200))      # 保持比例

# 旋转
rotated = img.rotate(45, expand=True)   # 逆时针45度
flipped = img.transpose(Image.FLIP_LEFT_RIGHT)  # 镜像

# 转换为灰度
gray = img.convert("L")
```

## 像素级分析

```python
import numpy as np

# 转为 numpy 数组 (三维: 高×宽×通道)
arr = np.array(img)
print(f"形状: {arr.shape}")   # (高, 宽, 3) 或 (高, 宽, 4)

# 通道分离
r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]

# 统计信息
print(f"R 均值: {r.mean():.1f}")
print(f"G 均值: {g.mean():.1f}")
print(f"B 均值: {b.mean():.1f}")
print(f"最亮像素: {arr.max()}")
print(f"最暗像素: {arr.min()}")

# 判断图片整体色调
if r.mean() > g.mean() and r.mean() > b.mean():
    print("偏暖色调 (红)")
elif b.mean() > r.mean():
    print("偏冷色调 (蓝)")
```

## 滤镜与增强

```python
# 模糊
blurred = img.filter(ImageFilter.BLUR)
gaussian = img.filter(ImageFilter.GaussianBlur(radius=5))

# 边缘检测
edges = img.filter(ImageFilter.FIND_EDGES)

# 锐化
sharp = img.filter(ImageFilter.SHARPEN)

# 增强
enhancer = ImageEnhance.Brightness(img)
bright = enhancer.enhance(1.5)    # 1.5倍亮度

enhancer = ImageEnhance.Contrast(img)
contrast = enhancer.enhance(1.3)   # 1.3倍对比度

enhancer = ImageEnhance.Color(img)
vivid = enhancer.enhance(2.0)     # 2倍饱和度
```

## 直方图：像素分布

```python
# 直方图 = 像素值分布图
hist = img.histogram()

# RGB 各有 256 级
r_hist = hist[:256]    # 红色通道分布
g_hist = hist[256:512] # 绿色通道分布
b_hist = hist[512:]    # 蓝色通道分布

# 简单的亮度判断
avg_brightness = sum(i * r_hist[i] for i in range(256)) / sum(r_hist)
if avg_brightness < 85:
    print("偏暗 — 可能是夜景/暗室")
elif avg_brightness > 170:
    print("偏亮 — 可能是雪景/过曝")
else:
    print("正常曝光")
```

## OpenCV 高级分析

```python
import cv2
import numpy as np

img = cv2.imread("photo.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 人脸检测 (需要 Haar Cascade 模型)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
print(f"检测到 {len(faces)} 张人脸")
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# 轮廓检测
edges = cv2.Canny(gray, 100, 200)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print(f"检测到 {len(contours)} 个轮廓")

# 颜色检测
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 检测红色区域
lower_red = np.array([0, 100, 100])
upper_red = np.array([10, 255, 255])
mask = cv2.inRange(hsv, lower_red, upper_red)
red_pixels = cv2.countNonZero(mask)
print(f"红色区域: {red_pixels} 像素 ({100*red_pixels/mask.size:.1f}%)")

# 图片相似度
def compare_images(path1, path2):
    """用直方图比较两张图相似度"""
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)
    hist1 = cv2.calcHist([img1], [0,1,2], None, [8,8,8], [0,256]*3)
    hist2 = cv2.calcHist([img2], [0,1,2], None, [8,8,8], [0,256]*3)
    score = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return score  # 1.0 = 完全相同
```
