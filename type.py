class Type:
    def VARCHAR(a):
        return f"VARCHAR({a})"

    def CHAR(a):
        return f"CHAR({a})"

    def NVARCHAR(a):
        return f"NVARCHAR({a})"

    def NCHAR(a):
        return f"NCHAR({a})"

    def TEXT(a):
        return f"TEXT({a})"
    
    def BYTE():
        return f"BYTE"

    def DECIMAL(a, b):
        return f"DECIMAL({a}, {b})"

    def SHORTFLOAT():
        return f"SHORTFLOAT"

    def INTERGER():
        return f"INT"

    def NUMBER(a, b):
        return f"NUMBER({a}, {b})"

    def FLOAT(a):
        return f"FLOAT({a})"

    def LONGINTERGER():
        return f"LONGINT"

    def MONEY(a, b):
        return f"MONEY({a}, {b})"

    def LONGFLOAT():
        return f"LONGFLOAT"

    def SERIAL(a):
        return f"SERIAL({a})"

    def DATE():
        return f"DATE"

    def TIME():
        return f"TIME"

    def DATETIME():
        return f"DATETIME"

    def TIMESTAMP():
        return f"TIMESTAMP"

    def BINARY(a):
        return f"BINARY({a})"

    def BOOLEAN():
        return f"BOOLEAN"
