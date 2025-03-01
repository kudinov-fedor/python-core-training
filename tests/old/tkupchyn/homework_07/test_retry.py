from tkupchyn.homework_07.retrying import unstable_function


def test_retry_decorator(mocker):
    mock_random = mocker.patch('random.random', side_effect=[0, 0.49, 0.51])
    result = unstable_function()

    assert result == 0.51
    assert mock_random.call_count == 3
