import cv2

def transform_raw_image(file_name:str, width=150, height=150 ) -> str:
    """Use open-cv library to change the raw image to greyscale, resize the image and write as a jpg to the processed folder.
    File name to operate on should not include the path and should include the filetype eg: .png.
    This returns None after storing processed image.
    In prod the raspberry pi camera will store pictures on JPEG format"""
    # possibly use cvtColor to transform from one color space to another instead of using IMREAD_GRAYSCALE
    img = cv2.imread('images/raw/'+file_name, cv2.IMREAD_GRAYSCALE)
    resized = cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)
    processed_file_name = file_name.split('.', 1)[0]+'.jpg'
    cv2.imwrite('images/processed/'+processed_file_name, resized, [int(cv2.IMWRITE_JPEG_QUALITY), 95])
    return processed_file_name
