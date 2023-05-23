import logging
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def send_processed_image(file_name:str, channel_id:str) -> None:
    """Send a file to a Slack channel using file_name.type and not including the path"""
	# instantiate the webclient use a bot token
    file_path = '/images/processed/{}'.format(file_name)
	client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
	logger = logging.getLogger(__name__)
	try:
    		# call method to upload files to channel
    		result = client.files_upload(
        		channels=channel_id,
        		initial_comment="Processed photo available for {}".format(file_name),
        		file=file_path,
    		)
    		# Log the result
    		logger.info(result)
	except SlackApiError as e:
    		logger.error("Error uploading file: {}".format(e))
