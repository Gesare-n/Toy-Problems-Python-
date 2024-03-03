#Function solution(A) needs to find the maximum sum of two numbers in array A
#If the pair does not exist , return -1

def solution(A):
    N = len(A)
    if N < 2:
        return -1  # If there are less than two numbers, there can't be a pair, so return -1
    
    digit_sums = set()  # Set to store unique digit sums encountered
    max_sum = 0  # Variable to track the maximum sum of two numbers with equal digit sums
    
    # Iterate through the numbers in the array
    for num in A:
        # Calculate the digit sum of the current number
        digit_sum = sum(int(digit) for digit in str(num))
        
        # If this digit sum has been seen before
        if digit_sum in digit_sums:
            # Find the previous number with the same digit sum and update max_sum if needed
            max_sum = max(max_sum, num + A[A.index(num) - 1])
        else:
            # Add the digit sum to the set
            digit_sums.add(digit_sum)
        
    # If max_sum remains 0, it means no pair with equal digit sums was found
    if max_sum == 0:
        return -1  
    
    # Return the maximum sum of two numbers with equal digit sums
    return max_sum  
