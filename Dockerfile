FROM nvidia/cuda:12.8.1-cudnn-devel-ubuntu22.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y
RUN apt-get install ffmpeg -y
RUN apt-get install curl -y


RUN mkdir /workspace
WORKDIR /workspace
RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.local/bin:${PATH}"
COPY . .
RUN uv sync
CMD ["uv", "run", "./quickcodec/bench/qc_cuda_benchmark.py", "./quickcodec/assets/movie1080p.BluRay.1hour.x264_2_448x448.mp4"]