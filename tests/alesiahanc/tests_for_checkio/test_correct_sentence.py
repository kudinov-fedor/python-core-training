from alesiahanc.ch_correct_sentence import correct_sentence


def test_correct_sentence():
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("greetings, friends.") == "Greetings, friends."
