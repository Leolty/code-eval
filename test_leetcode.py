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
    
    print(test_leetcode(problem_id=1, lang="python", solution=two_sum_py))
    print(submit_leetcode(problem_id=1, lang="python", solution=two_sum_py))
    
    import time
    time.sleep(3)
    
    print(test_leetcode(problem_id=1, lang="java", solution=two_sum_java))
    print(submit_leetcode(problem_id=1, lang="java", solution=two_sum_java))
    
    import time
    time.sleep(3)
    
    #### Below are the failed tests ####
    
    print(test_leetcode(problem_id=1, lang="python", solution=two_sum_py_fail))
    print(submit_leetcode(problem_id=1, lang="python", solution=two_sum_py_fail))
    
    import time
    time.sleep(3)
    
    print(test_leetcode(problem_id=1, lang="java", solution=two_sum_java_fail))
    print(submit_leetcode(problem_id=1, lang="java", solution=two_sum_java_fail))
    
    """
    My output:
    TestResult(success=True, runtime=0, output='Accepted       Runtime: 0 ms\n\nYour input:    [2,7,11,15]↩ 9↩ [3,2,4]↩ 6↩ [3,3]↩ 6\nOutput:        [0,1]↩ [1,2]↩ [0,1]↩ \nExpected:      [0,1]↩ [1,2]↩ [0,1]↩')
    SubmissionResult(success=True, runtime=0, memory=17.8, runtime_percentile=100.0, memory_percentile=42.0, output='Success\n\nRuntime: 0 ms, faster than 100% of Python3 online submissions for Two Sum.\n\nMemory Usage: 17.8 MB, less than 42% of Python3 Two Sum.\n\nStdout:')
    TestResult(success=True, runtime=0, output='Accepted       Runtime: 0 ms\n\nYour input:    [2,7,11,15]↩ 9↩ [3,2,4]↩ 6↩ [3,3]↩ 6\nOutput:        [0,1]↩ [1,2]↩ [0,1]↩ \nExpected:      [0,1]↩ [1,2]↩ [0,1]↩')
    SubmissionResult(success=True, runtime=2, memory=44.7, runtime_percentile=98.0, memory_percentile=76.0, output='Success\n\nRuntime: 2 ms, faster than 98% of Java online submissions for Two Sum.\n\nMemory Usage: 44.7 MB, less than 76% of Java Two Sum.\n\nStdout:')
    TestResult(success=False, runtime=0, output='Wrong Answer   Runtime: 0 ms\n\nYour input:    [2,7,11,15]↩ 9↩ [3,2,4]↩ 6↩ [3,3]↩ 6\nOutput:        [0,1]↩ [0,1]↩ [0,1]↩ \nExpected:      [0,1]↩ [1,2]↩ [0,1]↩')
    SubmissionResult(success=False, runtime=None, memory=None, runtime_percentile=None, memory_percentile=None, output='Wrong Answer\n\nCases passed:  38\nTotal cases:   63\nLast case:     [3,2,4]↩ 6\nOutput:        [0,1]\nExpected:      [1,2]\nStdout:')
    TestResult(success=False, runtime=0, output='Wrong Answer   Runtime: 0 ms\n\nYour input:    [2,7,11,15]↩ 9↩ [3,2,4]↩ 6↩ [3,3]↩ 6\nOutput:        [0,1]↩ [0,1]↩ [0,1]↩ \nExpected:      [0,1]↩ [1,2]↩ [0,1]↩')
    SubmissionResult(success=False, runtime=None, memory=None, runtime_percentile=None, memory_percentile=None, output='Wrong Answer\n\nCases passed:  38\nTotal cases:   63\nLast case:     [3,2,4]↩ 6\nOutput:        [0,1]\nExpected:      [1,2]\nStdout:')
"""