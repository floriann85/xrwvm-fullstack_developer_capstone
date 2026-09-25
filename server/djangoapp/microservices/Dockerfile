FROM python:3.9.18-slim-bookworm


WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ENV FLASK_APP=sentiment_analyzer.py
ENV FLASK_RUN_PORT=5000
RUN ls
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
