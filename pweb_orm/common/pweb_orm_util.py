class PWebORMUtil:
    @staticmethod
    def enum_to_string(data, name):
        if name in data and data[name]:
            data[name] = str(data[name])
