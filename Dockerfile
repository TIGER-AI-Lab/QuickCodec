FROM nvidia/cuda:13.0.1-cudnn-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y
RUN apt-get install ffmpeg -y
RUN apt-get install curl -y


RUN mkdir /workspace
WORKDIR /workspace
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
RUN source $HOME/.local/bin/env
COPY debug.sh .
COPY pyproject.toml .
RUN uv sync
RUN curl -L -o /workspace/video.mp4 https://videos.pexels.com/video-files/854132/854132-sd_640_360_25fps.mp4
COPY assets/movie1080p.BluRay.1hour.x264_2_448x448.mp4 .