from detect_new_raw_image import compare_file_names
from transform_image import transform_raw_image
from message_slack import send_processed_image
import time

# get a list of new images in raw that have not been processed. 
new_raw_images=compare_file_names()

# transform image(s) and send the image to Slack.
if len(new_raw_images)!=0:
	for image_name in new_raw_images:
		transform_raw_image(image_name)
		send_processed_image(image_name)
else:
	print('No new images to send')
