# test humaneval

from human_eval.execution import check_correctness

py_pass = """
def add(a, b):
    return a + b
    
assert add(1, 2) == 3
"""

py_fail = """
def add(a, b):
    return a + b


assert add(1, 2) == 4
"""

java_pass = """
public class Add {
    public static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        assert add(1, 2) == 3;
    }
}
"""

java_fail = """
public class Add {
    public static int add(int a, int b) {
        return a + b;
    }

    public static void main(String[] args) {
        assert add(1, 2) == 4;
    }
}
"""

cpp_pass = """
#include <iostream>
#include <cassert>

int add(int a, int b) {
    return a + b;
}

int main() {
    assert(add(1, 2) == 3);
}
"""

cpp_fail = """
#include <iostream>
#include <cassert>

int add(int a, int b) {
    return a + b;
}

int main() {
    assert(add(1, 2) == 4);
}
"""

if __name__ == "__main__":
    # test python, expect pass
    print(check_correctness({"test_code": py_pass}, language="python"))
    # test python, expect fail
    print(check_correctness({"test_code": py_fail}, language="python"))
    # test java, expect pass
    print(check_correctness({"test_code": java_pass}, language="java"))
    # test java, expect fail
    print(check_correctness({"test_code": java_fail}, language="java"))
    # test cpp, expect pass
    print(check_correctness({"test_code": cpp_pass}, language="cpp"))
    # test cpp, expect fail
    print(check_correctness({"test_code": cpp_fail}, language="cpp"))
    
    """
    Expected output:
    {'passed': True, 'result': 'passed', 'completion_id': None}
    {'passed': False, 'result': 'failed: AssertionError', 'completion_id': None}
    {'passed': True, 'result': 'passed', 'completion_id': None}
    {'passed': False, 'result': 'failed: Exception in thread "main" java.lang.AssertionError\n\tat Add.main(task_5c95cd69.java:8)', 'completion_id': None}
    {'passed': True, 'result': 'passed', 'completion_id': None}
    {'passed': False, 'result': 'failed: Assertion failed: (add(1, 2) == 4), function main, file task_57eea8bf.cpp, line 10.', 'completion_id': None}
    """