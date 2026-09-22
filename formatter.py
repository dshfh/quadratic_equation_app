def format_number(number):
    if abs(number) < 1e-10:
        number = 0

    return f"{number:.5f}".rstrip("0").rstrip(".")


def create_solution_text(a, b, c, result):
    a_text = format_number(a)
    b_text = format_number(b)
    c_text = format_number(c)

    d_text = format_number(
        result["discriminant"]
    )

    text = (
        "STEP-BY-STEP SOLUTION\n"
        "======================\n\n"

        f"Given equation:\n"
        f"{a_text}x² + ({b_text})x + ({c_text}) = 0\n\n"

        "Step 1: Identify the coefficients\n\n"
        f"a = {a_text}\n"
        f"b = {b_text}\n"
        f"c = {c_text}\n\n"

        "Step 2: Calculate the discriminant\n\n"
        "D = b² - 4ac\n"
        f"D = ({b_text})² - "
        f"4 × ({a_text}) × ({c_text})\n"
        f"D = {d_text}\n\n"
    )

    if result["roots_count"] == 2:

        x1 = format_number(result["x1"])
        x2 = format_number(result["x2"])

        text += (
            "Step 3: Determine the number of roots\n\n"
            f"Since D = {d_text} > 0, "
            "the equation has two different real roots.\n\n"

            "Step 4: Calculate the roots\n\n"
            "x₁ = (-b + √D) / (2a)\n"
            f"x₁ = {x1}\n\n"

            "x₂ = (-b - √D) / (2a)\n"
            f"x₂ = {x2}\n\n"

            "FINAL ANSWER:\n"
            f"x₁ = {x1}\n"
            f"x₂ = {x2}"
        )

    elif result["roots_count"] == 1:

        x = format_number(result["x"])

        text += (
            "Step 3: Determine the number of roots\n\n"
            f"Since D = {d_text}, "
            "the equation has one real root.\n\n"

            "Step 4: Calculate the root\n\n"
            "x = -b / (2a)\n"
            f"x = {x}\n\n"

            "FINAL ANSWER:\n"
            f"x = {x}"
        )

    else:

        text += (
            "Step 3: Determine the number of roots\n\n"
            f"Since D = {d_text} < 0, "
            "the equation has no real roots.\n\n"

            "The square root of a negative number "
            "is not a real number.\n\n"

            "FINAL ANSWER:\n"
            "No real roots."
        )

    return text