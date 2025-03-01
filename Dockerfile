#base image
FROM artemisfowl004/vid-compress
RUN apt update && apt install -y ffmpeg
COPY requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["bash","start.sh"]
