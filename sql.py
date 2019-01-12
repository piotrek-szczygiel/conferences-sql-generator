def prepare(table):
    return 'delete from {0};\ndbcc checkident({0}, reseed, 0);\n'.format(table)


def insert(objects):
    if type(objects) != list:
        objects = [objects]

    table = objects[0].TABLE
    columns = [x for x in objects[0].__dict__]
    values = []

    for o in objects:
        values.append([o.__dict__[x] for x in columns])

    return ('set identity_insert {} on;\n'.format(table)
            + _insert(table, columns, values)
            + 'set identity_insert {} off;\n'.format(table))


def put(objects):
    if type(objects) != list:
        objects = [objects]

    table = objects[0].TABLE

    return prepare(table) + insert(objects)


def _insert(table, columns, values):
    return 'insert into {} {} values\n{};\n'.format(table,
                                                    _columns(columns),
                                                    _values_multiple(values))


def _convert(value):
    if value is None:
        return "''"
    elif type(value) == bool:
        return '1' if value else '0'
    elif type(value) == int:
        return str(value)
    else:
        return "'" + str(value) + "'"


def _values_single(values):
    return '(' + ', '.join(_convert(x) for x in values) + ')'


def _values_multiple(values_multiple):
    return ',\n'.join(_values_single(x) for x in values_multiple)


def _columns(columns):
    return '(' + ', '.join(columns) + ')'
