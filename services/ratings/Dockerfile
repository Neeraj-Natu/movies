# Using an official python runtime image as parent image.
FROM python:3.7-slim

# Setting working directory as ratings
WORKDIR /ratings

# copying the current directory contents to ratings directory in container
COPY . /ratings

# Installing any needed dependencies specified in requirements.txt
RUN pip install Flask
RUN pip install pandas

# Make port 9003 available to outside world.
EXPOSE 9003


# Run ratings.py when the container launches
CMD ["python", "ratings.py"]
