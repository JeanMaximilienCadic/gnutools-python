docker rmi -f jcadic/gnutools-python:latest
docker build . -t jcadic/gnutools-python
docker run --rm -it jcadic/gnutools-python bash