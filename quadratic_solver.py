import math


def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError(
            "Coefficient 'a' cannot be zero."
        )

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        sqrt_d = math.sqrt(discriminant)

        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)

        return {
            "discriminant": discriminant,
            "roots_count": 2,
            "x1": x1,
            "x2": x2
        }

    if discriminant == 0:
        x = -b / (2 * a)

        return {
            "discriminant": discriminant,
            "roots_count": 1,
            "x": x
        }

    return {
        "discriminant": discriminant,
        "roots_count": 0
    }