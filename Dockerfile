FROM python:3.8  #This is instruction in FROM tells that dockerfile is fetching python 3.8 from Dockerhub and keep it inside package and run on containers

COPY . /app  #This tell that entire local code (.) will be copied to app folder in the container

WORKDIR /app #This app working directory we are creating in the container

RUN pip install -r requirements.txt  #This tells which command to run

CMD ["python", "app.py"]  #This tells that which command to needed to run app.py (python app.py)