import logging
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

def send_processed_image(file_name:str, channel_id="C058V9D6PE0"):
	# instantiate the webclient use a bot token
	client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
	logger = logging.getLogger(__name__)
	try:
    		# call method to upload files to channel
    		result = client.files_upload(
        		channels=channel_id,
        		initial_comment="New photo available for {}".format(file_name),
        		file=file_name,
    		)
    		# Log the result
    		logger.info(result)
	except SlackApiError as e:
    		logger.error("Error uploading file: {}".format(e))
