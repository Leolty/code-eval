import os
import toml
import subprocess
from typing import Optional, Dict
from logging import Logger, getLogger, NullHandler

LANGUAGES_TO_SUFFIX: Dict[str, str] = {
    "python": "py",
    "python3": "py",
    "java": "java",
    "cpp": "cpp",
    "c": "c",
    "javascript": "js",
    "typescript": "ts",
    "ruby": "rb",
    "swift": "swift",
    "go": "go",
    "rust": "rs",
    "php": "php",
    "bash": "sh",
    "r": "r",
    "mysql": "sql",
}

def check_leetcode_installed() -> bool:
    """Checks if leetcode-cli is installed."""
    try:
        subprocess.run(
            ["leetcode", "-V"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True
        )
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def get_leetcode_config(path: str = "~/.leetcode/leetcode.toml") -> Optional[Dict]:
    """Reads the leetcode config file."""
    config_path = os.path.expanduser(path)
    try:
        with open(config_path, 'r') as config_file:
            return toml.load(config_file)
    except Exception:
        return None

def update_leetcode_config(lang: str, path: str = "~/.leetcode/leetcode.toml") -> bool:
    """Updates the language in the leetcode config file."""
    config_path = os.path.expanduser(path)
    try:
        with open(config_path, 'r') as config_file:
            config = toml.load(config_file)
        config['code']['lang'] = lang
        with open(config_path, 'w') as config_file:
            toml.dump(config, config_file)
        return True
    except Exception:
        return False

def get_problem_path_by_id(problem_id: int, lang: str, config: Dict) -> str:
    """Gets the path to the problem file."""
    try:
        problem_dir = os.path.join(config['storage']['root'], config['storage']['code'])
        problem_dir = os.path.expanduser(problem_dir)
        suffix = LANGUAGES_TO_SUFFIX.get(lang)
        if not suffix:
            return ""
        for file_name in os.listdir(problem_dir):
            if file_name.startswith(f"{problem_id}.") and file_name.endswith(f".{suffix}"):
                return os.path.join(problem_dir, file_name)
        return ""
    except Exception:
        return ""

def fetch_problem_by_id(problem_id: int, lang: str) -> bool:
    """Fetches the problem by ID using leetcode-cli."""
    try:
        subprocess.run(
            ["leetcode", "edit", str(problem_id)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return True
    except Exception:
        return False