FROM python:3.6-slim AS pytorch_base
RUN pip3 install http://download.pytorch.org/whl/cpu/torch-0.4.0-cp36-cp36m-linux_x86_64.whl 


FROM pytorch_base
ADD . /pytorch-runtime
WORKDIR /pytorch-runtime
RUN pip install .
VOLUME [ "/model" ]
ENTRYPOINT [ "serve-pytorch" ] 