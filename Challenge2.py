def solution(A):
  """
  This function finds the maximum sum of two numbers in the array A whose digits add up to the same sum.

  Args:
      A: A list of integers.

  Returns:
      The maximum sum of two such numbers, or -1 if none are found.
  """
  # Create a dictionary to store the sum of digits for each number.
  digit_sums = {}
  max_sum = -1
  
  for num in A:
    # Calculate the sum of digits for the current number.
    digit_sum = sum(int(d) for d in str(num))
    
    # Check if there's a previous number with the same digit sum.
    if digit_sum in digit_sums:
      # Update max_sum if the current pair has a larger sum.
      max_sum = max(max_sum, num + digit_sums[digit_sum])
    else:
      # Add the current number and its digit sum to the dictionary.
      digit_sums[digit_sum] = num
  
  return max_sum

# Example 1
A = [51, 71, 17, 42]
result = solution(A)
print("Example 1: Maximum sum =", result)  # Output: Example 1: Maximum sum = 93

# Example 2
A = [42, 33, 60]
result = solution(A)
print("Example 2: Maximum sum =", result)  # Output: Example 2: Maximum sum = 102

# Example 3
A = [51, 32, 43]
result = solution(A)
print("Example 3: Maximum sum =", result)  # Output: Example 3: Maximum sum = -1
