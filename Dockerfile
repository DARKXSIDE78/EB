FROM DARKXSIDE78/EB
RUN apt update && apt install -y ffmpeg
RUN pip install Pillow psutil hachoir tgcrypto pyrofork motor aiofiles dnspython ffmpeg asyncio flask
CMD ["python", "-m bot"]
