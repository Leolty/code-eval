# 👩‍⚖ Code-Eval 👨‍⚖️

This repository is designed to evaluate the **executability** of LLM-generated code. It is largely based on, modified, and extended from [OpenAI's HumanEval](https://github.com/openai/human-eval).

## 🛠️ How to Use

### 1. ✅ Check Your Environment

Before running the code, you need to set up the environment using `conda`. Follow these steps to set up the environment:

1. Clone the repository and set up the environment:

   ```bash
   git clone git@github.com:Leolty/code-eval.git && cd code-eval
   conda create --name codeeval python=3.10 && conda activate codeeval
   pip install -r requirements.txt
   ```

   > **🔍 Note:** The `requirements.txt` may not include all necessary packages. Use `pip install <package_name>` to install any missing dependencies as needed.

2. Verify your environment for Java, C++, and Python:

   ```bash
   # 🐍 Python Test
   python ./test/test.py

   # ☕ Java Test
   java ./test/Test.java

   # 💻 C++ Test
   g++ -o ./test/test ./test/test.cpp && ./test/test && rm ./test/test
   ```

   If all tests output `All tests passed!` 🎉, your environment should be ready. If not, please troubleshoot any issues about the environment setup before proceeding.

### 2. 🧪 Execute Code

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
   {
     "passed": true,
     "result": "passed",
     "completion_id": null
   }
   ```

#### ℹ️ Explanation of `check_correctness`:

The `check_correctness` function evaluates the correctness of code based on the following parameters:

- `sample`: A dictionary containing the test code (under the key `test_code`) that you want to evaluate, and other optional relevant information (e.g., `task_id`).
- `language`: The programming language of the code you are testing. Supported languages include "python", "java", and "cpp" now.
- `timeout`: The maximum allowed time (in seconds) for the execution. By default, this is set to 5 seconds.
- `completion_id`: (Optional) A unique identifier used for matching test results if needed.

The function executes the code in a sandboxed environment 🛡️ and returns whether the code passed, failed, or timed out ⏳.

## ⚠️ Disclaimer

### 📝 Authorship
This repository is based on OpenAI’s [HumanEval](https://github.com/openai/human-eval), with minor modifications.

### 🔒 Safety
The code provided here is for evaluation purposes only. **Do not execute untrusted or potentially unsafe code in your local environment**. This evaluation tool is designed to run model-generated code, which may cause unintended side effects. Users are strongly encouraged to sandbox the evaluation to prevent any destructive actions on their host systems or networks. Please ensure appropriate precautions are taken before running any code.
