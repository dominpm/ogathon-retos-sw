from typing import List
import itertools
    
def minimal_moves(matrix: List[List[int]]) -> int:
    n = len(matrix)
    if n == 0 or any(len(row) != n for row in matrix):
        raise ValueError("La matriz debe ser cuadrada (n contenedores × n tipos).")

    total = sum(sum(row) for row in matrix)
    best_correct = 0

    for perm in itertools.permutations(range(n)):      # todas las asignaciones posibles
        correct = sum(matrix[i][perm[i]] for i in range(n))
        best_correct = max(best_correct, correct)

    return total - best_correct                        # movimientos mínimos