# Fridge project: computer vision to inventorize your fridge

This project is run on a Raspberry Pi.

The project's goal is to automate inventory for your personal fridge in order to reduce waste and always have an up to date list of ingredients.

Creators: Kyle Lawrence and Aspen James

## Files
- transform_image.py: reads in image, rescales and changes colour scale to greyscale and writes to processed folder
- message_slack.py: uses local env variable for Slack Bot to send an image to channel #new-photo-messsage given a path to image
- start_slack_with_bolt.py: uses local env variables for Slack App and Slack Bot to use SocketMode to generate a connection

