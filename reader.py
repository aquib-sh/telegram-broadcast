import pandas

class CSVReader:
    def __init__(self, filename:str):
        self.__raise_error_if_not_csv(filename)
        self.filename = filename
        self.data = {}

    def __raise_error_if_not_csv(self, filename:str):
        if (not filename.endswith(".csv")):
            raise Exception(f"[!] {filename} is not a CSV file")
        
    def __clean_data(self):
        DELETE_KEY = 'Unnamed'
        to_delete = []  # hold the unwanted col names
        for col in self.data:
            if DELETE_KEY in col:
                to_delete.append(col)
        # Delete the Unnamed columns
        for k in to_delete:
            del self.data[k]

    def load(self):
        df = pandas.read_csv(self.filename)
        self.data = df.to_dict()
        self.__clean_data()

    def __strip(self, value):
        string = str(value)
        return string.strip()

    def get_row(self) -> tuple:
        ID_KEY = 'ID'
        USERNAME_KEY = 'Username'
        NAME_KEY = 'Name'
        length = len(self.data[ID_KEY])

        for i in range(0, length):
            _id = self.__strip(self.data[ID_KEY][i])
            username = self.__strip(self.data[USERNAME_KEY][i])
            name = self.__strip(self.data[NAME_KEY][i])

            # if username if not present then skip
            if (username == 'No Username'):
                continue

            row = (_id, username, name)
            yield row

class Message:
    def __init__(self, filename:str):
        self.text = self.__read(filename)

    def __read(self, filename):
        fp = open(filename, "r")
        text = fp.read().strip()
        fp.close()
        return text

    def get(self):
        return self.text



