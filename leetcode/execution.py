import os
import re
import subprocess
from typing import Tuple, Union, Dict, Optional
from leetcode.utils import (
    get_problem_path_by_id,
    fetch_problem_by_id,
    get_leetcode_config,
    update_leetcode_config
)

def test_leetcode(problem_id: int, lang: str, solution: str, return_runtime: bool = False) -> Union[bool, Tuple[bool, int]]:
    """
    Tests the leetcode module.

    Args:
        problem_id (int): The ID of the problem.
        lang (str): The language of the problem.
        solution (str): The solution to the problem.
        return_runtime (bool): Whether to return the runtime along with the success status.
        
    Returns:
        If return_runtime is False:
            bool: True if the test was successful, False otherwise.
        If return_runtime is True:
            Tuple[bool, int]: (success status, runtime in ms)
    """
    config = get_leetcode_config()
    if not config:
        print("Failed to load leetcode configuration.")
        return (False, 0) if return_runtime else False

    # Normalize language if needed
    original_lang = lang
    if lang.lower() == "python":
        lang = "python3"

    config_lang = config.get("code", {}).get("lang")
    if config_lang != lang:
        print(f"Language '{lang}' is not consistent with the config language '{config_lang}'.")
        print(f"Updating config language to '{lang}'...")
        if not update_leetcode_config(lang=lang):
            print("Error updating config language.")
            return (False, 0) if return_runtime else False

    problem_path = get_problem_path_by_id(problem_id, lang, config)

    if not problem_path:
        print(f"Problem file not found for problem {problem_id} in {lang}.")
        print("Fetching problem...")
        if not fetch_problem_by_id(problem_id, lang):
            print("Error fetching problem.")
            return (False, 0) if return_runtime else False
        problem_path = get_problem_path_by_id(problem_id, lang, config)
        if not problem_path:
            print(f"Problem file still not found for problem {problem_id} in {lang}.")
            return (False, 0) if return_runtime else False
    else:
        print(f"Problem file found at: {problem_path}")

    try:
        with open(problem_path, "w") as f:
            f.write(solution)
        print(f"Solution written to {problem_path}")
    except Exception as e:
        print(f"Failed to write solution to {problem_path}: {e}")
        return (False, 0) if return_runtime else False

    try:
        result = subprocess.run(
            ["leetcode", "test", str(problem_id)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        
        result = result.stdout.strip()
        
        # only when "Accepted" is in the result, the solution is correct
        if "accepted" not in result.lower():
            print(f"Tests failed for problem {problem_id}.")
            return (False, 0) if return_runtime else False
        
        # parse the result to get the runtime and memory usage
        runtime_value = 0
        if return_runtime:
            runtime = re.search(r'Runtime: (\d+) ms', result)
            runtime_value = int(runtime.group(1)) if runtime else 0

        print(f"Tests passed for problem {problem_id}.")

        return (True, runtime_value) if return_runtime else True
    except subprocess.CalledProcessError as e:
        print(f"Tests failed for problem {problem_id}.")
        print(e.stdout)
        print(e.stderr)
    except FileNotFoundError:
        print("leetcode-cli is not installed.")
    except Exception as e:
        print(f"An unexpected error occurred while testing: {e}")
    
    return (False, 0) if return_runtime else False


def submit_leetcode(problem_id: int, lang: str, solution: str, include_stats: bool = False) -> Union[bool, Tuple[bool, Dict[str, Optional[Union[int, float]]]]]:
    """
    Submits the leetcode problem solution.

    Args:
        problem_id (int): The ID of the problem.
        lang (str): The language of the problem.
        solution (str): The solution to the problem.
        include_stats (bool): Whether to return the runtime and memory usage statistics.
        
    Returns:
        If include_stats is False:
            bool: True if the submission was successful, False otherwise.
        If include_stats is True:
            Tuple[bool, Dict[str, Optional[Union[int, float]]]]: (success status, stats dictionary)
            The stats dictionary contains 'runtime', 'memory', 'runtime_percentile', and 'memory_percentile'.
    """
    config = get_leetcode_config()
    if not config:
        print("Failed to load leetcode configuration.")
        return (False, {}) if include_stats else False

    # Normalize language if needed
    if lang.lower() == "python":
        lang = "python3"

    config_lang = config.get("code", {}).get("lang")
    if config_lang != lang:
        print(f"Language '{lang}' is not consistent with the config language '{config_lang}'.")
        print(f"Updating config language to '{lang}'...")
        if not update_leetcode_config(lang=lang):
            print("Error updating config language.")
            return (False, {}) if include_stats else False

    problem_path = get_problem_path_by_id(problem_id, lang, config)

    if not problem_path:
        print(f"Problem file not found for problem {problem_id} in {lang}.")
        print("Fetching problem...")
        if not fetch_problem_by_id(problem_id, lang):
            print("Error fetching problem.")
            return (False, {}) if include_stats else False
        problem_path = get_problem_path_by_id(problem_id, lang, config)
        if not problem_path:
            print(f"Problem file still not found for problem {problem_id} in {lang}.")
            return (False, {}) if include_stats else False
    else:
        print(f"Problem file found at: {problem_path}")

    try:
        with open(problem_path, "w") as f:
            f.write(solution)
        print(f"Solution written to {problem_path}")
    except Exception as e:
        print(f"Failed to write solution to {problem_path}: {e}")
        return (False, {}) if include_stats else False

    try:
        result = subprocess.run(
            ["leetcode", "exec", str(problem_id)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        
        output = result.stdout.strip()
        
        if "success" not in output.lower():
            print(f"Submission failed for problem {problem_id}.")
            return (False, {}) if include_stats else False
        
        # Parse statistics
        stats = {}
        if include_stats:
            runtime_match = re.search(r'Runtime: (\d+) ms', output)
            memory_match = re.search(r'Memory Usage: ([\d.]+) MB', output)
            runtime_percentile_match = re.search(r'faster than ([\d.]+)%', output)
            memory_percentile_match = re.search(r'less than ([\d.]+)%', output)

            stats['runtime'] = int(runtime_match.group(1)) if runtime_match else None
            stats['memory'] = float(memory_match.group(1)) if memory_match else None
            stats['runtime_percentile'] = float(runtime_percentile_match.group(1)) if runtime_percentile_match else None
            stats['memory_percentile'] = float(memory_percentile_match.group(1)) if memory_percentile_match else None

        print(f"Submission successful for problem {problem_id}.")
        # if include_stats:
        #     print(f"Runtime: {stats['runtime']} ms, faster than {stats['runtime_percentile']}% of submissions.")
        #     print(f"Memory Usage: {stats['memory']} MB, less than {stats['memory_percentile']}% of submissions.")

        return (True, stats) if include_stats else True
    except subprocess.CalledProcessError as e:
        print(f"Submission failed for problem {problem_id}.")
        print(e.stdout)
        print(e.stderr)
    except FileNotFoundError:
        print("leetcode-cli is not installed.")
    except Exception as e:
        print(f"An unexpected error occurred while submitting: {e}")
    
    return (False, {}) if include_stats else False

if __name__ == "__main__":
    import time
    
    # Example usage
    problem_id = 5
    lang = "python"
    solution = """
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                    Max_Len = j-i+1
                    Max_Str = s[i:j+1]

        return Max_Str
"""
    # Test without returning runtime
    success = test_leetcode(problem_id, lang, solution)
    if success:
        print("Test completed successfully.")
    else:
        print("Test failed.")
        
    # sleep for 3 seconds
    time.sleep(3)

    # Test with returning runtime
    success, runtime = test_leetcode(problem_id, lang, solution, return_runtime=True)
    if success:
        print(f"Test completed successfully. Runtime: {runtime} ms")
    else:
        print("Test failed.")

    # Submit without returning stats
    success = submit_leetcode(problem_id, lang, solution)
    if success:
        print("Submission completed successfully.")
    else:
        print("Submission failed.")
        
    # sleep for 3 seconds
    time.sleep(3)
    
    # Submit with returning stats
    success, stats = submit_leetcode(problem_id, lang, solution, include_stats=True)
    if success:
        print("Submission completed successfully.")
        print(f"Runtime: {stats['runtime']} ms, faster than {stats['runtime_percentile']}% of submissions.")
        print(f"Memory Usage: {stats['memory']} MB, less than {stats['memory_percentile']}% of submissions.")
    else:
        print("Submission failed.")