FROM python:3.7-slim

# for flask web server
EXPOSE 8000

# add files
ADD . /app

# set working directory
WORKDIR /app

# install required libraries
RUN pip install -r requirements.txt

# CMD powermetrics --samplers smc |grep -i "CPU die temperature"

# CMD gunicorn -w 1 -b :7878 app:app

CMD python app.py

#  docker run -it --device /dev/dri  
