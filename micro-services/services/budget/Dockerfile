# Using an official python runtime image as parent image.
FROM python:3.7-slim

# Setting working directory as budget
WORKDIR /budget

# copying the current directory contents to budget directory in container
COPY . /budget

# Installing any needed dependencies specified in requirements.txt
RUN pip install -r ./requirements.txt

# Make port 80 available to outside world.
EXPOSE 80


# Run budget.py when the container launches
CMD ["python", "budget.py"]
