import cv2
import sys
import os


def threshold_grayscale(
    image_path=r"c:\Users\ASUS\Downloads\p3.jpg",
    threshold_value=127
):
    # Validate file path
    if not os.path.isfile(image_path):
        print(f"Error: File '{image_path}' not found.")
        return

    # Read image in grayscale mode
    img_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    if img_gray is None:
        print("Error: Unable to read image. Ensure it's a valid image file.")
        return

    # Apply binary thresholding
    _, thresh_img = cv2.threshold(
        img_gray,
        threshold_value,
        255,
        cv2.THRESH_BINARY
    )

    def make_panel(image, label):
        panel_width, panel_height = 400, 300
        image_height, image_width = image.shape
        scale = min(panel_width / image_width, 270 / image_height)
        resized_width = max(1, int(image_width * scale))
        resized_height = max(1, int(image_height * scale))
        interpolation = cv2.INTER_NEAREST if label == "Thresholded" else cv2.INTER_AREA
        preview = cv2.resize(image, (resized_width, resized_height),
                             interpolation=interpolation)
        left = (panel_width - resized_width) // 2
        top = 30 + (270 - resized_height) // 2
        panel = cv2.copyMakeBorder(
            preview, top, panel_height - top - resized_height,
            left, panel_width - left - resized_width,
            cv2.BORDER_CONSTANT, value=0
        )
        cv2.putText(panel, label, (10, 22), cv2.FONT_HERSHEY_SIMPLEX,
                    0.55, 255, 1, cv2.LINE_AA)
        return panel

    combined = cv2.hconcat((
        make_panel(img_gray, "Original Grayscale"),
        make_panel(thresh_img, "Thresholded Image")
    ))
    cv2.imshow("Grayscale and Threshold", combined)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        # Use the default image
        threshold_grayscale()
    else:
        img_path = sys.argv[1]
        thresh_val = int(sys.argv[2]) if len(sys.argv) > 2 else 127
        threshold_grayscale(img_path, thresh_val)