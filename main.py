from detect_new_raw_image import compare_file_names
from transform_image import transform_raw_image
from message_slack import send_processed_image
import time

# determine if new images exist in raw. Returns set of raw images not processed if any. 
new_raw_images=compare_file_names()

# transform image if exists
if len(new_raw_images)!=0:
	for image_name in new_raw_images:
		transform_raw_image(image_name)
		time.sleep(3) # wait for system to write processed file
		send_processed_image(image_name)
else:
	print('No new images to send')
