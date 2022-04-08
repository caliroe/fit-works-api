
install: 
	pip install -r requirements.txt	


run-dev:
	uvicorn main:app --reload --port 8080


build-run:
	sudo docker build -t works-api && \
	sudo docker run --name works-api -p 8080:8080
