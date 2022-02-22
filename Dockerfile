FROM python:3.9.10-alpine

COPY ./application /application
WORKDIR /application

RUN pip install -r requirements.txt
			
CMD ["tail", "-f", "/dev/null"]