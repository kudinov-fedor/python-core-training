from opary.task_backward_string import backward_string


def test_backward_string():
    assert backward_string('banana') == 'ananab'
    assert backward_string('06101991') == '19910160'
    assert backward_string('level') == 'level'