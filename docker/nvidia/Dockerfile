# BUILDER
FROM nvidia/cuda:12.6.3-base-ubuntu22.04
WORKDIR /builder
ARG TORCH_CUDA_ARCH_LIST=7.5
ARG BUILD_EXTENSIONS=""
ARG APP_UID=6972
ARG APP_GID=6972
ARG HOST_PORT=7860
ARG CONTAINER_PORT=7860
ARG HOST_API_PORT=5000
ARG CONTAINER_API_PORT=5000
ARG APP_RUNTIME_GID=6972
ARG TRANSFORMERS_CACHE=/home/app/text-generation-webui/cache/
ARG HF_HOME=/home/app/text-generation-webui/cache/

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked,rw \
    apt update && apt install -y \
    python3-pip \
    git vim build-essential python3-dev pip bash curl && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /home/app/
RUN git clone https://github.com/SquirrelMom/text-generation-webui.git
# https://github.com/oobabooga/text-generation-webui.git 
WORKDIR /home/app/text-generation-webui
RUN GPU_CHOICE=A USE_CUDA118=FALSE LAUNCH_AFTER_INSTALL=FALSE INSTALL_EXTENSIONS=TRUE ./start_linux.sh --verbose
COPY ../../CMD_FLAGS.txt /home/app/text-generation-webui/
EXPOSE ${CONTAINER_PORT:-7860} ${CONTAINER_API_PORT:-5000} ${CONTAINER_API_STREAM_PORT:-5005}
WORKDIR /home/app/text-generation-webui
# set umask to ensure group read / write at runtime
CMD umask 0002 && export HOME=/home/app/text-generation-webui && ./start_linux.sh --listen
