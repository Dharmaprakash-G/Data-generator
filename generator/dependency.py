from collections import defaultdict, deque

def order_tables_by_dependency(tables: list[dict]) -> list[dict]:

    #Map table_name -> table schema
    table_map = {t["table_name"]: t for t in tables}

    #build graph
    graph = defaultdict(set)
    indegree = {name: 0 for name in table_map}

    for table in tables:
        table_name = table["table_name"]

        for col in table.get("columns", []):
            ref = col.get("ref")

            if ref:
                parent = ref["table"]

                if parent not in table_map:
                    raise ValueError(
                        f"Table '{table_name}' references unknown table '{parent}'"
                    )

                
                #edge : parent -> table_name
                if table_name not in graph[parent]:
                    graph[parent].add(table_name)
                    indegree[table_name] += 1
    
    #kahn's algo for topological sort
    queue = deque([
        name for name, deg in indegree.items() if deg == 0
    ])

    ordered_names = []

    while queue:
        current = queue.popleft()
        ordered_names.append(current)

        for child in graph[current]:
            indegree[child] -= 1

            if indegree[child] == 0:
                queue.append(child)

    if len(ordered_names) != len(table_map):
        raise ValueError(
            "Circular dependency detected between tables"
        )

    return [table_map[name] for name in ordered_names]
 




