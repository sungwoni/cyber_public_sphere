FROM python:3.9.0

WORKDIR /home/

RUN echo "testing1234567"

RUN git clone https://www.github.com/sungwoni/cyber_public_sphere.git

WORKDIR /home/cyber_public_sphere/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=sungwon_poll.settings.deploy && python manage.py migrate --settings=sungwon_poll.settings.deploy && gunicorn sungwon_poll.wsgi --env DJANGO_SETTINGS_MODULE=sungwon_poll.settings.deploy --bind 0.0.0.0:8000"]