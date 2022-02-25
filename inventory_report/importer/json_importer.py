from inventory_report.importer.importer import Importer
from inventory_report.importer.file_validator import Validator

import json

RIGHT_TYPE = 'json'


class JsonImporter(Importer):
    def import_data(file):

        Validator.valid_file_type(file_path=file, expected_type=RIGHT_TYPE)

        with open(file) as JSON_report:
            report_reader = JSON_report.read()

            json_dict_list = json.loads(report_reader)
        return json_dict_list
