# After building, run with "docker run -p 8000:8000 [docker]"
# in order to access the server port

FROM python:3.6

ENV PYTHONUNBUFFERED 1
RUN mkdir /bugoff
WORKDIR /bugoff
COPY requirements.txt /bugoff/
RUN pip install -r requirements.txt
COPY . /bugoff

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
