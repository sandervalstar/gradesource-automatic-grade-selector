from csv_to_json.utils import file_utils as fu

# NOTE: create a "data" directory
FILE_NAME = 'example_data'

if __name__ == '__main__':
    print("grading...")

    data = fu.read_csv_data(FILE_NAME)
    print(data)

    result = dict()
    for s in data:
        # NOTE: replace these column names with the corresponding column names in your own CSV
        result[s['Student ID']] = s['Letter Grade']

    fu.save_json(result, FILE_NAME)

