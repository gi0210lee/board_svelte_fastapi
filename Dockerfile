FROM python:alpine

RUN mkdir /back
WORKDIR /back
ADD . /back

RUN apk upgrade && apk add bash
RUN apk add postgresql-client
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]