# Using an official python runtime image as parent image.
FROM python:3.7-slim

# Setting working directory as predictions
WORKDIR /predictions

# copying the current directory contents to predictions directory in container
COPY . /predictions

# Installing any needed dependencies specified in requirements.txt
RUN pip install -r ./requirements.txt

# Make port 80 available to outside world.
EXPOSE 80


# Run predictions.py when the container launches
CMD ["python", "predictions.py"]
