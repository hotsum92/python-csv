diamonds.csv:
	curl -O https://raw.githubusercontent.com/PacktPublishing/Hands-On-Predictive-Analytics-with-Python/master/Data/diamonds.csv

build:
	docker build -t python-csv .

run:
	docker run -it --rm --gpus all -u $(id -u):$(id -g) -v ./:/usr/src python-csv bash
