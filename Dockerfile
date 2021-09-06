FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/youngjuj/steffie-s.git

WORKDIR /home/with_teacher/

RUN echo "SECRET_KEY=django-insecure-wyq#+8ce@$23$141(#=qjx(vwr*(_a&30^azgxzuf&!=%v))d2" > .env

RUN pip install -r requirements.txt

RUN python manage.py migrate

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
