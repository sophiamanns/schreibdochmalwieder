.DEFAULT_GOAL := help

.PHONY: help
help:	## Show this help
	@grep -E '^[\.a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY:
run:	## Run the development Server
	cd schreibdochmalwieder && flask run

.PHONY: lint
lint:	## Lint the code
	flake8 schreibdochmalwieder

.PHONY: generate-letterpaper
generate-letterpaper: ## Has to be run initially to generate the letterpaper from the images
	python schreibdochmalwieder/generate_letterpaper.py
