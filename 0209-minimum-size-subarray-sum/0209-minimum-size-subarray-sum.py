class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left , current_sum,min_length = 0,0,float('inf')

        for right in range(len(nums)):
            current_sum+= nums[right]

            while current_sum>=target:
                min_length = min(min_length,right-left+1)
                current_sum-=nums[left]
                left +=1

        return 0 if min_length == float('inf') else min_length

#  EXPLANATION 


  # Start of the window
  # Current sum of the window
  # Minimum length found so far (initialized to infinity)

   # Move the right end of the window
   # Add the current number to the sum


            # Shrink the window from the left while the sum is still enough

                # Update the minimum length
                
                # Remove the leftmost element from the window
            
                # Move left pointer forward
                

        # If we found no valid window, return 0; else return the minimum length
        