"""   Unique Paths ==> medium

There is a robot on an m x n grid. The robot is initially located at 
the top-left corner (i.e., grid[0][0]). The robot tries to move 
to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot 
can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible 
unique paths that the robot can take to reach the bottom-right 
corner.

The test cases are generated so that the answer will be less than 
or equal to 2 * 109.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

        Link : https://leetcode.com/problems/unique-paths/?envType=daily-question&envId=2023-09-03

""" 
# Solution

#   C(n,k) = n!/k!*(n-k)!   
#its enough to calculate C of m or n since there is binary choices

import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        return int(math.factorial(m+n-2)/(math.factorial(n-1)*math.factorial(m-1)))
        
m , n = 3,2  
m,n = 3 ,7  

# Create an instance of the Solution class
solution_instance = Solution()

# Call the mergeAlternately method with your word1 and word2
test = solution_instance.uniquePaths(m,n)

# Print the result
print(test)