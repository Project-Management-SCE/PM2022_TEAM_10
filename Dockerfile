
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG 0
COPY . /app
WORKDIR /app
EXPOSE 8000

RUN python -m pip install -r requirements.txt

WORKDIR /app/ProjectManagement
ENTRYPOINT ["sh","ep.sh"]