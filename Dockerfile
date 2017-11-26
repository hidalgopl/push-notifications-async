FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /home/application && \
     mkdir /home/application/socks && \
     mkdir /home/application/logs && \
     mkdir /home/application/media
RUN apt-get update && \
     apt-get upgrade -y && \
     apt-get install -y apt-utils
RUN chown -R www-data:www-data /home/application
ADD . /home/application/app/
WORKDIR /home/application/app/
RUN apt-get install -y libproj-dev
RUN pip3.6 install -r requirements.txt
RUN pip3.6 install -r requirements-ci.txt
