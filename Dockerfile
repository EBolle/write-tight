FROM python:3.9-slim

RUN useradd --create-home --shell /bin/bash user

WORKDIR /home/user 

ENV PATH="${PATH}:/home/user/.local/bin"

COPY ./writetight ./writetight

COPY requirements.txt setup.py main.py ./

USER user

RUN pip install --upgrade pip

RUN pip install --user pip setuptools wheel

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=main.py

RUN ["python3", "-m", "spacy", "download", "en_core_web_sm"]

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]