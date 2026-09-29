import cv2
import matplotlib.pyplot as plt

image = cv2.imread("C:\\Users\\Student\\Downloads\\images (2).jpg")

if image is None:
    print("Image not found. Check the file path.")
    exit()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

T = 127
ret, result = cv2.threshold(gray, T, 255, cv2.THRESH_BINARY)

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Step 1: Original Image")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(gray, cmap="gray")
plt.title("Step 2: Grayscale Image")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(result, cmap="gray")
plt.title(f"Step 3: Threshold Result (T={T})")
plt.axis("off")

plt.tight_layout()
plt.show()

print(f"Threshold value used : {T}")
print("Pixels in result     : only 0 and 255")