# Using an official python runtime image as parent image.
FROM python:3.7-slim

# Setting working directory as movies
WORKDIR /movies

# copying the current directory contents to movies directory in container
COPY . /movies

# Installing any needed dependencies specified in requirements.txt
RUN pip install Flask
RUN pip install pandas

# Make port 9002 available to outside world.
EXPOSE 9002


# Run movies.py when the container launches
CMD ["python", "movies.py"]
