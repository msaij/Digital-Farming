FROM python

ENV DIRNAME=Digital-Farming
ENV PROJECT=final_year_project

WORKDIR $DIRNAME
COPY . .

RUN pip3 install -r requirements.txt

WORKDIR ${PROJECT}
RUN python manage.py makemigrations