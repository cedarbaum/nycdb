def create_table(table_name, fields, pk_fields=[]):
    """
    String, Iterable --> String
    """
    if len(pk_fields) > 0:
        sql = "CREATE TABLE IF NOT EXISTS {} (".format(table_name)
        sql += ", ".join(["{} {}".format(field, fields[field]) for field in fields])
        sql += ", PRIMARY KEY ({})".format(", ".join(pk_fields))
        sql += ")"
    else:
        sql = "CREATE TABLE IF NOT EXISTS {} (".format(table_name)
        sql += ", ".join(["{} {}".format(field, fields[field]) for field in fields])
        sql += ")"
    return sql


def insert_many(table_name, rows, pk_fields=[], update=False):
    """
    Given a table name and a list of dictionaries representing
    rows, generate a (sql, template) tuple of strings that can be
    passed to psycopg2.extras.execute_values() [1] to bulk insert all the
    values for improved efficiency [2].

    For example:

        >>> insert_many('boop', [{'foo': 1, 'bar': 2}])
        ('INSERT INTO boop (foo, bar) VALUES %s', '(%(foo)s, %(bar)s)')

    [1]: http://initd.org/psycopg/docs/extras.html#psycopg2.extras.execute_values
    [2]: https://stackoverflow.com/a/30985541
    """

    field_names = list(rows[0].keys())
    fields = ", ".join(field_names)
    update_clause = ", ".join(
        [f"{field}=EXCLUDED.{field}" for field in field_names if field not in pk_fields]
    )
    placeholders = ", ".join(["%({})s".format(k) for k in field_names])
    template = f"({placeholders})"

    sql = None
    if len(pk_fields) == 0:
        sql = f"""INSERT INTO {table_name} ({fields}) VALUES %s"""
    else:
        pk_fields_str = ", ".join(pk_fields)
        sql = f"""INSERT INTO {table_name} ({fields}) VALUES %s
                    ON CONFLICT ({pk_fields_str}) DO UPDATE
                    SET {update_clause}"""

    return sql, template
