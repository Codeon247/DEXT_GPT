FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Expose the port on which the server will run
EXPOSE 8888

# Run migrations.
RUN python manage.py makemigrations src
RUN python manage.py migrate

# Run the server when the container starts
ENTRYPOINT ["python"]
CMD [ "manage.py", "runserver" , "0.0.0.0:8888"]