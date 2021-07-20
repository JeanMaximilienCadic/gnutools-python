nano build_wheel.sh
sh build_wheel.sh
mv *.whl python3.8/
docker build python3.8 -t jcadic/gnutools-python:3.8-2.0a1
docker run -it jcadic/gnutools-python:3.8-2.0a1 bash
