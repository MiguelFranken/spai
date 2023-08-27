# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the docker container
WORKDIR /app

# Copy only the requirements file and install dependencies
# Docker will reuse the cached layer and won't reinstall the
# dependencies every time you change your source code.
COPY requirements.txt /app/
RUN pip install --upgrade pip &&\
    pip install -r requirements.txt

COPY src/ /app/
COPY entrypoint.sh /app/

CMD ["./entrypoint.sh"]

