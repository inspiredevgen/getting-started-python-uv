# Getting started with UV for Python

## I. Using UV

### 1. What is UV ?

UV is an extremely fast Python package and project manager, written in Rust.

> "A single tool to replace pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, and more."

**UV** can so much more, please checkout the official website

More information: https://docs.astral.sh/uv/

### 2. How do I install UV ?

One simple commmand:

```bash
pip install uv
Collecting uv
  Obtaining dependency information for uv from https://files.pythonhosted.org/packages/f1/7e/4c8b7ca07945fe6ffd1a7e5d1f992b72534be69e97e20a2536d192734adc/uv-0.5.17-py3-none-macosx_11_0_arm64.whl.metadata
  Downloading uv-0.5.17-py3-none-macosx_11_0_arm64.whl.metadata (11 kB)
Downloading uv-0.5.17-py3-none-macosx_11_0_arm64.whl (14.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 14.0/14.0 MB 15.0 MB/s eta 0:00:00
Installing collected packages: uv
Successfully installed uv-0.5.17
```

### 3. Installing a version of Python

```bash
uv python install 3.12
Installed Python 3.12.8 in 1.58s
 + cpython-3.12.8-macos-aarch64-none
```

### 4. How to initialize a new Project under UV

```bash
uv init project-1
Initialized project `project-1` at `/Projects/getting-started-python-uv/project-1`
```

#### 4.1 Exploring the pyproject.toml file

```txt
[project]
name = "project-1"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = []

```

#### 4.2 Creating a Virtual Environment with UV

```bash
uv python install 3.12
Installed Python 3.12.8 in 1.58s
 + cpython-3.12.8-macos-aarch64-none
```

#### 4.3 Creating a virtual environment using Python 3.13

```bash
uv venv --python 3.13
Using CPython 3.13.1 interpreter at: /opt/homebrew/opt/python@3.13/bin/python3.13
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
```

#### 4.4 Activating your Virtual Environment

```bash
source .venv/bin/activate
```

#### 4.5 Installing our first package (fastapi)

```bash
uv add fastapi

Using CPython 3.12.8
Removed virtual environment at: .venv
Creating virtual environment at: .venv
Resolved 10 packages in 441ms
Prepared 9 packages in 277ms
Installed 9 packages in 10ms
 + annotated-types==0.7.0
 + anyio==4.8.0
 + fastapi==0.115.6
 + idna==3.10
 + pydantic==2.10.5
 + pydantic-core==2.27.2
 + sniffio==1.3.1
 + starlette==0.41.3
 + typing-extensions==4.12.2
```

#### 4.6 Installing uvicorn

```bash
uv add uvicorn

### Output ###
Resolved 14 packages in 184ms
Prepared 3 packages in 69ms
Installed 3 packages in 7ms
+ click==8.1.8
+ h11==0.14.0
+ uvicorn==0.34.0
```

#### 4.7 Dependencies are updated

```txt
[project]
name = "project-1"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
   "fastapi>=0.115.6",
   "uvicorn>=0.34.0",
]
```

#### 4.8 Running your project

```bash
uv run main.py

### Output ###

INFO:     Started server process [66888]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:62055 - "GET / HTTP/1.1" 200 OK
^CINFO:     Shutting down
INFO:     Waiting for application shutdown.
INFO:     Application shutdown complete.
INFO:     Finished server process [66888]
```

## II. Projects in this Repo

### Project-1: simple FastAPI project

[project-1 - FastAPI](https://github.com/inspiredevgen/getting-started-python-uv/tree/main/project-1)

### Project-2: Pydantic Project

[Project-2 FastAPI](https://github.com/inspiredevgen/getting-started-python-uv/tree/main/project-2)

### Project-3: FastAPI Auth Project

[Project-3 FastAPI Auth](https://github.com/inspiredevgen/getting-started-python-uv/tree/main/project-3)

### Project-4: FastAPI: Car inventory project

[Project-4 Car Inventory App](https://github.com/inspiredevgen/getting-started-python-uv/tree/main/project-4)

### Project-5: Flask WebApp

[Project-5 Flask WebApp](https://github.com/inspiredevgen/getting-started-python-uv/tree/main/project-5)

### Project-6: simple database project using DuckDB

[Project-6 DuckDB](https://github.com/inspiredevgen/getting-started-python-uv/tree/main/project-6)

[project-7 Python with SQLite]
