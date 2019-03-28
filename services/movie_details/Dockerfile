# Using an official python runtime image as parent image.
FROM python:3.7-slim

# Setting working directory as movies
WORKDIR /movies

# copying the current directory contents to movies directory in container
COPY . /movies

# Installing any needed dependencies specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to outside world.
EXPOSE 5000


# Run movies.py when the container launches
CMD ["python", "movies.py"]
