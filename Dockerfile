FROM python:3.6

#RUN apt update && apt install ffmpeg -y

WORKDIR /workspace

RUN pip install git+https://github.com/JeanMaximilienCadic/gnutools-python --no-cache-dir
