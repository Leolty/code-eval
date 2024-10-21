import os
import toml
import subprocess
from typing import Optional, Dict

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
    """
    Checks if leetcode-cli is installed by running 'leetcode -V'.

    Returns:
        bool: True if leetcode-cli is installed, False otherwise.
    """
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
    """
    Reads the leetcode config file and returns the parsed TOML content.

    Args:
        path (str): The path to the leetcode config file.

    Returns:
        Optional[Dict]: The parsed TOML content, or None if an error occurs.
    """
    config_path = os.path.expanduser(path)

    try:
        with open(config_path, 'r') as config_file:
            config = toml.load(config_file)
        return config
    except FileNotFoundError:
        print(f"Config file not found at {config_path}")
    except toml.TomlDecodeError as e:
        print(f"Error parsing TOML file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return None

def update_leetcode_config(lang: str, path: str = "~/.leetcode/leetcode.toml") -> bool:
    """
    Updates the language in the leetcode config file.

    Args:
        lang (str): The new language to set.
        path (str): The path to the leetcode config file.

    Returns:
        bool: True if the update was successful, False otherwise.
    """
    config_path = os.path.expanduser(path)

    try:
        with open(config_path, 'r') as config_file:
            config = toml.load(config_file)
        
        config['code']['lang'] = lang

        with open(config_path, 'w') as config_file:
            toml.dump(config, config_file)
        
        print(f"Successfully updated 'lang' to '{lang}' in {config_path}")
        return True
    except FileNotFoundError:
        print(f"Config file not found at {config_path}")
    except toml.TomlDecodeError as e:
        print(f"Error parsing TOML file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return False

def get_problem_path_by_id(problem_id: int, lang: str, config: Dict) -> str:
    """
    Given a problem ID and the leetcode config, returns the path to the problem file.

    Args:
        problem_id (int): The ID of the problem.
        lang (str): The programming language (e.g., 'python', 'java').
        config (Dict): Configuration dict with storage paths.

    Returns:
        str: The path to the matched problem file, or an empty string if no match is found.
    """
    try:
        problem_dir = os.path.join(config['storage']['root'], config['storage']['code'])
        problem_dir = os.path.expanduser(problem_dir)

        suffix = LANGUAGES_TO_SUFFIX.get(lang)
        if not suffix:
            print(f"Language '{lang}' is not supported.")
            return ""

        for file_name in os.listdir(problem_dir):
            if file_name.startswith(f"{problem_id}.") and file_name.endswith(f".{suffix}"):
                return os.path.join(problem_dir, file_name)

        return ""
    except KeyError as e:
        print(f"Missing key in config: {e}")
    except FileNotFoundError:
        print(f"Problem directory not found: {problem_dir}")
    except Exception as e:
        print(f"Error: {e}")
    
    return ""

def fetch_problem_by_id(problem_id: int, lang: str) -> bool:
    """
    Fetches the problem by ID and language using leetcode-cli.

    Args:
        problem_id (int): The ID of the problem.
        lang (str): The programming language.

    Returns:
        bool: True if the problem was fetched successfully, False otherwise.
    """
    try:
        result = subprocess.run(
            ["leetcode", "edit", str(problem_id)],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error fetching problem {problem_id}: {e.stderr.strip()}")
    except FileNotFoundError:
        print("leetcode-cli is not installed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    return False

if __name__ == "__main__":
    if check_leetcode_installed():
        config = get_leetcode_config()
        if config:
            problem_id = 5
            lang = "python"
            problem_path = get_problem_path_by_id(problem_id, lang, config)
            
            if problem_path:
                print(f"Problem file found at: {problem_path}")
            else:
                print(f"Problem file not found for problem {problem_id} in {lang}.")
                print("Fetching problem...")
                if fetch_problem_by_id(problem_id, lang):
                    problem_path = get_problem_path_by_id(problem_id, lang, config)
                    if problem_path:
                        print(f"Problem file found at: {problem_path}")
                    else:
                        print(f"Problem file still not found for problem {problem_id} in {lang}.")
                else:
                    print("Failed to fetch the problem.")
    else:
        print("leetcode-cli is not installed.")
