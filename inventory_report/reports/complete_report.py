from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    def generate(stock_report):
        quantity_products = {}
        p_stocked = ""

        for comp_data in stock_report:
            comp_name = comp_data["nome_da_empresa"]
            if comp_name in quantity_products:
                quantity_products[comp_name] += 1
            else:
                quantity_products[comp_name] = 1

        for comp in quantity_products.keys():
            p_stocked = f'{p_stocked}- {comp}: {quantity_products[comp]}\n'

        simple_report = SimpleReport.generate(stock_report)
        complete_report = (
            f'{simple_report}'
            f'\nProdutos estocados por empresa: \n'
            f'{p_stocked}'
        )
        return complete_report
