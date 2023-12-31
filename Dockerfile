FROM python:3.10.0

RUN mkdir /src

COPY requirements.txt /src

RUN python -m pip install --upgrade pip

RUN pip3 install -r /src/requirements.txt --no-cache-dir

COPY ./ /src/

WORKDIR /src
