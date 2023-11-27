import pytest
import json
import pandas as pd

from app.model_adapter import ModelAdapter

model_path = "./model"


def test_first_session_successful():
    fname = "./tests/resources/provided_input/new_session.json"
    with open(fname, "r") as file:
        new_session_dict = json.load(file)
        output_dict = ModelAdapter(model_path).process_session(new_session_dict)
    with open("./tests/resources/expected_output/new_session.json", "r") as file:
        expected_dict = json.load(file)

    actual_series = pd.Series(output_dict)
    expected_series = pd.Series(expected_dict)
    print(actual_series)
    print(expected_series)
    pd.testing.assert_series_equal(actual_series, expected_series)


def test_middle_session_successful():
    fname = "./tests/resources/provided_input/middle_session.json"
    with open(fname, "r") as file:
        new_session_dict = json.load(file)
        output_dict = ModelAdapter(model_path).process_session(new_session_dict)
    with open("./tests/resources/expected_output/middle_session.json", "r") as file:
        expected_dict = json.load(file)

    actual_series = pd.Series(output_dict)
    expected_series = pd.Series(expected_dict)
    print(actual_series)
    print(expected_series)
    pd.testing.assert_series_equal(actual_series, expected_series)


def test_last_session_successful():
    fname = "./tests/resources/provided_input/end_session.json"
    with open(fname, "r") as file:
        new_session_dict = json.load(file)
        output_dict = ModelAdapter(model_path).process_session(new_session_dict)
    with open("./tests/resources/expected_output/end_session.json", "r") as file:
        expected_dict = json.load(file)

    actual_series = pd.Series(output_dict)
    expected_series = pd.Series(expected_dict)
    print(actual_series)
    print(expected_series)
    pd.testing.assert_series_equal(actual_series, expected_series)