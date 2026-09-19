from pathlib import Path

import pytest
import yaml

from bengali_romanizer import romanize


def load_test_cases() -> dict[str, list[dict[str, str]]]:
    with Path(__file__).with_name("test_cases.yaml").open(encoding="utf-8") as stream:
        cases: dict[str, list[dict[str, str]]] = yaml.safe_load(stream)
    return cases


@pytest.mark.parametrize(
    "test_case", [case for group in load_test_cases().values() for case in group]
)
def test_romanization(test_case: dict[str, str]) -> None:
    assert romanize(test_case["input"]) == test_case["expected"]
