import re
from abc import ABC, abstractmethod
import os

class FileFilterStrategy(ABC):
    @abstractmethod
    def is_excluded(self, filename: str) -> bool:
        pass

class DependencyFileFilter(FileFilterStrategy):
    EXCLUDED_DIRS = [
        "node_modules/",
        "vendor/",
        ".venv/",
        "venv/",
        "env/",
        "dist/",
        "build/",
        "__pycache__/",
        ".idea/",
        "gradlew",
        "gradlew.bat",
        ".git/",
        ".svn/",
        ".hg/",
        ".bzr/",
        ".hg/",
        "_darcs/",
        ".fslckout/",
        ".gitmodules/",
    ]

    EXCLUDED_FILE_EXTENSIONS = [
        ".jar", ".dll", ".so", ".exe", ".pdb",
        ".min.js", ".map", ".lock", ".zip", ".tar.gz", ".whl",
        ".class", ".pyc", ".iml", ".svg",".log",".gitattributes",
    ]

    EXCLUDED_FILENAMES = [
        "package-lock.json", "yarn.lock", "Pipfile.lock", "poetry.lock"
    ]

    _log_file_pattern = re.compile(r"\.log(\.\d+)?$")

    def is_excluded(self, filename: str) -> bool:
        # Checking directory exclusion
        for excluded_dir in self.EXCLUDED_DIRS:
            if filename.startswith(excluded_dir) or f"/{excluded_dir}" in filename:
                return True

        # Checking file extension exclusion (except .log handled separately)
        for ext in self.EXCLUDED_FILE_EXTENSIONS:
            if ext == ".log":
                continue
            if filename.endswith(ext):
                return True

        # .log variants with regex
        if self._log_file_pattern.search(filename):
            return True

        # Checking specific filenames to exclude
        if os.path.basename(filename) in self.EXCLUDED_FILENAMES:
            return True

        return False