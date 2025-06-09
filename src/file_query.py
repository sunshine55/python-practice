from response_operator import ResponseOperator


class FileQuery:
    def __init__(self):
        pass

    def generate_operator_list(self, prompt):
        lines = prompt.split("\n")
        operator_list = []
        for line in lines:
            title, url = line.split("@")
            operator_list.append(ResponseOperator(title, url))
        return operator_list
