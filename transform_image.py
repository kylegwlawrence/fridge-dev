import cv2

def transform_raw_image(image_name:str, width=150, height=150 ) -> None:
    """Take an image name from the raw image folder,
    read it in and comvert to greyscale, resize it,
    and write to processed folder as a JPEG file."""

    # possibly use cvtColor to transform from one color space to another instead of using IMREAD_GRAYSCALE
    img = cv2.imread('images/raw/'+image_name, cv2.IMREAD_GRAYSCALE)
    resized = cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)
    cv2.imwrite('images/processed/'+image_name, resized, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
    return None