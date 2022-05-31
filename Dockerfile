FROM python:3.9-alpine
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBUG 0
COPY . /app
WORKDIR /app
EXPOSE 8000

RUN python -m pip install -r requirements.txt

RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

WORKDIR /app/ProjectManagement
ENTRYPOINT ["sh","ep.sh"]