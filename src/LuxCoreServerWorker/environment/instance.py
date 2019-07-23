import os

# Load the development "mode". Use "developmen" if not specified
env = os.environ.get("PYTHON_ENV", "development")

# Configuration for each environment
# Alternatively use "python-dotenv"
all_environments = {
    "development": {"host": "0.0.0.0", "port": 5000, "debug": True, "swagger-url": "/" },
    "production": { "host": "0.0.0.0", "port": 8080, "debug": False, "swagger-url": None  }
}

# The config for the current environment
environment_config = all_environments[env]