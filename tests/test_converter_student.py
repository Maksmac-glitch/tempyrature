import pytest

from tempyrature.tempyrature import Converter


# 1. C F: точка -40 
def test_celsius_fahrenheit_round_trip_minus_40():

    celsius = -40.0

    fahrenheit = Converter.celsius2fahrenheit(celsius)
    back_to_celsius = Converter.fahrenheit2celsius(fahrenheit)

    assert fahrenheit == pytest.approx(-40.0)
    assert back_to_celsius == pytest.approx(celsius)


# 2. C K: 10.5
def test_celsius_kelvin_round_trip():

    celsius = 10.5

    kelvin = Converter.celsius2kelvin(celsius)
    back_to_celsius = Converter.kelvin2celsius(kelvin)

    assert kelvin == pytest.approx(283.65)
    assert back_to_celsius == pytest.approx(celsius)


# 3. K R: 313.15
def test_kelvin_rankine_round_trip():

    kelvin = 313.15

    rankine = Converter.kelvin2rankine(kelvin)
    back_to_kelvin = Converter.rankine2kelvin(rankine)

    assert rankine == pytest.approx(563.67, rel=1e-12)
    assert back_to_kelvin == pytest.approx(kelvin)


# 4. C R: Rankine
def test_celsius_rankine_round_trip():

    celsius = 10.0

    rankine = Converter.celsius2rankine(celsius)
    back_to_celsius = Converter.rankine2celsius(rankine)

    assert rankine == pytest.approx(509.67, rel=1e-12)
    assert back_to_celsius == pytest.approx(celsius)


# 5. F K: 80 F
def test_fahrenheit_kelvin_round_trip():

    fahrenheit = 80.0

    kelvin = Converter.fahrenheit2kelvin(fahrenheit)
    back_to_fahrenheit = Converter.kelvin2fahrenheit(kelvin)

    assert kelvin == pytest.approx(299.81666666666666)
    assert back_to_fahrenheit == pytest.approx(fahrenheit)


# 6. F R: 104 F
def test_fahrenheit_rankine_round_trip():

    fahrenheit = 104.0

    rankine = Converter.fahrenheit2rankine(fahrenheit)
    back_to_fahrenheit = Converter.rankine2fahrenheit(rankine)

    assert rankine == pytest.approx(563.6700000000001)
    assert back_to_fahrenheit == pytest.approx(fahrenheit)


# 7. абсолютный ноль
def test_absolute_zero_celsius_kelvin():

    celsius = -273.15

    kelvin = Converter.celsius2kelvin(celsius)
    back_to_celsius = Converter.kelvin2celsius(kelvin)

    assert kelvin == pytest.approx(0.0)
    assert back_to_celsius == pytest.approx(celsius)


# 8. 0 и 100
def test_celsius_to_fahrenheit_water_points():

    freezing = 0.0
    boiling = 100.0

    freezing_f = Converter.celsius2fahrenheit(freezing)
    boiling_f = Converter.celsius2fahrenheit(boiling)

    assert freezing_f == pytest.approx(32.0)
    assert boiling_f == pytest.approx(212.0)
