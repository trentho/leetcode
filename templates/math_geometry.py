from __future__ import annotations


def rotate_matrix_90_clockwise(matrix: list[list[int]]) -> None:
    """In-place rotate n x n matrix."""
    n = len(matrix)
    matrix.reverse()
    for r in range(n):
        for c in range(r + 1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)
