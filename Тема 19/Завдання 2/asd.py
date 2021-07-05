class Doc_ContextManager:
    counter = 0
    file_types = {
        'jpg': 0,
        'png': 0,
        'txt': 0,
        'other': 0
    }

    def __init__(self, file, mode):
        self.file = file
        self.mode = mode
        self.type_file = self.file.split()[-1]

    def check_dict(self):
        for key in Doc_ContextManager.file_types.keys():
            if key == self.type_file:
                value = Doc_ContextManager.file_types.get(key)
                value += 1
                Doc_ContextManager.file_types[key] = value
        return Doc_ContextManager.file_types

    def __enter__(self):
        Doc_ContextManager.check_dict(self.type_file)
        Doc_ContextManager.counter += 1
        print(f'Файл відкривався: {Doc_ContextManager.counter}.')
        return open(self.file, self.mode)

    def __exit__(self, exc_type, exc_tb, exc_value):
        print('Finishing work.')
        return None

with Doc_ContextManager('file.txt', 'r'):
    pass