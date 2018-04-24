FROM python:3.6.5-alpine

LABEL maintainer="Frank van Gemeren <frank@frankvangemeren.com>"

ADD blackpython.py /blackpython.py

ENTRYPOINT ["python3", "/blackpython.py"]
