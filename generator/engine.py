from generator.types import generate_value 
from generator.dependency import order_tables_by_dependency
import random


def generate_dataset(dataset_schema : dict):
    
    generate_data = {}
    value_registry = {}

    ordered_tables = order_tables_by_dependency(dataset_schema["tables"])
    
    for table in ordered_tables:
        table_name =  table["table_name"]
        rows = table["rows"]
        columns = table["columns"]

        table_row = []
        value_registry[table_name] = {}

        #initialize registry for each column
        for col in columns:
            value_registry[table_name][col["name"]] = []


        for _ in range(rows):
            row = {}

            for col in columns:
                col_name = col["name"]
                col_type = col["type"]

                # 🔗 HANDLE RELATIONSHIP
                if col.get("ref"):
                    ref_table = col["ref"]["table"]
                    ref_column = col["ref"]["column"]

                    parent_values = value_registry[ref_table][ref_column]

                    if not parent_values:
                        raise ValueError(
                            f"No values fount for reference {ref_table}.{ref_column}"
                        )

                    value = random.choice(parent_values)

                else:
                    value = generate_value(col_type, col)

                row[col_name] = value
                value_registry[table_name][col_name].append(value)

            table_row.append(row)

        generate_data[table_name] = table_row

    return generate_data