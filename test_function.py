from function import number_to_month, validate_number
import pytest


@pytest.mark.code
def test_january():
    input = 1
    expected_result = "january"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


def test_february():
    input = 2
    expected_result = "february"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


def test_march():
    input = 3
    expected_result = "march"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


def test_april():
    input = 4
    expected_result = "april"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


def test_may():
    input = 5
    expected_result = "may"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


def test_june():
    input = 6
    expected_result = "june"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


def test_july():
    input = 7
    expected_result = "july"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


def test_august():
    input = 8
    expected_result = "august"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


def test_september():
    input = 9
    expected_result = "september"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


def test_october():
    input = 10
    expected_result = "october"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


def test_november():
    input = 11
    expected_result = "november"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


def test_december():
    input = 12
    expected_result = "december"
    actual_result = number_to_month(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_out_of_range_input_0():
    input = 0
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_out_of_range_input_13():
    input = 13
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_out_of_range_input_ng10():
    input = -10
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_out_of_range_input_22():
    input = 22
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_out_of_range_input_1_p_1():
    input = 1.1
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_out_of_range_input_13_p_1():
    input = 13.1
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_out_of_range_input_A():
    input = "a"
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_out_of_range_input_shap():
    input = "#"
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_out_of_range_input_negative():
    input = -0.5
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_out_of_range_input_negative1_5():
    input = -1.5
    expected_result = "out of range"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_out_of_range_input_1_5():
    input = 1.5
    expected_result = "input integer"
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_input_12():
    input = 12
    expected_result = 12
    actual_result = validate_number(input)
    assert expected_result == actual_result


@pytest.mark.validate
def test_input_1():
    input = 1
    expected_result = 1
    actual_result = validate_number(input)
    assert expected_result == actual_result
