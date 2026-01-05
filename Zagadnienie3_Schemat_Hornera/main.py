def horner(coeffs, x):
    result = coeffs[0]
    for i in range(1, len(coeffs)):
        result = result * x + coeffs[i]
    return result


if __name__ == "__main__":
    # 2x^3 - 3x^2 + 4x - 5
    coefficients = [2, -3, 4, -5]
    x = 3
    print(horner(coefficients, x))
