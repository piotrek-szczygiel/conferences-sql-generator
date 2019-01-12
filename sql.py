def sql_delete(table):
    return 'delete from {0};\ndbcc checkident({0}, reseed, 0);'.format(table)


def sql_values_single(values):
    return '(' + ', '.join("'" + str(x) + "'" for x in values) + ')'


def sql_values_multiple(values_multiple):
    return ',\n'.join(sql_values_single(x) for x in values_multiple)


def sql_columns(columns):
    return '(' + ', '.join(columns) + ')'


def sql_insert(table, columns, values):
    return "insert into {} {} values\n{};".format(table,
                                                  sql_columns(columns),
                                                  sql_values_multiple(values))
