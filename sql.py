def start():
    return '''-- remove everything
exec sys.sp_msforeachtable 'disable trigger all on ?';
exec sys.sp_msforeachtable 'alter table ? nocheck constraint all';
exec sys.sp_msforeachtable 'delete from ?';
exec sys.sp_msforeachtable 'alter table ? check constraint all';
exec sys.sp_msforeachtable 'enable trigger all on ?';

'''


def put(objects):
    if type(objects) != list:
        objects = [objects]

    table = objects[0].TABLE
    columns = [x for x in objects[0].__dict__]
    values = []

    for o in objects:
        values.append([o.__dict__[x] for x in columns])

    return f'''-- fill {table}
set identity_insert {table} on;
{insert(table, columns, values)}
set identity_insert {table} off;
'''


def put_all(tables):
    result = []
    for table in tables:
        result.append(put(table))

    return '\n'.join(result)


def insert(table, columns, values):
    return 'insert into {} {} values\n{};'.format(table,
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
