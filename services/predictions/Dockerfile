# Using an official python runtime image as parent image.
FROM python:3.7-slim

# Setting working directory as predictions
WORKDIR /predictions

# copying the current directory contents to predictions directory in container
COPY . /predictions

# Installing any needed dependencies specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 5000 available to outside world.
EXPOSE 5000


# Run predictions.py when the container launches
CMD ["python", "predictions.py"]
