def clear_db():
    return '''-- remove everything
exec sys.sp_msforeachtable 'disable trigger all on ?';
exec sys.sp_msforeachtable 'alter table ? nocheck constraint all';
exec sys.sp_msforeachtable 'delete from ?';
exec sys.sp_msforeachtable 'alter table ? check constraint all';
exec sys.sp_msforeachtable 'enable trigger all on ?';
set identity_insert conference off;
set identity_insert client off;
set identity_insert participant off;
set identity_insert conference_day off;
set identity_insert conference_price off;
set identity_insert conference_booking off;
set identity_insert payment off;
set identity_insert conference_day_booking off;
set identity_insert conference_day_participant off;
set identity_insert workshop off;
set identity_insert workshop_booking off;
set identity_insert workshop_participant off;

'''


def put(objects):
    if type(objects) != list:
        objects = [objects]

    table = objects[0].TABLE
    columns = []
    for column in objects[0].__dict__:
        if not column.startswith('_'):
            columns.append(column)
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
    result = []

    chunk_size = 1000
    if chunk_size > 1:
        separator = '\n'
    else:
        separator = ' '

    for chunk in _chunks(values, chunk_size):
        result.append('insert into {} {} values{}{};'
                      .format(table,
                              _columns(columns),
                              separator,
                              _values_multiple(chunk)))

    return '\n'.join(result)


def _chunks(values, size):
    for i in range(0, len(values), size):
        yield values[i:i + size]


def _convert(value):
    if value is None:
        return "null"
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
