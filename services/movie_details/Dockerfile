# Using an official python runtime image as parent image.
FROM python:3.7-slim

# Setting working directory as movie_details
WORKDIR /movie_details

# copying the current directory contents to movie_details directory in container
COPY . /movies_details

# Installing any needed dependencies specified in requirements.txt
RUN pip install Flask
RUN pip install pandas

# Make port 9001 available to outside world.
EXPOSE 9001


# Run movie-details.py when the container launches
CMD ["python", "movie-details.py"]
