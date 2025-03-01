#base image
FROM artemisfowl004/vid-compress
RUN apt update && apt install -y ffmpeg
RUN pip install -r requirements.txt
CMD ["python3","-m main"]
