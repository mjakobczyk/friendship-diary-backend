.PHONY: build version dockerize publish

version=develop
imagename=friendship-diary-backend

build:
	python3 app.py

version:
	@echo $(imagename) $(version)

dockerize:
	docker build -t $(imagename):$(version) . -f Dockerfile

publish: dockerize
	docker login
	docker push $(imagename):$(version)
