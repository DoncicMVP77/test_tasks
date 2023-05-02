import json

from requests.exceptions import HTTPError

import requests

from collections import Counter


def _get_page_response_text(url: str) -> str:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as err:
        print(err)
    else:
        return response.text


def _count_number_appears_element_in_page(html: str) -> dict[str, int]:
    count_elements = Counter(html)

    return dict(count_elements)


def _write_dict_to_file(file_name: str, count_number_appears_element_dict: dict) -> None:
    with open(file_name, mode='w') as f:
        f.seek(0)
        f.write(json.dumps(count_number_appears_element_dict))


def handle() -> None:
    url = "https://www.python.org"

    html = _get_page_response_text(url)

    count_dict = _count_number_appears_element_in_page(html)

    _write_dict_to_file('readme.md', count_dict)


if __name__ == '__main__':
    handle()
