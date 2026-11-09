FROM python:3.11-alpine
WORKDIR /app
COPY . .
RUN pip install psycopg2-binary
EXPOSE 3000
CMD ["python", "index.py"]