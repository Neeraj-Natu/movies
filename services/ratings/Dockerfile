# Using an official python runtime image as parent image.
FROM python:3.7-slim

# Setting working directory as ratings
WORKDIR /ratings

# copying the current directory contents to ratings directory in container
COPY . /ratings

# Installing any needed dependencies specified in requirements.txt
RUN pip install -r ./requirements.txt

# Make port 80 available to outside world.
EXPOSE 80


# Run ratings.py when the container launches
CMD ["python", "ratings.py"]
