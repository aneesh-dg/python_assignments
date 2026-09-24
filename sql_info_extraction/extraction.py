import sys
import json
import re

input_file = sys.argv[1]


with open(input_file, "r", encoding="utf-8") as file:
    sql = file.read()



match = re.search(
    r"CREATE\s+PROCEDURE\s+(\w+)",
    sql,
    re.IGNORECASE
)

if match:
    procedure_name = match.group(1)
else:
    procedure_name = None

#parameters
parameter_pattern = r"(@\w+)\s+(\w+)"

parameters = re.findall(parameter_pattern, sql)

parameters = [
    {
        "name": name,
        "type": datatype
    }
    for name, datatype in parameters
]


#table name

table_pattern = r"\b(?:FROM|UPDATE|INTO|JOIN)\s+([A-Za-z_][A-Za-z0-9_]*)"

tables = re.findall(
    table_pattern,
    sql,
    re.IGNORECASE
)

# Remove duplicates while preserving order
tables = list(dict.fromkeys(tables))


# sql operations
operation_pattern = r"\b(SELECT|INSERT|UPDATE|DELETE)\b"

operations = re.findall(
    operation_pattern,
    sql,
    re.IGNORECASE
)

operations = [operation.upper() for operation in operations]

operations = list(dict.fromkeys(operations))


result = {
    "procedure_name": procedure_name,
    "parameters": parameters,
    "tables": tables,
    "operations": operations
}
output_file = "sample_stored_procedure.json"

with open(output_file, "w", encoding="utf-8") as file:
    json.dump(result, file, indent=4)