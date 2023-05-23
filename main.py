from detect_new_raw_image import compare_file_names
from transform_image import transform_image
from message_slack import send_processed_image

# determine if new images exist in raw - change this to return None if no new raw images
new_raw_files=compare_file_names('images/raw','images/processed')

# transform image - change to return filepath of new image for message_slack consumption
for image in list(new_raw_files):
	transform_image(image)
	send_processed_image('images/processed/'+image+'.jpg'

