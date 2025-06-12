from mi_conversor import celsius_a_fahrenheit, fahrenheit_a_celsius

def test_celsius_a_fahrenheit():
    assert celsius_a_fahrenheit(0) == 32

def test_fahreinheit_a_celsius():
    assert fahrenheit_a_celsius(32) == 0
