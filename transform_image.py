import cv2

# snap image from camera

# read, transform, and store image
def transform_image(filename:str) -> None:
    """Use open-cv library to change to greyscale, resize the image and write as a jpg to processed folder"""
    img = cv2.imread('images/raw/'+filename, cv2.IMREAD_GRAYSCALE)
    #resize to one common size
    width = 150
    height = 150
    resized = cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)
    new_filename = filename.split('.', 1)[0]+'.jpg'
    cv2.imwrite('images/processed/'+new_filename, resized, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
    # possibly use cvtColor to transform from one color space to another instead of using IMREAD_GRAYSCALE
    return None

transform_image('Fridge_2.jpg')
