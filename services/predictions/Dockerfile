# Using an official python runtime image as parent image.
FROM python:3.7-slim

# Setting working directory as predictions
WORKDIR /predictions

# copying the current directory contents to predictions directory in container
COPY . /predictions

# Installing any needed dependencies specified in requirements.txt
RUN pip install Flask
RUN pip install pandas

# Make port 9004 available to outside world.
EXPOSE 9004


# Run predictions.py when the container launches
CMD ["python", "predictions.py"]
