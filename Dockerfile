FROM python:3-slim

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y gcc g++ libpq-dev libgmt-dev gmt

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

RUN pip install -r requirements.txt 

# Timeout needed to wait for the app to start
CMD ["gunicorn", "-w", "6", "-b", "0.0.0.0:8050", "--timeout", "2400", "app:server"]
