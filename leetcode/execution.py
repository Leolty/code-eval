import re
from dataclasses import dataclass
from typing import Optional
import subprocess
from leetcode.utils import (
    get_leetcode_config,
    update_leetcode_config,
    get_problem_path_by_id,
    fetch_problem_by_id
)

@dataclass
class TestResult:
    success: bool
    runtime: Optional[int] = None
    output: str = ""

@dataclass
class SubmissionResult:
    success: bool
    runtime: Optional[int] = None
    memory: Optional[float] = None
    runtime_percentile: Optional[float] = None
    memory_percentile: Optional[float] = None
    output: str = ""

def test_leetcode(problem_id: int, lang: str, solution: str) -> TestResult:
    """
    Tests the leetcode solution and returns structured results.
    Always returns a TestResult, regardless of success/failure.
    """
    config = get_leetcode_config()
    if not config:
        return TestResult(success=False, output="Failed to load leetcode configuration")

    # Normalize language if needed
    lang = "python3" if lang.lower() == "python" else lang

    # Update config language if needed
    config_lang = config.get("code", {}).get("lang")
    if config_lang != lang and not update_leetcode_config(lang=lang):
        return TestResult(success=False, output="Failed to update language configuration")

    # Get or fetch problem
    problem_path = get_problem_path_by_id(problem_id, lang, config)
    if not problem_path:
        if not fetch_problem_by_id(problem_id, lang):
            return TestResult(success=False, output="Failed to fetch problem")
        problem_path = get_problem_path_by_id(problem_id, lang, config)
        if not problem_path:
            return TestResult(success=False, output="Problem file not found after fetch")

    # Write solution
    try:
        with open(problem_path, "w") as f:
            f.write(solution)
    except Exception as e:
        return TestResult(success=False, output=f"Failed to write solution: {str(e)}")

    # Run test
    try:
        result = subprocess.run(
            ["leetcode", "test", str(problem_id)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        
        output = result.stdout.strip()
        success = "accepted" in output.lower()
        
        # Parse runtime if available
        runtime = None
        runtime_match = re.search(r'Runtime: (\d+) ms', output)
        if runtime_match:
            runtime = int(runtime_match.group(1))

        return TestResult(
            success=success,
            runtime=runtime,
            output=output
        )

    except subprocess.CalledProcessError as e:
        # Even if the test fails, we want to capture the output
        output = e.stdout.strip() if e.stdout else e.stderr.strip()
        return TestResult(success=False, output=output)
    except Exception as e:
        return TestResult(success=False, output=str(e))

def submit_leetcode(problem_id: int, lang: str, solution: str) -> SubmissionResult:
    """
    Submits the leetcode solution and returns structured results.
    Always returns a SubmissionResult, regardless of success/failure.
    """
    config = get_leetcode_config()
    if not config:
        return SubmissionResult(success=False, output="Failed to load leetcode configuration")

    # Normalize language
    lang = "python3" if lang.lower() == "python" else lang

    # Update config language if needed
    config_lang = config.get("code", {}).get("lang")
    if config_lang != lang and not update_leetcode_config(lang=lang):
        return SubmissionResult(success=False, output="Failed to update language configuration")

    # Get or fetch problem
    problem_path = get_problem_path_by_id(problem_id, lang, config)
    if not problem_path:
        if not fetch_problem_by_id(problem_id, lang):
            return SubmissionResult(success=False, output="Failed to fetch problem")
        problem_path = get_problem_path_by_id(problem_id, lang, config)
        if not problem_path:
            return SubmissionResult(success=False, output="Problem file not found after fetch")

    # Write solution
    try:
        with open(problem_path, "w") as f:
            f.write(solution)
    except Exception as e:
        return SubmissionResult(success=False, output=f"Failed to write solution: {str(e)}")

    # Submit solution
    try:
        result = subprocess.run(
            ["leetcode", "exec", str(problem_id)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        
        output = result.stdout.strip()
        success = "success" in output.lower()
        
        # Parse statistics
        runtime_match = re.search(r'Runtime: (\d+) ms', output)
        memory_match = re.search(r'Memory Usage: ([\d.]+) MB', output)
        runtime_percentile_match = re.search(r'faster than ([\d.]+)%', output)
        memory_percentile_match = re.search(r'less than ([\d.]+)%', output)

        return SubmissionResult(
            success=success,
            runtime=int(runtime_match.group(1)) if runtime_match else None,
            memory=float(memory_match.group(1)) if memory_match else None,
            runtime_percentile=float(runtime_percentile_match.group(1)) if runtime_percentile_match else None,
            memory_percentile=float(memory_percentile_match.group(1)) if memory_percentile_match else None,
            output=output
        )

    except subprocess.CalledProcessError as e:
        # Even if the submission fails, we want to capture the output
        output = e.stdout.strip() if e.stdout else e.stderr.strip()
        return SubmissionResult(success=False, output=output)
    except Exception as e:
        return SubmissionResult(success=False, output=str(e))