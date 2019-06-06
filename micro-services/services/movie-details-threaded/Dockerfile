# Using an official python runtime image as parent image.
FROM python:3.7-slim

# Setting working directory as threaded-details
WORKDIR /threaded-details

# copying the current directory contents to threaded-details directory in container
COPY . /threaded-details

# Installing any needed dependencies specified in requirements.txt
RUN pip install -r ./requirements.txt

# Make port 80 available to outside world.
EXPOSE 80


# Run movie-details.py when the container launches
CMD ["python", "threaded-details.py"]
