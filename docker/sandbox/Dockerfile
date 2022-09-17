FROM cadic/gnutools:vanilla

WORKDIR /workspace

COPY requirements.txt /workspace
COPY dist/*.whl /workspace/

RUN pip install -r requirements.txt && rm requirements.txt
RUN pip install *.whl && rm *.whl

COPY Makefile /workspace

RUN make tests

CMD ["/bin/bash"]