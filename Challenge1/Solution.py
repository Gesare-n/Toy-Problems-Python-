#A list of numbers representing the bricks in each box
#Redistribute the bricks so that each box contains exctly 10 bricks
#solution A should determine the minimum number of moves needed to reach  that arrangement
#If it is not possible return -1

def solution(A):
    N = len(A)  # Get the number of boxes
    target = 10  # The target number of bricks in each box
    min_moves = float('inf')  # Initialize the minimum number of moves to infinity
    prefix_sum = [0] * (N + 1)  # Initialize a prefix sum array
    suffix_sum = [0] * (N + 1)  # Initialize a suffix sum array
    
    # Calculate prefix sum and suffix sum
    for i in range(N):
        prefix_sum[i + 1] = prefix_sum[i] + A[i]  # Calculate the prefix sum
        suffix_sum[N - i] = suffix_sum[N - i - 1] + A[N - i - 1]  # Calculate the suffix sum
    
    # Iterate over each box to find the minimum number of moves needed
    for i in range(N):
        # Check if it's possible to end up with exactly 10 bricks in every box
        if prefix_sum[i] + suffix_sum[i + 1] < target * (N - i):
            continue
        # Check if it's not possible to end up with exactly 10 bricks in every box
        if prefix_sum[i] + suffix_sum[i + 1] > target * (N - i) + N - 1:
            return -1
        # Calculate the minimum number of moves needed to end up with exactly 10 bricks in every box
        moves = (prefix_sum[i] + suffix_sum[i + 1] - target * (N - i)) // 2
        min_moves = min(min_moves, moves)
    
    return min_moves if min_moves != float('inf') else -1  # Return the minimum number of moves or -1 if it's not possible to end up with exactly 10 bricks in every box
