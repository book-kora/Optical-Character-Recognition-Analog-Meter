import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.datasets import cifar10

# โหลดข้อมูล CIFAR-10
(train_images, train_labels), _ = cifar10.load_data()
img = train_images[105]  # ลองใช้ภาพที่ 105

# แสดงภาพ
fig, ax = plt.subplots()
im = ax.imshow(img)

# ฟังก์ชันเมื่อคลิกที่ภาพ
def onclick(event):
    if event.inaxes == ax:
        x, y = int(event.xdata), int(event.ydata)
        rgb = img[y, x]  # Note: row = y, col = x
        print(f"Pixel at ({x}, {y}): R={rgb[0]}, G={rgb[1]}, B={rgb[2]}")
        ax.set_title(f"RGB at ({x}, {y}): {rgb}")
        fig.canvas.draw()

# เชื่อม event
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.title("Click on the image to see RGB values")
plt.show()
