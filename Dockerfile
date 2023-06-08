FROM prefecthq/prefect:2.10.10-python3.10

COPY docker-requirements.txt .

RUN pip install -r docker-requirements.txt --trusted-host pypi.python.org --no-cache-dir

COPY main.py /opt/prefect/flows
COPY detect_new_raw_image.py opt/prefect/flows