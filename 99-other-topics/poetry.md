### Basic Guide to the Poetry Package Manager

**Poetry** is a modern tool for managing Python dependencies and packages. It combines functionalities like project creation, dependency management, and package publishing, making developers' lives easier.

---

### **Installation**
1. **Using Script (Recommended):**
   Run the command:
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Windows (Using PowerShell):**
   ```powershell
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
   ```

After installation, ensure Poetry is added to your PATH. Verify the installation with:
```bash
poetry --version
```

---

### **Initial Configuration**
To set global preferences, use:
```bash
poetry config --list
```
Example: Change the PyPI repository:
```bash
poetry config repositories.my-repo https://pypi.org/
```

---

### **Creating a New Project**
To create a new project with a virtual environment:
```bash
poetry new project_name
```

Project structure:
```
project_name/
├── pyproject.toml
├── README.rst
├── project_name/
│   └── __init__.py
└── tests/
    └── __init__.py
```

---

### **Managing Dependencies**
1. **Add dependencies:**
   - Main dependencies:
     ```bash
     poetry add package_name
     ```
   - Development dependencies:
     ```bash
     poetry add package_name --group dev
     ```

2. **Remove dependencies:**
   ```bash
   poetry remove package_name
   ```

3. **Update dependencies:**
   ```bash
   poetry update
   ```

---

### **Handling Virtual Environments**
Poetry automatically creates a virtual environment:
- Access the virtual environment shell:
  ```bash
  poetry shell
  ```
- Run commands within the environment:
  ```bash
  poetry run python script.py
  ```

---

### **Working with `pyproject.toml`**
This file defines project settings, such as dependencies, Python version, and package metadata.

Example of dependencies:
```toml
[tool.poetry.dependencies]
python = "^3.10"
numpy = "^1.23.0"
```

---

### **Testing Your Project**
1. Add testing tools like `pytest`:
   ```bash
   poetry add pytest --group dev
   ```
2. Run the tests:
   ```bash
   poetry run pytest
   ```

---

### **Publishing Packages**
1. Build the package:
   ```bash
   poetry build
   ```
2. Publish to PyPI:
   ```bash
   poetry publish --username your-username --password your-password
   ```

---

### **Useful Commands**
- **List installed dependencies:**
  ```bash
  poetry show
  ```
- **Lock dependency versions:**
  ```bash
  poetry lock
  ```
- **Check project status:**
  ```bash
  poetry check
  ```

---

### **Advanced Features**
1. **Using Custom Repositories:**
   Configure additional repositories:
   ```bash
   poetry config repositories.<repo-name> <repo-url>
   ```
   Add packages from a custom repository:
   ```bash
   poetry add package --source <repo-name>
   ```

2. **Custom Scripts:**
   Define custom scripts in `pyproject.toml`:
   ```toml
   [tool.poetry.scripts]
   my-script = "module:function"
   ```
   Run the script:
   ```bash
   poetry run my-script
   ```

---

### **Tips and Best Practices**
- Always use the `poetry.lock` file to ensure consistent dependency versions across environments.
- Configure local virtual environments with:
  ```bash
  poetry config virtualenvs.in-project true
  ```

For more information, refer to the [official Poetry documentation](https://python-poetry.org/docs/).

---

Poetry for PyTorch GPU - Step by Step

Primeiro é necessário inicializar o Poetry:
```bash
    poetry init
```

No arquivo pyproject.toml insira as seguintes dependências:
```bash
    [tool.poetry.dependencies]
    torch = { version = "^2.5.0", source = "pytorch" }

    [[tool.poetry.source]]
    name = "pytorch"
    url = "https://download.pytorch.org/whl/cu118"
    priority = "explicit"

```

Salve o arquivo e em seguida execute os seguintes comandos no terminal:
```bash
    poetry lock
    poetry add torch torchvision torchaudio --source pytorch
```

Para utilizar o jupyter notebook, adcione-o utilizando `poetry add`:
```bash
    poetry add ipykernel
```

Para instalar o Tensorflow, siga esse tutorial:
[TensorFlow 2.x cannot be imported after Poetry install on Windows](https://github.com/tensorflow/tensorflow/issues/62899)