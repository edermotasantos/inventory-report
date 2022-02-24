from datetime import date, datetime
TODAY = date.today()


class SimpleReport:
    @classmethod
    def generate(self, stock_report):
        company_name = [product["nome_da_empresa"] for product in stock_report]

        production_date = [prod["data_de_fabricacao"] for prod in stock_report]
        production_date.sort()

        expire_date = []
        for product in stock_report:
            expiration = product["data_de_validade"]
            convert_to_date = datetime.strptime(expiration, "%Y-%m-%d").date()
            expire_date.append(convert_to_date)

        company = max(company_name, key=company_name.count)
        nearest_to_expire = min(dt for dt in expire_date if dt > TODAY)

        comp = f'Empresa com maior quantidade de produtos estocados: {company}'
        fab = f'Data de fabricação mais antiga: {production_date[0]}'
        exp = f'Data de validade mais próxima: {nearest_to_expire}'

        return f'{fab}\n{exp}\n{comp}\n'
