# Code-Eval

This repository is designed to evaluate the **executability** of LLM-generated code. It is largely based on, modified, and extended from [OpenAI's HumanEval](https://github.com/openai/human-eval).

## How to Use

### 1. Check Your Environment

Before running the code, you need to set up the environment using `conda`. Follow these steps:

1. Clone this project:
   ```
   git clone git@github.com:Leolty/code-eval.git
   cd code-eval
   ```

2. Create and activate a conda environment named `codeeval`:
   ```bash
   conda create --name codeeval python=3.8
   conda activate codeeval
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

> **Note:** The `requirements.txt` may not include all necessary packages. Use `pip install <package_name>` to install any missing dependencies as needed.

4. Verify your environment for Java, C++, and Python. Make sure you're in the root directory of the repo, then run the following commands:

   **Python Test**:
   ```bash
   python ./test/test.py
   ```

   **Java Test**:
   ```bash
   java ./test/Test.java
   ```

   **C++ Test**:
   ```bash
   g++ -o ./test/test ./test/test.cpp && ./test/test && rm ./test/test
   ```

   Ensure that all tests pass and display the output:  
   `All tests passed!`  
   If so, your environment is ready. If not, please troubleshoot any issues about the environment setup before proceeding.

### 2. Execute Code

To check whether a generated code snippet is correct (more precisely, executable), you can use the `check_correctness` function. Here’s a simple example for Python code:

```python
from human_eval.execution import check_correctness

python_code = """
def add(a, b):
    return a + b
    
print(add(1, 2))
"""

res = check_correctness(
    sample={"test_code": python_code},
    language="python",
)

print(res)
```

This will output:
```json
{'passed': True, 'result': 'passed', 'completion_id': None}
```

#### Explanation of `check_correctness`:

The `check_correctness` function evaluates the correctness of code based on the following parameters:

- `sample`: A dictionary containing the test code (under the key `test_code`) that you want to evaluate, and other optional relevant information (e.g., `task_id`).
- `language`: The programming language of the code you are testing. Supported languages include "python", "java", and "cpp" now.
- `timeout`: The maximum allowed time (in seconds) for the execution. By default, this is set to 5 seconds.
- `completion_id`: (Optional) A unique identifier used for matching test results if needed.

The function executes the code in a sandboxed environment and returns whether the code passed, failed, or timed out.

## Disclaimer

### Authorship
This repository is based on OpenAI’s [HumanEval](https://github.com/openai/human-eval), with minor modifications.

### Safety
The code provided here is for evaluation purposes only. **Do not execute untrusted or potentially unsafe code in your local environment**. This evaluation tool is designed to run model-generated code, which may cause unintended side effects. Users are strongly encouraged to sandbox the evaluation to prevent any destructive actions on their host systems or networks. Please ensure appropriate precautions are taken before running any code.