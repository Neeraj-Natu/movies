# Using an official python runtime image as parent image.
FROM python:3.7-slim

# Setting working directory as grpc-details
WORKDIR /grpc-details

# copying the current directory contents to grpc-details directory in container
COPY . /grpc-details

# Installing any needed dependencies specified in requirements.txt
RUN pip install -r ./requirements.txt

# Make port 80 available to outside world.
EXPOSE 80


# Run movie-details.py when the container launches
CMD ["python", "grpc-details.py"]
