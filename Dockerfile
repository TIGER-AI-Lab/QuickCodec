FROM nvidia/cuda:13.0.1-cudnn-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y
RUN apt-get install ffmpeg -y
RUN apt-get install curl -y


RUN mkdir /workspace
WORKDIR /workspace
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
COPY debug.sh .
COPY pyproject.toml .
RUN curl -L -o /tmp/video.mp4 https://videos.pexels.com/video-files/854132/854132-sd_640_360_25fps.mp4
