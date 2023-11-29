import cv2
import os

def apply_mean_filter(image):
    return cv2.blur(image, (5, 5))

def apply_median_filter(image):
    return cv2.medianBlur(image, 5)

def apply_k_closest_averaging(image, k):
    return cv2.blur(image, (k, k))

def apply_threshold_averaging(image, threshold):
    _, thresholded = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)
    return cv2.blur(thresholded, (5, 5))

def main():
    input_path = '/content/pic22.png'
    output_folder = '/content/output'

    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read the input image
    image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

    # Apply filters
    mean_filtered = apply_mean_filter(image)
    median_filtered = apply_median_filter(image)
    k_closest_filtered = apply_k_closest_averaging(image, k=5)  # Adjust k as needed
    threshold_filtered = apply_threshold_averaging(image, threshold=210)  # Adjust threshold as needed

    # Save the output images with filter names
    mean_output_path = os.path.join(output_folder, f'mean_{os.path.basename(input_path)}')
    median_output_path = os.path.join(output_folder, f'median_{os.path.basename(input_path)}')
    k_closest_output_path = os.path.join(output_folder, f'k_closest_{os.path.basename(input_path)}')
    threshold_output_path = os.path.join(output_folder, f'threshold_{os.path.basename(input_path)}')

    cv2.imwrite(mean_output_path, mean_filtered)
    cv2.imwrite(median_output_path, median_filtered)
    cv2.imwrite(k_closest_output_path, k_closest_filtered)
    cv2.imwrite(threshold_output_path, threshold_filtered)

if __name__ == "__main__":
    main()
