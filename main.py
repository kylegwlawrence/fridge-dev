from prefect import flow, task
import cv2
import logging
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def get_file_names(directory:str) -> set:
	"""Loop over files in the directory and return a set of file names. Ignores sub-directories.
	Returns a set of image names with extension"""
	image_names=[]
	for entry in os.scandir(directory):
		if entry.is_file():
			image_name=entry.name
			image_names.append(image_name)
	return set(image_names)

@task(name='Determine unprocessed raw images')
def compare_file_names(raw_directory:str='images/raw', processed_directory:str='images/processed') -> list:
	"""Get a set of raw imagenames and a set of processed image names, compare the sets, and return a list of raw image names that have not been processed. If all raw images have a match in the processed images folder, return an empty set."""
	raw_names = get_file_names(raw_directory)
	processed_names = get_file_names(processed_directory)
	# compare equality between the two sets
	raw_images_not_processed = raw_names.difference(processed_names)
	return list(raw_images_not_processed)

@task(name='Process raw images')
def transform_raw_image(image_name:str, width=150, height=150 ) -> None:
    """Take an image name from the raw image folder,read it in and comvert to greyscale, resize it, and write to processed folder as a JPEG file."""
    # possibly use cvtColor to transform from one color space to another instead of using IMREAD_GRAYSCALE
    img = cv2.imread('images/raw/'+image_name, cv2.IMREAD_GRAYSCALE)
    resized = cv2.resize(img, (width, height), interpolation = cv2.INTER_AREA)
    cv2.imwrite('images/processed/'+image_name, resized, [int(cv2.IMWRITE_JPEG_QUALITY), 95])

@task(name='Send processed images to Slack')
def send_processed_image(image_name:str, channel_id:str="C058V9D6PE0") -> None:
	"""Take a processed image name and upload it to a given channel_id in your Slack workspace."""
	logger = logging.getLogger(__name__)
	image_path = 'images/processed/{}'.format(image_name)
    # instantiate the webclient with a bot token
	try:
		client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
	except SlackApiError as e:
		logger.error("Error creating client: {}".format(e))
	try:
		# call method to upload files to channel
		result = client.files_upload_v2(
			channel=channel_id,
			initial_comment="Processed photo available for {}".format(image_name),
			file=image_path,
			request_file_info=False
		)
		logger.info(result)
	except SlackApiError as e:
		logger.error("Error uploading file: {}".format(e))
		# send failure message to slack channel
		try:
			result = client.chat_postMessage(
    			channel=channel_id,
				text="File upload to Slack failed."
			)
			logger.info(result)
		except SlackApiError as e:
			logger.error("Error sending failure message: {}".format(e))

@flow(name='Raw images: find, process, and notify', log_prints=True)
def main():
	# get a list of new images in raw that have not been processed. 
	new_raw_images=compare_file_names()
	# transform image(s) and send the image to Slack.
	if len(new_raw_images)!=0:
		for image_name in new_raw_images:
			transform_raw_image(image_name, wait_for=[compare_file_names])
			send_processed_image(image_name, wait_for=[transform_raw_image])
	else:
		print('No new images to send')

if __name__ == '__main__':
	main()