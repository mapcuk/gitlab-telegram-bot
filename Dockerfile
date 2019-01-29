FROM python:3.6-alpine

# Example: docker build -t docker-registry-default.prod.trmpln.ru/dev/gitlab-telegram-bot:0.1

RUN mkdir -p /opt/project
COPY requirements.txt /opt/project/requirements.txt
RUN pip install -r /opt/project/requirements.txt
COPY . /opt/project

CMD ["python3", "/opt/project/app.py"]
