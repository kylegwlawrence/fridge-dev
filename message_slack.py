import logging
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def send_processed_image(image_name:str, channel_id:str="C058V9D6PE0") -> None:
	"""Take a processed image name and upload it to a given channel_id in your Slack workspace."""
    logger = logging.getLogger(__name__)
	image_path = 'images/processed/{}'.format(image_name)
    # instantiate the webclient use a bot token
	client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
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

def send_message(text:str, channel_id:str) -> None:
	"""Send a message with custom text to slack channel"""