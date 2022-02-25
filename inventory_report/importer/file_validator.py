class Validator:

    def valid_file_type(file_path, expected_type):
        file_type = file_path.split('.')[-1]
        if file_type != expected_type:
            raise ValueError('Arquivo inválido')
