import logging
import os
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
logger = logging.getLogger(__name__)
# The name of the file you're going to upload
file_name = "./images/processed/Fridge_2.jpg"
# ID of channel that you want to upload file to
channel_id = "C058V9D6PE0"

try:
    # Call the files.upload method using the WebClient
    # Uploading files requires the `files:write` scope
    result = client.files_upload(
        channels=channel_id,
        initial_comment="New photo available for {}".format(file_name),
        file=file_name,
    )
    # Log the result
    logger.info(result)

except SlackApiError as e:
    logger.error("Error uploading file: {}".format(e))
