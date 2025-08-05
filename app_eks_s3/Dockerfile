FROM amazonlinux:2023

RUN yum -y install vim-enhanced

# Install Python and pip
RUN yum install -y python3 python3-pip

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME DSD

# Run app.py when the container launches
CMD ["sleep", "infinity"]
