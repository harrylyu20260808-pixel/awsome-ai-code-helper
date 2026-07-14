"""
Comprehensive Calculator Application
Supports basic arithmetic, scientific functions, and more
"""

class Calculator:
    """Basic Calculator"""

    def add(self, a, b):
        """Add two numbers"""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a"""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers"""
        return a * b

    def divide(self, a, b):
        """Divide a by b"""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        """Calculate a to the power of b"""
        return a ** b

    def square_root(self, a):
        """Calculate square root"""
        if a < 0:
            raise ValueError("Cannot calculate square root of negative number")
        return a ** 0.5

    def absolute(self, a):
        """Get absolute value"""
        return abs(a)

    def percentage(self, value, percent):
        """Calculate percentage of a value"""
        return (percent / 100) * value


class ScientificCalculator(Calculator):
    """Scientific Calculator with advanced functions"""

    def sine(self, angle_degrees):
        """Calculate sine in degrees"""
        import math
        return math.sin(math.radians(angle_degrees))

    def cosine(self, angle_degrees):
        """Calculate cosine in degrees"""
        import math
        return math.cos(math.radians(angle_degrees))

    def tangent(self, angle_degrees):
        """Calculate tangent in degrees"""
        import math
        return math.tan(math.radians(angle_degrees))

    def log(self, base, x):
        """Calculate logarithm"""
        if x <= 0 or base <= 0:
            raise ValueError("Invalid logarithm parameters")
        return math.log(x, base)

    def log10(self, x):
        """Calculate base-10 logarithm"""
        if x <= 0:
            raise ValueError("Cannot calculate log of non-positive number")
        return math.log10(x)

    def natural_log(self, x):
        """Calculate natural logarithm (ln)"""
        if x <= 0:
            raise ValueError("Cannot calculate ln of non-positive number")
        return math.log(x)

    def factorial(self, n):
        """Calculate factorial"""
        if n < 0:
            raise ValueError("Cannot calculate factorial of negative number")
        if n == 0 or n == 1:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def combinations(self, n, k):
        """Calculate combinations (n choose k)"""
        from math import factorial
        if n < 0 or k < 0 or n < k:
            raise ValueError("Invalid combination parameters")
        return factorial(n) // (factorial(k) * factorial(n - k))

    def permutations(self, n, k):
        """Calculate permutations (nPk)"""
        from math import factorial
        if n < 0 or k < 0 or n < k:
            raise ValueError("Invalid permutation parameters")
        return factorial(n) // factorial(n - k)

    def logarithm(self, x, base=10):
        """Calculate logarithm with specified base"""
        return self.log(base, x)

    def antilog(self, x, base=10):
        """Calculate antilogarithm (base^x)"""
        return base ** x

    def round_to_decimal(self, number, decimals=2):
        """Round number to specified decimal places"""
        return round(number, decimals)

    def floor(self, number):
        """Round down to nearest integer"""
        return math.floor(number)

    def ceiling(self, number):
        """Round up to nearest integer"""
        return math.ceil(number)


class ConverterCalculator:
    """Unit Converter Calculator"""

    # Length conversions
    LENGTH_UNITS = {
        'millimeter': 0.001,
        'centimeter': 0.01,
        'meter': 1,
        'kilometer': 1000,
        'inch': 0.0254,
        'foot': 0.3048,
        'yard': 0.9144,
        'mile': 1609.344
    }

    # Weight conversions
    WEIGHT_UNITS = {
        'milligram': 0.000001,
        'gram': 0.001,
        'kilogram': 1,
        'ton': 1000,
        'ounce': 0.0283495,
        'pound': 0.453592
    }

    # Temperature conversions
    TEMP_FORMULAS = {
        'celsius_fahrenheit': lambda c: (c * 9/5) + 32,
        'fahrenheit_celsius': lambda f: (f - 32) * 5/9,
        'celsius_kelvin': lambda c: c + 273.15,
        'kelvin_celsius': lambda k: k - 273.15,
        'fahrenheit_kelvin': lambda f: (f - 32) * 5/9 + 273.15,
        'kelvin_fahrenheit': lambda k: (k - 273.15) * 9/5 + 32
    }

    def convert_length(self, value, from_unit, to_unit):
        """Convert between length units"""
        from_factor = self.LENGTH_UNITS[from_unit]
        to_factor = self.LENGTH_UNITS[to_unit]

        in_meters = value * from_factor
        result = in_meters / to_factor
        return result

    def convert_weight(self, value, from_unit, to_unit):
        """Convert between weight units"""
        from_factor = self.WEIGHT_UNITS[from_unit]
        to_factor = self.WEIGHT_UNITS[to_unit]

        in_kilograms = value * from_factor
        result = in_kilograms / to_factor
        return result

    def convert_temperature(self, value, from_unit, to_unit):
        """Convert between temperature units"""
        formula = self.TEMP_FORMULAS[f"{from_unit}_to_{to_unit}"]
        return formula(value)

    def convert_currency(self, amount, from_currency, to_currency, rates):
        """Convert between currencies"""
        amount_in_usd = amount / rates[from_currency]
        result = amount_in_usd * rates[to_currency]
        return result


class FinancialCalculator:
    """Financial Calculator"""

    def calculate_simple_interest(self, principal, rate, time):
        """Calculate simple interest"""
        return (principal * rate * time) / 100

    def calculate_compound_interest(self, principal, rate, time, compound_freq=12):
        """Calculate compound interest"""
        amount = principal * (1 + rate / 100) ** (compound_freq * time)
        return amount - principal

    def calculate_loan_payment(self, principal, annual_rate, years):
        """Calculate monthly loan payment"""
        monthly_rate = annual_rate / 100 / 12
        num_payments = years * 12
        payment = (principal * monthly_rate * (1 + monthly_rate) ** num_payments) / ((1 + monthly_rate) ** num_payments - 1)
        return payment

    def calculate_mortgage(self, house_price, down_payment, annual_rate, years):
        """Calculate monthly mortgage payment"""
        loan_amount = house_price - down_payment
        return self.calculate_loan_payment(loan_amount, annual_rate, years)

    def calculate_investment_growth(self, initial, monthly_contrib, annual_return, years):
        """Calculate investment growth"""
        monthly_rate = annual_return / 100 / 12
        num_months = years * 12

        # Future value of initial investment
        fv_initial = initial * ((1 + monthly_rate) ** num_months)

        # Future value of monthly contributions
        fv_contributions = monthly_contrib * (((1 + monthly_rate) ** num_months - 1) / monthly_rate)

        return fv_initial + fv_contributions

    def calculate_roi(self, cost, revenue):
        """Calculate Return on Investment"""
        return ((revenue - cost) / cost) * 100

    def calculate_break_even(self, fixed_cost, variable_cost_per_unit, price_per_unit):
        """Calculate break-even point"""
        if price_per_unit <= variable_cost_per_unit:
            return float('inf')
        return fixed_cost / (price_per_unit - variable_cost_per_unit)


# Usage examples
if __name__ == "__main__":
    # Basic Calculator
    calc = Calculator()
    print("Basic Calculator")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"4^2 = {calc.power(4, 2)}")
    print(f"√25 = {calc.square_root(25)}")
    print(f"| -10 | = {calc.absolute(-10)}")
    print(f"50% of 200 = {calc.percentage(200, 50)}")

    # Scientific Calculator
    sci_calc = ScientificCalculator()
    print("\nScientific Calculator")
    print(f"sin(30°) = {sci_calc.sine(30):.4f}")
    print(f"cos(60°) = {sci_calc.cosine(60):.4f}")
    print(f"tan(45°) = {sci_calc.tangent(45):.4f}")
    print(f"log10(1000) = {sci_calc.log10(1000):.4f}")
    print(f"ln(100) = {sci_calc.natural_log(100):.4f}")
    print(f"factorial(5) = {sci_calc.factorial(5)}")
    print(f"10 choose 3 = {sci_calc.combinations(10, 3)}")
    print(f"5! = {sci_calc.factorial(5)}")

    # Converter Calculator
    converter = ConverterCalculator()
    print("\nUnit Converter")
    print(f"100 meters to feet = {converter.convert_length(100, 'meter', 'foot'):.2f} feet")
    print(f"10 kilometers to miles = {converter.convert_length(10, 'kilometer', 'mile'):.2f} miles")
    print(f"5 pounds to kilograms = {converter.convert_weight(5, 'pound', 'kilogram'):.2f} kg")
    print(f"0°C to Fahrenheit = {converter.convert_temperature(0, 'celsius', 'fahrenheit'):.2f}°F")

    # Financial Calculator
    fin_calc = FinancialCalculator()
    print("\nFinancial Calculator")
    print(f"Simple interest on $1000 at 5% for 2 years = ${fin_calc.calculate_simple_interest(1000, 5, 2):.2f}")
    print(f"Mortgage payment on $200,000 at 4% for 30 years = ${fin_calc.calculate_mortgage(200000, 40000, 4, 30):.2f}/month")
    print(f"Initial $1000 + $100/month at 8% for 10 years = ${fin_calc.calculate_investment_growth(1000, 100, 8, 10):.2f}")

    print("\n✨ Calculator completed!")
