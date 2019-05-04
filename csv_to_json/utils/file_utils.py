import csv
import json
import os


def _get_file_name_with_extension(file_name, extension):
    if ".{}".format(extension) not in file_name:
        file_name = "{}.{}".format(file_name, extension)

    return file_name


def _get_data_file_path(file_name):
    data_path = "data"
    path = "{}/{}".format(data_path, file_name)
    return os.path.abspath(path)


def _get_csv_file_as_dict_list(file_path):
    with open(file_path, encoding='utf-8-sig') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        return [dict(row) for row in csv_reader]


def read_csv_data(file_name):
    file_name = _get_file_name_with_extension(file_name, 'csv')
    return _get_csv_file_as_dict_list(_get_data_file_path(file_name))


def _save_dict_list_as_csv_file(dict_list, file_path):
    with open(file_path, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, dict_list[0].keys(), delimiter=',')
        writer.writeheader()
        for row in dict_list:
            writer.writerow(row)


def save_csv_data(dict_list, file_name):
    file_name = _get_file_name_with_extension(file_name, 'csv')
    _save_dict_list_as_csv_file(dict_list, _get_data_file_path(file_name))


def save_json(dict, file_name):
    file_name = _get_file_name_with_extension(file_name, 'json')
    json.dump(dict, open(_get_data_file_path(file_name), 'w'), sort_keys=True, indent=4)


def read_json(file_name):
    file_name = _get_file_name_with_extension(file_name, 'json')
    return json.load(open(_get_data_file_path(file_name), 'r'))


if __name__ == '__main__':
    test_data = read_csv_data("prior_course_grades_and_terms")
    print("joehoe", test_data)
