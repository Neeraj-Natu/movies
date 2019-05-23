# Using an official python runtime image as parent image.
FROM python:3.7-slim

# Setting working directory as revenues
WORKDIR /revenues

# copying the current directory contents to revenues directory in container
COPY . /revenues

# Installing any needed dependencies specified in requirements.txt
RUN pip install -r ./requirements.txt

# Make port 80 available to outside world.
EXPOSE 80


# Run revenues.py when the container launches
CMD ["python", "revenues.py"]
