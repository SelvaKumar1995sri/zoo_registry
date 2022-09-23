FROM python:alpine3.15
ADD . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements.txt
CMD [ "python3", "src/zoo_app.py" ]