def solution(A):
    N = len(A)
    target_bricks = 10
    total_bricks = sum(A)
    target_per_box = total_bricks // N

    if total_bricks % N != 0:
        return -1

    moves = 0

    for bricks in A:
        moves += abs(bricks - target_per_box)
    return moves // 2 

# Examples:
A1 = [7, 15, 10, 8]
result1 = solution(A1)
print(f"Example 1: {result1}")

A2 = [11, 10, 8, 12, 8, 10, 11]
result2 = solution(A2)
print(f"Example 2: {result2}")

A3 = [7, 14, 10]
result3 = solution(A3)
print(f"Example 3: {result3}")