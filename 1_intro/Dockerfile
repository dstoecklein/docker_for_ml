# base image
FROM ubuntu:18.04 
# move the application to the container image
COPY . /docker_for_ml/1_intro
# set the working directory
WORKDIR /docker_for_ml/1_intro
# if error "pip not found error occurs"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
# install requirements
RUN pip install -r requirements.txt
# expose port (default is 5000)
EXPOSE 5000
# run command
CMD python ./index.py