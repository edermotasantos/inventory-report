import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


SIMPLE = 'simples'


class Inventory:
    @classmethod
    def import_data(self, path, reportType):
        with open(path) as reportCSV:
            report_reader = csv.DictReader(reportCSV, delimiter=",")

            dict_products = [row for row in report_reader]

            if reportType == SIMPLE:
                return SimpleReport.generate(dict_products)

        return CompleteReport.generate(dict_products)


Inventory.import_data('inventory_report/data/inventory.csv', 'simples')
