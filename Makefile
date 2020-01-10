.PHONY: run version dockerize publish

user=user
version=develop
imagename=friendship-diary-backend-python

run:
	python3 startup.py

version:
	@echo $(imagename) $(version)

dockerize:
	docker build -t $(user)/$(imagename):$(version) . -f Dockerfile

publish: dockerize
	docker login
	docker push $(user)/$(imagename):$(version)
