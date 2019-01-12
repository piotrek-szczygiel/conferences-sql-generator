def delete(table):
    return 'delete from {0};\ndbcc checkident({0}, reseed, 0);\n'.format(table) + '\n'


def insert(objects):
    if type(objects) != list:
        objects = [objects]

    table = objects[0].TABLE
    columns = [x for x in objects[0].__dict__]
    values = []

    for o in objects:
        values.append([o.__dict__[x] for x in columns])

    return _insert(table, columns, values) + '\n'


def delete_and_insert(objects):
    if type(objects) != list:
        objects = [objects]

    table = objects[0].TABLE

    return delete(table) + insert(objects)


def _insert(table, columns, values):
    return "insert into {} {} values\n{};\n".format(table,
                                                    _columns(columns),
                                                    _values_multiple(values))


def _convert(value):
    if value is None:
        return "''"
    elif type(value) == bool:
        return '1' if value else '0'
    else:
        return "'" + str(value) + "'"


def _values_single(values):
    return '(' + ', '.join(_convert(x) for x in values) + ')'


def _values_multiple(values_multiple):
    return ',\n'.join(_values_single(x) for x in values_multiple)


def _columns(columns):
    return '(' + ', '.join(columns) + ')'
