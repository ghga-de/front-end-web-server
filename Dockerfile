FROM python:alpine3.13
COPY ./front-end-web-server /front-end-web-server
COPY ./requirements.txt /front-end-web-server/requirements.txt
COPY ./run_web_server.sh /run_web_server
WORKDIR /front-end-web-server
EXPOSE 4000
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install -r requirements.txt
RUN chmod +x /run_web_server
CMD exec /run_web_server
