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
    "open",
    "file",
    "input",
    "pickle",
    "dangerous_function",
    "rm",
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
    "type",
    "repr",
)
