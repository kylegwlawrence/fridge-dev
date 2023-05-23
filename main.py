from detect_new_raw_image import compare_file_names
from transform_image import transform_image
from message_slack import send_processed_image

# determine if new images exist in raw. Returns set of raw images not processed if any. 
new_raw_images=list(compare_file_names('images/raw','images/processed'))

# transform image
for image_name in new_raw_images:
	transform_image(image_name)
	send_processed_image(image_name, channel_id="C058V9D6PE0")
