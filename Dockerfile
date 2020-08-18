FROM ubuntu:18.04

MAINTAINER EtricKombat 

RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
RUN apt-get update -y
RUN apt-get install -qqy x11-apps -y
COPY . /app
WORKDIR /app

RUN pip3 install pygame
ENTRYPOINT ["python"]
CMD ["main.py"]

#sudo docker run -e DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix --user="$(id --user):$(id --group)" nirupamjm/njmaxc
