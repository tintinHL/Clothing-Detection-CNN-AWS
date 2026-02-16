FROM continuumio/miniconda3:latest
WORKDIR /app
COPY . /app

RUN apt update && apt install awscli -y && apt-get upgrade && pip install --upgrade pip && pip install --upgrade pip && apt-get install ffmpeg libsm6 libxext6 -y && pip install -r requirements.txt && apt-get clean && apt-get autoremove -y && torch torchvision  && torch-model-archiver --version

CMD ["python", "app.py"]