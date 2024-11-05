FROM python:3.10.11


SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

RUN apt update && apt -qy install gcc libjpeg-dev libxslt-dev \
    libpq-dev gettext cron openssh-client flake8 locales vim git

RUN useradd -rms /bin/bash petapp && chmod 777 /opt /run

WORKDIR /petapp

RUN mkdir /petapp/static && mkdir /petapp/media && chown -R petapp:petapp /petapp && chmod 755 /petapp

COPY --chown=petapp:petapp . .

RUN pip install -r requirements.txt

USER petapp

CMD ["python manage.py runserver"]