FROM python:3.12

COPY ./app /app

WORKDIR /app

RUN pip install -r requirements.txt
RUN mkdir -p /model
COPY model /model

EXPOSE 9001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9001"]