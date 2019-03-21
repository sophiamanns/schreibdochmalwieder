FROM python:3
ENV PYTHONUNBUFFERED 1
RUN apt-get update && \
    apt-get install -y nginx && \
    mkdir -p /srv/code/schreibdochmalwieder && \
    mkdir /srv/deploy

COPY deploy/requirements.txt /srv/deploy
COPY requirements.txt /srv/deploy/requirements-src.txt

RUN pip install -r /srv/deploy/requirements.txt \
		-r /srv/deploy/requirements-src.txt

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY deploy/nginx.conf /etc/nginx/site-available/default

ADD deploy /srv/deploy

ADD schreibdochmalwieder /srv/code/schreibdochmalwieder
WORKDIR /srv/code

EXPOSE 8000
CMD /srv/deploy/start.sh
