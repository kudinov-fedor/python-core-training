import os

from api_testing.helpers.api_client import ApiClient
from api_testing.helpers.constants import SAMPLES_PATH


def test_attachment(client: ApiClient, card_id, tmp_dir):

    file_name = "sample_data.txt"
    path = os.path.join(SAMPLES_PATH, file_name)
    res = client.create_attachment(card_id,
                                   path=path,
                                   name=file_name,
                                   set_cover=False)

    client.download_attachment(res["url"], os.path.join(tmp_dir, res["name"]))

    with open(os.path.join(tmp_dir, file_name)) as file:
        assert file.read() == "Hello World!"
