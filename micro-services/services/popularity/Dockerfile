# Using an official python runtime image as parent image.
FROM python:3.7-slim

# Setting working directory as popularity
WORKDIR /popularity

# copying the current directory contents to popularity directory in container
COPY . /popularity

# Installing any needed dependencies specified in requirements.txt
RUN pip install -r ./requirements.txt

# Make port 80 available to outside world.
EXPOSE 80


# Run popularity.py when the container launches
CMD ["python", "popularity.py"]
