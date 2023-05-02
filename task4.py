import os
import json
from datetime import datetime


def _read_json_file_to_dict(json_file_name: json) -> dict:
    with open(
        file=f"{os.path.join(os.path.dirname(__file__), json_file_name)}",
        mode='r'
    ) as outfile:

        temp_dict = json.loads(outfile.read())
        return temp_dict


def _change_datetime_in_update_field(temp_dict: dict) -> dict:
    for item in temp_dict:
        if 'updated' in item:
            item['updated'] = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    return temp_dict


def _write_dict_to_json_file(file_name: str, temp_dict: dict) -> None:

    with open(
        file=f"{os.path.join(os.path.dirname(__file__), file_name)}",
        mode='w'
    ) as f:
        json.dumps(temp_dict)


def change_json_updated_field_value_to_now_datetime_in_iso_8601_format(filename: str):
    temp_dict = _read_json_file_to_dict(filename)

    updated_temp_dict = _change_datetime_in_update_field(temp_dict)

    _write_dict_to_json_file(filename, updated_temp_dict)


if __name__ == '__main__':
    change_json_updated_field_value_to_now_datetime_in_iso_8601_format('updated_field.json')
