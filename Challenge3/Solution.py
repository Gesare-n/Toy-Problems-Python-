#Function solution (N)aims to generate a string of length N
#The string should contain as many different lowercase lettera (a to z)as possible
#Each letter should appear an equal number of times within the string 
#The function should efficiently handle input values within the range of 1 to 200000
def solution(N):
    # If the number of letters needed is a multiple of 3
    if N % 3 == 0:
        # Return a string of 3 lowercase letters ('a', 'b', 'c') repeated N // 3 times
        return ''.join(chr(i) for i in range(ord('a'), ord('d') + 1)) * (N // 3)
    
    # If the number of letters needed is greater than 3
    elif N > 3:
        # Return a string of 3 lowercase letters ('a', 'b', 'c') repeated N // 3 - 1 times,
        # followed by a string of N % 3 lowercase letters
        return ''.join(chr(i) for i in range(ord('a'), ord('d') + 1)) * (N // 3 - 1) + ''.join(chr(i) for i in range(ord('a'), ord('a') + N % 3))
    
    # If the number of letters needed is less than or equal to 3
    else:
        # Return a string of N lowercase letters ('a', 'b', 'c')
        return ''.join(chr(i) for i in range(ord('a'), ord('a') + N))
