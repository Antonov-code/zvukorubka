FROM python:3.14-rc-alpine3.20
RUN pip install pip install django==5.1.5
RUN pip install djangorestframework
RUN pip install django-filter
RUN pip install djangorestframework-simplejwt
WORKDIR /app
COPY . /app
ENTRYPOINT ["python3", "manage.py"]