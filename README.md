# schreibdochmalwieder

An Application to create custom letter paper from digitized herbarium data of
[Gleimhaus](https://www.gleimhaus.de) and graphical artworks of *Eugen Diederichs Verlag* at [ThULB](https://www.thulb.uni-jena.de/).
The authors of this software provide access to an instance of this software at [schreibdochmalwieder.trollofix.com](https://schreibdochmalwieder.trollofix.com).

<p align="center">
  <img width="100%" src="schreibdochmalwieder/static/schreibdochmalwieder.svg">
</p>

This project was created during, and entered into the compition of the 
culture hackathon [Coding Da Vinci Ost 2018](https://codingdavinci.de/events/ost) from April - June 2018 
at the Leipzig University Library. 

## Prequisites

This software is developed with and for Python3.6.

The recommended deployment method is via docker and docker-compose. 
Please refer to the [official docker compose documentation](https://docs.docker.com/compose/install/) for more 
information on how to setup *docker compose* on your machine. 

## Prerequisites

You need *git* to checkout the latest version of *schreibdochmalwieder* from github and *Python3* to generate
the assets.

## Deployment

Clone the repository using git.

```zsh
$ git clone https://github.com/sophiamanns/schreibdochmalwieder
```

Install the requirements

```zsh
$ pip install -r requirements.txt
```

Build the assets
```zsh 
$ make generate-letterpaper
```

Build and run the container:

```zsh
$ docker-compose up -d
```

Alternatively you can use the method from *Makefile* to perform all of the above steps, except the cloning

```zsh
$ make all
```

## Development

You are welcome to this project with your contribution, either by adding additional content, creating new features
or fixing bugs. 

## License

* GNU General Public License v3

## Collaborators

* Annika Schröer
* Sophia Manns
* Florian Rämisch
