FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

ENV PORT="81"\
    PYTHONUNBUFFERED=TRUE


COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt
RUN apt update && apt install -y swig

COPY . /app

RUN cd /app && pytest app/tests -vs