from typing_extensions import Self

class TableController:
    def __init__(self: Self, classInstance, table_name: str, variables: dict):
        self.table_name: str = table_name
        self.variables = variables
        self.createTable()
        #gunanya untuk Alter Table, Delete, Select, Dll

    def createTable(self: Self):
        query = f"""
        CREATE TABLE {self.table_name} (
            ...
        )
        """
        self.executeSql(query)

    def selectOne(self, select: str = "*", where: dict = {}) -> :
        query = f'SELECT {select} FROM {self.table_name}'
        self.executeSql(query)

    def executeSql(self, query: str) -> bool:
        print(query)

def persistClass(classInstance: type) -> TableController:
    instance = classInstance()
    variables = vars(instance)
    tableController = TableController(instance.class_name, variables)
    
    return tableController
    
def variable(type: str, default_value = None, prop: dict = {}):
    return {
        "type": type,
        "value": default_value,
        "prop": prop
    }

class Table:
    def __init__(self, class_name: str):
        self.class_name = self.__class__.__name__
        pass

    def persist(self) -> bool:
        query = f'INSERT INTO {self.class_name}(...) SET(...)'
        pass

    def delete(self) -> bool:
        query = f'DELETE FROM {self.class_name} WHERE 1'
        return True

    def getVariables(self) -> Self:
        return vars(self)

