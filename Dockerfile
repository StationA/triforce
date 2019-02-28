FROM registry.stationa.io/stationa/base:latest

ADD . /triforce
WORKDIR /triforce
RUN pip3 install -r requirements.txt
RUN pip3 install .

ENTRYPOINT ["/usr/local/bin/triforce"]
