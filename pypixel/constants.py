"""
Constants used throughout the project.
"""
START = "<start>"  # start and end tokens
END = "</end>"
SECRETS = "secrets.json"  # secrets file
ALLOWED_LIBRARIES = "opencv", "numpy", "matplotlib", "cv2"
OPENAI_API_KEY = "OPENAI_KEY"  # environment variables
COHERE_API_KEY = "COHERE_KEY"
STARCODER_API_KEY = "STARCODER_KEY"
BLACKLIST = (  # blacklisted functions
    "eval",
    "exec",
    "os.system",
    "__import__",
    "subprocess",
    "shell",
    "input",
    "pickle",
    "rm -rf",
    "rmdir",
    "unlink",
    "remove",
    "compile",
    "getattr",
    "setattr",
    "delattr",
    "globals",
    "locals",
    "vars",
    "dir",
)
DOWNLOAD_DIR = "downloads"  # directory for downloads
