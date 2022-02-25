from inventory_report.importer.importer import Importer
from inventory_report.importer.file_validator import Validator

import csv

RIGHT_TYPE = 'csv'


class CsvImporter(Importer):
    def import_data(file):

        Validator.valid_file_type(file_path=file, expected_type=RIGHT_TYPE)

        with open(file) as CSV_report:
            report_reader = csv.DictReader(CSV_report, delimiter=",")

            csv_dict_list = [row for row in report_reader]
        return csv_dict_list
