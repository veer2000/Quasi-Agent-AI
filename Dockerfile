# # Dockerfile

# # Use a Python base image.
# # We'll use python:3.10 (which is based on Debian) as it's easier to add build tools.
# # If you prefer 'slim-buster', you'd need to install more specific dependencies.
# FROM python:3.10

# # Set environment variables to prevent Python from buffering stdout/stderr
# ENV PYTHONUNBUFFERED 1

# # Set the working directory in the container
# WORKDIR /app

# # Copy the requirements file first to leverage Docker's build cache.
# # If requirements.txt doesn't change, this layer (and subsequent install) will be cached.
# COPY src/requirements.txt .

# # Install system dependencies required for building some Python packages (like xformers, torch).
# # build-essential provides compilers (gcc, g++), make, etc.
# # libgl1-mesa-glx and libglib2.0-0 are sometimes needed for graphics-related dependencies
# # that might be pulled in by ML libraries.
# RUN apt-get update && \
#     apt-get install -y --no-install-recommends \
#     build-essential \
#     libgl1-mesa-glx \
#     libglib2.0-0 && \
#     rm -rf /var/lib/apt/lists/*

# # Upgrade pip to the latest version
# RUN pip install --no-cache-dir --upgrade pip

# # Install PyTorch (CPU version) first, as xformers depends on it for building.
# # IMPORTANT: Replace '2.3.0' with the specific PyTorch version you need from your requirements.txt.
# # We use --index-url to explicitly get the CPU-only version, which is crucial for Docker.
# RUN pip install --no-cache-dir torch==2.3.0 --index-url https://download.pytorch.org/whl/cpu

# # Install all other Python dependencies from requirements.txt.
# # This will now include xformers, which should find torch already installed.
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the rest of your application code
# # This should be after requirements.txt to optimize caching
# COPY . .

# # Expose the port your FastAPI app runs on
# EXPOSE 8000

# # Command to run your application when the container starts
# # Assuming your main FastAPI app is in app/main.py and the app instance is named 'app'
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

#-------------------------
FROM python:3.13.3-slim-bookworm

WORKDIR app/src/

COPY src/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY src/ .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
