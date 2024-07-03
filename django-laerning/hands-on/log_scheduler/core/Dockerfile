FROM python:3.10-alpine

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip \
    && pip3 install --no-cache --upgrade pip setuptools \
    && pip install -r requirements.txt \
    # Logging 디렉토리 생성
    && mkdir -p /app/logs \
    && chmod -R 775 /app/logs 

EXPOSE 8000
