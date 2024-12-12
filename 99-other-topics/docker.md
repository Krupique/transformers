Creating a Docker container involves the following steps:

---

### 1. **Install Docker**
Make sure Docker is installed on your system. You can verify this by running:
```bash
docker --version
```
If it’s not installed, follow the installation instructions for your operating system on the official [Docker website](https://docs.docker.com/get-docker/).

---

### 2. **Create a Dockerfile**
A **Dockerfile** is a configuration file where you define how the container will be built. Create a file named `Dockerfile` and add the necessary content. 

**Example of a Dockerfile for a Python application:**
```dockerfile
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

# Use ENTRYPOINT to specify the base command
ENTRYPOINT ["poetry", "run", "python", "inference.py"]

# CMD will be the default arguments, which can be overridden at runtime
CMD ["--prompt", "I would like to make sure you are happy"]
```

---

### 3. **Build the Docker image**
Use the `docker build` command to create the image from the Dockerfile:
```bash
docker build -t my-app .
```
- **`-t`**: Assigns a name to the image (in this case, `my-app`).
- **`.`**: Specifies the current directory as the location of the Dockerfile.

---

### 4. **Run a container**
After building the image, you can run a container based on it:
```bash
docker run -d -p 5000:5000 --name my-container my-app
```
- **`-d`**: Runs the container in detached mode (in the background).
- **`-p`**: Maps the host port (first number) to the container port (second number).
- **`--name`**: Assigns a name to the container (`my-container`).
- **`my-app`**: The name of the image to be used.

```bash
docker run --rm my-container --prompt "Write a poem about the stars"
```


---

### 5. **Check active containers**
To see the running containers, use:
```bash
docker ps
```

---

### 6. **Stop or remove containers**
- To stop a container:
  ```bash
  docker stop my-container
  ```
- To remove a container:
  ```bash
  docker rm my-container
  ```

---

### 7. **Maintenance**
- **List Docker images:**
  ```bash
  docker images
  ```
- **Remove images:**
  ```bash
  docker rmi my-app
  ```

These steps cover the basics of creating and running Docker containers. If you need help with more advanced features, such as volumes, networks, or orchestration, feel free to ask! 😊