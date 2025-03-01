from tkupchyn.homework_03.common_words import find_common_words, common_words_alternative_solution

first_string = "test,Cisco,office,coffee,good,choice"
second_string = "test,Cisco,office,coffee,not,weather"
expected_result = 'Cisco,coffee,office,test'


def test_find_common_words():
    assert find_common_words(first_string, second_string) == expected_result


def test_common_words_alternative_solution():
    assert common_words_alternative_solution(first_string, second_string) == expected_result
