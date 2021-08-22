FROM python:3.8.1

ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt ./
#RUN apk add --update --no-cache postgresql-client jpeg-dev
#RUN apk add --update --no-cache --virtual .tmp-build-deps \
#    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
#RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
#RUN apk del .tmp-build-deps
COPY ./app /app


