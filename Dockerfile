FROM postgres:latest

RUN mkdir -p /home/app

COPY . /home/app

EXPOSE 5432

CMD ["postgres", "/home/app/main.py"]