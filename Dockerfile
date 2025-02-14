FROM python:3.11-slim
RUN pip install django==5.1.5
RUN pip install djangorestframework
RUN apt-get update && apt-get install -y \
    libjpeg-dev \
    libpng-dev \
    zlib1g-dev \
    libtiff-dev \
    libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir django-filter
RUN pip install --no-cache-dir djangorestframework-simplejwt
RUN pip install --no-cache-dir Pillow
WORKDIR /app
COPY . /app

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]