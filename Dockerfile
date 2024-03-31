# FROM homebrew/ubuntu22.04
# FROM ubuntu_python

# FROM eclipse/ubuntu_python

# FROM ubuntu:20.04

FROM python

# for flask web server
EXPOSE 8000

# COPY requirements.txt .

# add files
ADD . /app

# set working directory
WORKDIR /app

# RUN 

# install required libraries
RUN pip install -r requirements.txt

# RUN os.open("top")

# CMD powermetrics --samplers smc -n 1 |grep -i "CPU die temperature"

# CMD gunicorn -w 1 -b :7878 app:app

# CMD python app.py
CMD python app.py

# CMD top

#  docker run -it --device /dev/dri  
