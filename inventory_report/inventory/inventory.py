import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


SIMPLE = 'simples'


class Inventory:
    @classmethod
    def import_data(self, path, reportType):
        file_type = path.split('.')[1]

        if file_type == 'csv':
            return CsvReport(path, reportType).read_csv()
        elif file_type == 'xml':
            return XmlReport(path, reportType).read_xml()
        elif file_type == 'json':
            return JsonReport(path, reportType).read_json()


class CsvReport():
    def __init__(self, path, reportType):
        self.path = path
        self.reportType = reportType

    def read_csv(self):
        with open(self.path) as reportCSV:
            report_reader = csv.DictReader(reportCSV, delimiter=",")

            csv_dict_list = [row for row in report_reader]
            if self.reportType == SIMPLE:
                return SimpleReport.generate(csv_dict_list)

        return CompleteReport.generate(csv_dict_list)


class JsonReport():
    def __init__(self, path, reportType):
        self.path = path
        self.reportType = reportType

    def read_json(self):
        with open(self.path) as reportJSON:
            report_reader = reportJSON.read()

            json_dict_list = json.loads(report_reader)
            if self.reportType == SIMPLE:
                return SimpleReport.generate(json_dict_list)

            return CompleteReport.generate(json_dict_list)


class XmlReport():
    def __init__(self, path, reportType):
        self.path = path
        self.reportType = reportType

    def read_xml(self):
        #  How read a XML file, link below:
        #  https://docs.python.org/3/library/xml.etree.elementtree.html
        tree = ET.parse(self.path)
        base_xml = tree.getroot()
        xml_dict_list = []

        for dataset in base_xml:
            product = {}
            for record in dataset:
                product[record.tag] = record.text
            xml_dict_list.append(product)

        if self.reportType == SIMPLE:
            return SimpleReport.generate(xml_dict_list)

        return CompleteReport.generate(xml_dict_list)
