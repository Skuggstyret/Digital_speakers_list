FROM python:3

# Entry attach directory
WORKDIR /source

# Install depends
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN pip install flask-cors --upgrade

# Starts server
# ENTRYPOINT ["python3", "server.py"]
CMD [ "flask", "run", "--host=0.0.0.0"]

