all: delete lazyBuild

lazyBuild:
	docker build -t lr4image .
	docker run -it --name lr4container  -p 80:8000 lr4image

delete:
	# docker images -a
	# docker rmi lrx  #image
	# docker ps -a  #container

	docker stop $(shell docker ps -a -q)
	docker rm $(shell docker ps -a -q)

	docker rmi $(shell docker images -a -q)

# rm  ~/.docker/config.json 
