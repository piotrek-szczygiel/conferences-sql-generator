import sys

from faker import Factory

fake = Factory.create('pl_PL')


def sql_values_single(values):
    return '(' + ', '.join("'" + str(x) + "'" for x in values) + ')'


def sql_values_multiple(values_multiple):
    return ',\n'.join(sql_values_single(x) for x in values_multiple)


def sql_columns(columns):
    return '(' + ', '.join(columns) + ')'


def sql_insert(table, columns, values):
    return "insert into {} {} values\n{}".format(table,
                                                 sql_columns(columns),
                                                 sql_values_multiple(values))


def insert_clients(count):
    clients = []

    for _ in range(count):
        if fake.boolean():
            clients.append(random_client_individual())
        else:
            clients.append(random_client_company())

    return sql_insert('client',
                      [
                          'is_company',
                          'name',
                          'email',
                          'password',
                          'nip',
                          'address'
                      ],
                      clients
                      )


def random_client_company():
    return [
        1,
        fake.company(),
        fake.email(),
        fake.sha256(),
        fake.random_number(digits=10),
        fake.address().replace('\n', ', ')
    ]


def random_client_individual():
    return [
        0,
        fake.first_name() + ' ' + fake.last_name(),
        fake.email(),
        fake.sha256(),
        '',
        fake.address().replace('\n', ', ') if fake.boolean() else ''
    ]


if __name__ == '__main__':
    result = insert_clients(100)

    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        with open(file_name, 'wb') as file:
            file.write(result.encode('utf-8'))
    else:
        print(result)
