from api_testing.helpers.api_client import ApiClient


def test_attachment(client: ApiClient, tmp_dir):

    host = "https://trello.com"
    card_id = "613e0faf5395da0d2dcec0ae"
    attachment_id = "613e3fc2e57af26416fa080c"
    file_name = "1faf9268de7021ecc1d8c598204a7019.jpg"
    path = "{}/1/cards/{}/attachments/{}/download/{}".format(host, card_id, attachment_id, file_name)

    client.download_attachment(path, tmp_dir + "/some_attach.jpg")
    client.create_attachment("613e0faf5395da0d2dcec0ae",
                             path=tmp_dir + "/some_attach.jpg",
                             name="new_5",
                             set_cover=False)
