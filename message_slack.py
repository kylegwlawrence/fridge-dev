import logging
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def send_processed_image(image_name:str, channel_id:str="C058V9D6PE0") -> None:
	"""Send a file to a Slack channel using file_name.type and not including the path"""
	# instantiate the webclient use a bot token
	image_path = 'images/processed/{}'.format(image_name)
	client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
	logger = logging.getLogger(__name__)
	try:
    		# call method to upload files to channel
    		result = client.files_upload(
        		channels=channel_id,
        		initial_comment="Processed photo available for {}".format(image_name),
        		file=image_path,
    		)
    		# Log the result
    		logger.info(result)
	except SlackApiError as e:
    		logger.error("Error uploading file: {}".format(e))

def send_message(text:str, channel_id:str) -> None:
	"""Send a message with custom text to slack channel"""
