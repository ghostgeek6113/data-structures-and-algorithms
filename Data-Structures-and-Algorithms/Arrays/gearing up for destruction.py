from fractions import Fraction

# impossible_results = [-1, -1]
# minimum_radius_for_gears_other_than_first = 1
# minimum_radius_for_first_gear = 2 * minimum_radius_for_gears_other_than_first
#
#
# def is_gear_solution_possible_for_peg_arrangement(first_gear_radius, pegs):
#     if first_gear_radius < minimum_radius_for_first_gear:
#         return False
#     current_gear_radius = first_gear_radius
#     for i in range(1, len(pegs)):
#         distance = pegs[i] - pegs[i - 1]
#         current_gear_radius = distance - current_gear_radius
#         if current_gear_radius < minimum_radius_for_gears_other_than_first:
#             return False
#     return True
#
#
# def is_even(number):
#     return number % 2 == 0
#
#
# def get_first_gear_radius(pegs):
#     sum_of_even_indexed_and_negative_of_odd_indexed_distances = 0
#     for i in range(len(pegs) - 1):
#         distance = pegs[i + 1] - pegs[i]
#         sum_of_even_indexed_and_negative_of_odd_indexed_distances += distance if is_even(i) else -1 * distance
#     return (2 / 3 if is_even(len(pegs)) else 2) * sum_of_even_indexed_and_negative_of_odd_indexed_distances
#
#
# def solution(pegs):
#     first_gear_radius = get_first_gear_radius(pegs)
#     if not is_gear_solution_possible_for_peg_arrangement(first_gear_radius, pegs):
#         return [-1, -1]
#
#     first_gear_radius_as_ratio = Fraction(str(first_gear_radius))
#     return first_gear_radius_as_ratio.numerator, first_gear_radius_as_ratio.denominator
#
#
# print(solution([4, 30, 50]))
# print(solution([4, 17, 50]))


def invert(matrix):
    inverse = [[Fraction(0) for col in range(len(matrix))] for row in range(len(matrix))]

    for i in range(len(matrix)):
        inverse[i][i] = Fraction(1)

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                if matrix[i][i] == 0:
                    return False
                ratio = matrix[j][i] / matrix[i][i]
                for k in range(len(matrix)):
                    inverse[j][k] = inverse[j][k] - ratio * inverse[i][k]
                    matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

    for i in range(len(matrix)):
        a = matrix[i][i]
        if a == 0:
            return False
        for j in range(len(matrix)):
            inverse[i][j] = inverse[i][j] / a
    return inverse


def solution(pegs):
    if len(pegs) < 2:
        return [-1, -1]

    if len(pegs) == 2:
        x = (Fraction(pegs[1] - pegs[0]) / Fraction(3)) * Fraction(2)
        if (x.numerator < 1) or (x.numerator < x.denominator):
            return [-1, -1]

        return [x.numerator, x.denominator]

    matrix = []
    row_num = 0
    deltas = []
    for locs in pegs:
        deltas.append(Fraction(pegs[row_num + 1] - pegs[row_num]))

        if row_num == 0:
            row = [Fraction(2), Fraction(1)] + [Fraction(0)] * (len(pegs) - 3)
            matrix.append(row)
        elif row_num == len(pegs) - 2:
            row = [Fraction(1)] + [Fraction(0)] * (len(pegs) - 3) + [Fraction(1)]
            matrix.append(row)
            break
        else:
            row = [Fraction(0)] * row_num + [Fraction(1), Fraction(1)] + [Fraction(0)] * (len(pegs) - row_num - 3)
            matrix.append(row)
        row_num = row_num + 1

    inverse = invert(matrix)
    if not inverse:
        return [-1, -1]

    # Validate all gears
    for i in range(1, len(pegs) - 1):
        y = Fraction(0)
        for j in range(len(pegs) - 1):
            y = y + inverse[i][j] * deltas[j]
        if (y.numerator < 1) or (y.numerator < y.denominator):
            return [-1, -1]

    x = Fraction(0)
    for i in range(len(pegs) - 1):
        x = x + inverse[0][i] * deltas[i]

    x = x * Fraction(2)

    if (x.numerator < 1) or (x.numerator < x.denominator):
        return [-1, -1]

    return [x.numerator, x.denominator]


print(solution([4, 30, 50]))
print(solution([4, 17, 50]))
