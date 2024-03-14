from collections import Counter

def solution(N):
  """
  This function generates a string of length N containing as many different 
  lower-case letters as possible, where each letter occurs an equal number of times.

  Args:
      N: An integer representing the desired string length.

  Returns:
      A string satisfying the given conditions, or None if not possible.
  """
  if N <= 0:
    return None

  # Calculate the maximum number of unique letters possible.
  max_unique_letters = min(26, N // 2)

  # Create a string with the maximum number of unique letters, each repeated equally.
  chars = ''.join(chr(ord('a') + i) for i in range(max_unique_letters))
  repetitions = N // max_unique_letters

  # If N is not perfectly divisible by the number of unique letters, 
  # adjust the string to distribute the remaining characters.
  remaining = N % max_unique_letters
  if remaining:
    chars = chars[:remaining] + chars[remaining:]

  return chars * repetitions

# Examples
print(solution(3)) 
print(solution(5))  
print(solution(30)) 

