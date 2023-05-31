START = "<start>"
END = "</end>"
SECRETS = "secrets.json"
ALLOWED_LIBRARIES = "opencv", "numpy", "matplotlib", "cv2"
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
DOWNLOAD_DIR = "downloads"
