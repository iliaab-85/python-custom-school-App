import rembg
import numpy as np
import io
from PIL import Image

# بارگیری تصویر
with open('Untitled.png', 'rb') as f:
    img_data = f.read()

    # حذف بکگراند
    result = rembg.remove(img_data)

    # تبدیل داده‌های بایت به تصویر
    img = Image.open(io.BytesIO(result)).convert("RGBA")

    # نمایش تصویر
    img.show()

    # ذخیره تصویر بدون بک‌گراند
    img.save('54.png')