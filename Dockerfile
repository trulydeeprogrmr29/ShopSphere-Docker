FROM python:3.12-slim
RUN pip install --no-cache-dir flask==3.0.3 requests==2.32.3
WORKDIR /app
ARG SERVICE
COPY ${SERVICE}.py service.py
USER nobody
CMD ["python", "service.py"]
