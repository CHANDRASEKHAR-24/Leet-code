# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         i = 1
#         result =sum(nums[:k])/k
#         a =sum(nums[i:k])
#         for j in range (k,len(nums)):
#             a+=nums[j]
#             if a/k > result:
#                 result =  a/k
#             a-=nums[i]
#             i+=1


#         return result 

# ANOTHER WAY

class Solution:
    def findMaxAverage(self,nums:list[int],k:int)->float:

        # Calculate the sum of the first 'k' elements
        current_sum = sum(nums[:k])
        max_avg = current_sum/k

 # Slide the window over the rest of the list
        for i in range (k,len(nums)):
             # Update the window sum by removing the leftmost and adding the new element
            current_sum += nums[i]-nums[i-k]
             # Update max average if current window's average is greater
            max_avg=max(max_avg,current_sum/k)
        return  max_avg