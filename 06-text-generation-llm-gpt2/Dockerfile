# Use an official Python image as the base
FROM python:3.12.3

# Set the working directory in the container
WORKDIR /app

# Copy the Poetry configuration files to the container
COPY pyproject.toml poetry.lock ./

# Install Poetry
RUN pip install --no-cache-dir poetry

# Install the project dependencies using Poetry
RUN poetry install --no-root

# Copy the project files into the container
COPY . .

# Expose a port (if your script needs it, e.g., for APIs)
# EXPOSE 8000

# Use ENTRYPOINT to specify the base command
ENTRYPOINT ["poetry", "run", "python", "run.py"]

# CMD will be the default arguments, which can be overridden at runtime
CMD ["--prompt", "Once upon a time"]
