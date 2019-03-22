# schreibdochmalwieder

An Application to design letter paper. 

<p align="center">
  <img width="100%" src="schreibdochmalwieder/static/schreibdochmalwieder.svg">
</p>


This application provides a small server which lets you design letter paper
with a subset of the images of the _Graphiksammlung des Eugen Diederichs Verlags_
dataset. 

This project is meant to be entered into the competition of [Coding Da Vinci Ost 2018](https://codingdavinci.de/events/ost).

## Prequisites

This software is developed with and for Python3.6.

## Installation

Create a new virtual environment

```zsh
$ mkvirtualenv schreibdochmalwieder -p /usr/bin/python3
```

Install the dependencies

```zsh
$ pip install -r requirements.txt
```

## Usage

Run the server.

```zsh
$ flask run
```

## Yolo Deployment

The server can easily be installed as a systemd service. 
For a small service like that the web server provided with flask should be sufficient. 
A more advanced deployment would be with an application server like gunicorn
and a webserver/reverse proxy like caddy.

For the "easy" deployment, create a file e.g. named "schreibdochmalwieder.sh" 
in your homedir with the following contents:

```zsh
#!/usr/bin/zsh

# CONSTANTS
HOME=<YOUR HOMEDIR HERE>
VENVNAME=schreibdochmalwieder
VENVDIR=${HOME}/.virtualenvs/${VENVNAME}
APPDIR=${HOME}/<PATH TO THE APPLICATION HERE>
APPNAME=app.py

# ACTIVATE THE VIRTUALENV
source ${VENVDIR}/bin/activate

# START THE APPLICATION
cd $APPDIR
flask run
```
If you did that, make it executable.

```zsh
$ chmod 755 schreibdochmalwieder.sh
```

Then create the systemd-service file

```zsh
$ touch /etc/systemd/system/schreibdochmalwieder.service
```

with the following contents:

```zsh
[Unit]
Description=schreibdochmalwieder
After=network.target

[Service]
Type=simple
User=<YOUR USERNAME HERE!>
ExecStart=/home/olf/schreibdochmalwieder.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Make it executable. Run it and make it run even if the server restarts.

```zsh
$ systemctl daemon-reload
$ systemctl start schreibdochmalwieder.service
$ systemctl enable schreibdochmalwieder.service
```

You should now be able to reach the server at https://localhost:5000


## License

* GNU General Public License v3

## Collaborators

* Annika Schröer
* Sophia Manns
* Florian Rämisch
