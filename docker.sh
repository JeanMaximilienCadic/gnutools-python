docker rmi -f jcadic/gnutools-python
docker build . -t jcadic/gnutools-python
docker run --rm -it jcadic/gnutools-python bash
