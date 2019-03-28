# Using an official python runtime image as parent image.
FROM python:3.7-slim

# Setting working directory as movie-details
WORKDIR /movie-details

# copying the current directory contents to movie-details directory in container
COPY . /movies

# Installing any needed dependencies specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 8090 available to outside world.
EXPOSE 8090


# Run movie-details.py when the container launches
CMD ["python", "movie-details.py"]
