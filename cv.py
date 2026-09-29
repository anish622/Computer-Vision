import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread(r"C:\Users\Student\Downloads\xyz.webp")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

bright = cv2.add(image,
                 np.ones(image.shape, dtype=np.uint8) * 50)

dark = cv2.subtract(image,
                    np.ones(image.shape, dtype=np.uint8) * 50)

h_flip = cv2.flip(image, 1)
v_flip = cv2.flip(image, 0)

red = image[:, :, 0]
green = image[:, :, 1]
blue = image[:, :, 2]

gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
negative = 255 - image

plt.figure(figsize=(18, 12))   

plt.subplot(3, 4, 1)
plt.imshow(image);         plt.title('Original');      plt.axis('off')
plt.subplot(3, 4, 2)
plt.imshow(bright);        plt.title('Brighter +50');  plt.axis('off')
plt.subplot(3, 4, 3)
plt.imshow(dark);          plt.title('Darker -50');    plt.axis('off')

# Row 2 — Flip
plt.subplot(3, 4, 5)
plt.imshow(h_flip);        plt.title('H-Flip');        plt.axis('off')
plt.subplot(3, 4, 6)
plt.imshow(v_flip);        plt.title('V-Flip');        plt.axis('off')

# Row 2 — Color Channels
plt.subplot(3, 4, 7)
plt.imshow(red,   cmap='Reds');   plt.title('Red');   plt.axis('off')
plt.subplot(3, 4, 8)
plt.imshow(green, cmap='Greens'); plt.title('Green'); plt.axis('off')

# Row 3
plt.subplot(3, 4, 9)
plt.imshow(blue,  cmap='Blues');  plt.title('Blue');  plt.axis('off')
plt.subplot(3, 4, 10)
plt.imshow(gray,  cmap='gray');   plt.title('Gray');  plt.axis('off')
plt.subplot(3, 4, 11)
plt.imshow(negative);  plt.title('Negative'); plt.axis('off')

plt.tight_layout()
plt.show()
plt.subplot(1, 3, 2)
plt.imshow(bright)
plt.title('Brighter Image (+50)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(dark)
plt.title('Darker Image (-50)')
plt.axis('off')

plt.show()