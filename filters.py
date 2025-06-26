from PIL import Image, ImageFilter, ImageOps
import numpy as np
import cv2

def apply_filter(image_path, filter_type):
    image = Image.open(image_path)

    # Apply the filter based on the type selected by the user
    if filter_type == "mean":
        image = image.filter(ImageFilter.BoxBlur(5))  # Mean blur
    elif filter_type == "median":
        image = image.filter(ImageFilter.MedianFilter(5))  # Median blur
    elif filter_type == "gaussian":
        image = image.filter(ImageFilter.GaussianBlur(5))  # Gaussian blur
    elif filter_type == "grayscale":
        image = ImageOps.grayscale(image)  # Convert to grayscale
    elif filter_type == "sharpen":
        image = image.filter(ImageFilter.SHARPEN)  # Sharpen

    # Save the filtered image and return its path
    output_path = image_path.replace(".png", f"_{filter_type}.png")
    image.save(output_path)

    return output_path
