import json

class Credentials
    def __init__(self, filename:str):
        self.__filename = filename
        self.__credentials = json.load(open(filename, "r"))

    def __raise_exception_if_not_present(self, _key:str):
        if (_key not in self.__credentials):
            raise Exception(f"[!] {_key} not found in {self.__filename}")
 
    def get_api_key(self) -> str:
        _key = "API_KEY"
        self.__raise_exception_if_not_present(_key)
        return self.__credentials[_key]
            
    def get_api_hash(self) -> str:
        _key = "API_HASH" 
        self.__raise_exception_if_not_present(_key)
        return self.__credentials[_key]
            

