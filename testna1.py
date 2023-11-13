from collections import deque

def maxSlidingWindow(nums, k):
    """testna koda od chatGPT"""
    if not nums:
        return []

    max_values = []
    max_deque = deque()

    for i in range(len(nums)):
        # Remove elements that are out of the current window
        while max_deque and max_deque[0] < i - k + 1:
            max_deque.popleft()

        # Remove elements that are less than the current element
        while max_deque and nums[i] > nums[max_deque[-1]]:
            max_deque.pop()

        # Add the current element to the deque
        max_deque.append(i)

        # Add the maximum element in the current window to the result
        if i >= k - 1:
            max_values.append(nums[max_deque[0]])

    return max_values

#print(maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))

