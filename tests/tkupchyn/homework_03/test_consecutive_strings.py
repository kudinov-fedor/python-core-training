import pytest
from tkupchyn.homework_03.consecutive_strings import consecutive_concatenation


@pytest.mark.parametrize("list_of_strings, k, expected_result",
                         [
                             (["tree", "foling", "trashy", "blue", "abcdef", "uvwxyz",
                               "hehhnns", "concatenate", "strings", "function", "Python"], 3,
                              "concatenatestringsfunction"),

                             (["interface", "is", "Up", "issue", "is", "consistent"], 2, "isconsistent"),

                             (["interface", "connectivity", "Up", "issue", "is", "consistent"], 3,
                              "interfaceconnectivityUp"),

                             (["After", "configuring", "failover"], 1, "configuring"),
                         ])
def test_consecutive_strings(list_of_strings, k, expected_result):
    assert consecutive_concatenation(list_of_strings, k) == expected_result
