#!/bin/sh
uwsgi --ini /srv/deploy/uwsgi.ini &
exec /usr/sbin/nginx
