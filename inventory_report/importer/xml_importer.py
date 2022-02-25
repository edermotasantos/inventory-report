from inventory_report.importer.importer import Importer
from inventory_report.importer.file_validator import Validator

import xml.etree.ElementTree as ET


RIGHT_TYPE = 'xml'


class XmlImporter(Importer):
    def import_data(file):

        Validator.valid_file_type(file_path=file, expected_type=RIGHT_TYPE)

        with open(file) as XML_report:
            tree = ET.parse(XML_report)
            base_xml = tree.getroot()
            xml_dict_list = []

            for dataset in base_xml:
                product = {}
                for record in dataset:
                    product[record.tag] = record.text
                xml_dict_list.append(product)

        return xml_dict_list
