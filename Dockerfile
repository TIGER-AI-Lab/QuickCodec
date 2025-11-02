FROM nvidia/cuda:13.0.1-cudnn-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y
RUN apt-get install ffmpeg -y


RUN mkdir /workspace
WORKDIR /workspace
RUN curl -LsSf https://astral.sh/uv/install.sh | sh