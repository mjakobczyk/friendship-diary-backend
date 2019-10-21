.PHONY: run version dockerize publish

version=develop
imagename=friendship-diary-backend

run:
	python3 startup.py

version:
	@echo $(imagename) $(version)

dockerize:
	docker build -t $(imagename):$(version) . -f Dockerfile

publish: dockerize
	docker login
	docker push $(imagename):$(version)
