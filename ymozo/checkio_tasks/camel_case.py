import re


def from_camel_case(name: str) -> str:
    splitted_list = (re.split('(?<=.)(?=[A-Z])', name))
    converted_list = " ".join(splitted_list).replace(" ", "_").lower()

    return converted_list


if __name__ == "__main__":
    print("Example:")
    print(from_camel_case("MyFunctionName"))

    # These "asserts" are used for self-checking
    assert from_camel_case("MyFunctionName") == "my_function_name"
    assert from_camel_case("IPhone") == "i_phone"
    assert from_camel_case('ThisFunctionIsEmpty') == 'this_function_is_empty'
    assert from_camel_case('Name') == 'name'
    assert from_camel_case('ThisIsReallyVeryLongString') == 'this_is_really_very_long_string'

    print("The mission is done! Click 'Check Solution' to earn rewards!")
