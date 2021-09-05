import decimal

def conversion(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5/9


def better_conversion(fahrenheit: decimal.Decimal) -> decimal.Decimal:
    return (fahrenheit - 32) * 5/9


if __name__ == '__main__':
    print(conversion(99.8))
    print(f"Better conversion\n{better_conversion(decimal.Decimal(99.8))}")
