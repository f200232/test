FROM python:3.6
MAINTAINER Absar Ali"f200232@cfd.nu.edu.pk"
COPY app.py test.py /app/
WORKDIR /app
RUN pip install flask pytest flake8 
CMD ["python", "app.py"]
