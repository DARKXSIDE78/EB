FROM python:3.10-slim
RUN apt update && apt install -y ffmpeg
WORKDIR /app
COPY . /app/
RUN pip install Pillow psutil hachoir tgcrypto pyrofork motor aiofiles dnspython ffmpeg asyncio flask
CMD ["python", "-m bot"]
