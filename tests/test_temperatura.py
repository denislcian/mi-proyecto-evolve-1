from src.conversores.temperatura import celsius_a_fahrenheit

def test_celsius_a_fahrenheit():
    assert celsius_a_fahrenheit(0) == 32
    assert celsius_a_fahrenheit(100) == 212
