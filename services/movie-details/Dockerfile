# Using an official python runtime image as parent image.
FROM python:3.7-slim

# Setting working directory as movie-details
WORKDIR /details

# copying the current directory contents to movie-details directory in container
COPY . /details

# Installing any needed dependencies specified in requirements.txt
RUN pip install -r ./requirements.txt

# Make port 9001 available to outside world.
EXPOSE 9001


# Run movie-details.py when the container launches
CMD ["python", "movie-details.py"]
