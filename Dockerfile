FROM pytorch/pytorch:1.10.0-cuda11.3-cudnn8-devel

WORKDIR /usr/src/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
