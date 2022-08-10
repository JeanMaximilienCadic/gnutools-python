FROM python:3.9

WORKDIR /workspace

COPY requirements.txt /workspace
COPY dist/*.whl /workspace/

RUN pip install -r requirements.txt && rm requirements.txt
RUN pip install *.whl && rm *.whl

CMD ["/bin/bash"]