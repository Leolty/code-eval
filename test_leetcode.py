from leetcode.execution import test_leetcode, submit_leetcode

two_sum_py = """
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Dictionary to store the number and its index
        num_map = {}
        
        # Loop through the list of numbers
        for i, num in enumerate(nums):
            complement = target - num
            
            # Check if the complement is already in the dictionary
            if complement in num_map:
                # Return the indices of the two numbers
                return [num_map[complement], i]
            
            # Add the number to the dictionary
            num_map[num] = i

        # If no solution is found (though problem guarantees one exists)
        return []
"""

two_sum_java = """
class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Create a hashmap to store the values and their indices
        HashMap<Integer, Integer> map = new HashMap<>();
        
        // Loop through the array
        for (int i = 0; i < nums.length; i++) {
            // Calculate the complement that we are looking for
            int complement = target - nums[i];
            
            // If we find the complement in the map, return the indices
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            
            // If not, store the current number and its index in the map
            map.put(nums[i], i);
        }
        
        // Return an empty array if no solution is found (though the problem guarantees a solution)
        return new int[0];
    }
}
"""

two_sum_py_fail = """
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return [0, 1]
"""

two_sum_java_fail = """
class Solution {
    public int[] twoSum(int[] nums, int target) {
        return new int[] {0, 1};
    }
}
"""

if __name__ == "__main__":
    
    #### Below are the successful tests ####
    
    print(test_leetcode(problem_id=1, lang="python", solution=two_sum_py, return_runtime=True))
    print(submit_leetcode(problem_id=1, lang="python", solution=two_sum_py, include_stats=True))
    
    import time
    time.sleep(3)
    
    print(test_leetcode(problem_id=1, lang="java", solution=two_sum_java, return_runtime=True))
    print(submit_leetcode(problem_id=1, lang="java", solution=two_sum_java, include_stats=True))
    
    import time
    time.sleep(3)
    
    #### Below are the failed tests ####
    
    print(test_leetcode(problem_id=1, lang="python", solution=two_sum_py_fail, return_runtime=True))
    print(submit_leetcode(problem_id=1, lang="python", solution=two_sum_py_fail, include_stats=True))
    
    import time
    time.sleep(3)
    
    print(test_leetcode(problem_id=1, lang="java", solution=two_sum_java_fail, return_runtime=True))
    print(submit_leetcode(problem_id=1, lang="java", solution=two_sum_java_fail, include_stats=True))
    
    """
    My output:
    Language 'python3' is not consistent with the config language 'java'.
    Updating config language to 'python3'...
    Successfully updated 'lang' to 'python3' in /Users/tianyangliu/.leetcode/leetcode.toml
    Problem file found at: /Users/tianyangliu/.leetcode/code/1.two-sum.py
    Solution written to /Users/tianyangliu/.leetcode/code/1.two-sum.py
    Tests passed for problem 1.
    (True, 0)
    Problem file found at: /Users/tianyangliu/.leetcode/code/1.two-sum.py
    Solution written to /Users/tianyangliu/.leetcode/code/1.two-sum.py
    Submission successful for problem 1.
    (True, {'runtime': 0, 'memory': 17.7, 'runtime_percentile': 100.0, 'memory_percentile': 41.0})
    Language 'java' is not consistent with the config language 'python3'.
    Updating config language to 'java'...
    Successfully updated 'lang' to 'java' in /Users/tianyangliu/.leetcode/leetcode.toml
    Problem file found at: /Users/tianyangliu/.leetcode/code/1.two-sum.java
    Solution written to /Users/tianyangliu/.leetcode/code/1.two-sum.java
    Tests passed for problem 1.
    (True, 0)
    Problem file found at: /Users/tianyangliu/.leetcode/code/1.two-sum.java
    Solution written to /Users/tianyangliu/.leetcode/code/1.two-sum.java
    Submission successful for problem 1.
    (True, {'runtime': 2, 'memory': 45.0, 'runtime_percentile': 98.0, 'memory_percentile': 18.0})
    Language 'python3' is not consistent with the config language 'java'.
    Updating config language to 'python3'...
    Successfully updated 'lang' to 'python3' in /Users/tianyangliu/.leetcode/leetcode.toml
    Problem file found at: /Users/tianyangliu/.leetcode/code/1.two-sum.py
    Solution written to /Users/tianyangliu/.leetcode/code/1.two-sum.py
    Tests failed for problem 1.
    (False, 0)
    Problem file found at: /Users/tianyangliu/.leetcode/code/1.two-sum.py
    Solution written to /Users/tianyangliu/.leetcode/code/1.two-sum.py
    Submission failed for problem 1.
    (False, {})
    Language 'java' is not consistent with the config language 'python3'.
    Updating config language to 'java'...
    Successfully updated 'lang' to 'java' in /Users/tianyangliu/.leetcode/leetcode.toml
    Problem file found at: /Users/tianyangliu/.leetcode/code/1.two-sum.java
    Solution written to /Users/tianyangliu/.leetcode/code/1.two-sum.java
    Tests failed for problem 1.
    (False, 0)
    Problem file found at: /Users/tianyangliu/.leetcode/code/1.two-sum.java
    Solution written to /Users/tianyangliu/.leetcode/code/1.two-sum.java
    Submission failed for problem 1.
    (False, {})
"""