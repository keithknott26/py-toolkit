import sqlite3
import csv

db = './database/grid.db'
conn = sqlite3.connect(db)
conn.text_factory = str
c = conn.cursor()

tables = [
    {'name': 'general', 'file': './bms/general.csv'},
    {'name': 'survival_curves', 'file': './bms/survival_curves.csv'},
]

for table in tables:
    tableName = table['name']

    c.execute('DROP TABLE IF EXISTS ' + tableName)
    c.execute('DROP TABLE IF EXISTS ' + tableName + '_titles')
    conn.commit()

    filePath = table['file']
    csvReader = csv.reader(open(filePath), delimiter='|')
    t = (csvReader,)
    titles = next(csvReader)
    generalInfo = next(csvReader)
    columnDescription = next(csvReader)
    titlesDescription = next(csvReader)

    CREATE_TABLE_SQL = 'CREATE TABLE ' + tableName + \
                       '(' + ' TEXT, '.join(titles) + \
                       ' TEXT)'
    c.execute(CREATE_TABLE_SQL)
    conn.commit()

    placeholders = ['?'] * len(titles)
    INSERT_INTO_TABLE_SQL = 'INSERT INTO ' + tableName + \
                            ' values(' + ', '.join(placeholders) + \
                            ')'
    for t in csvReader:
        c.execute(INSERT_INTO_TABLE_SQL, t)
    conn.commit()

    CREATE_TABLE_SQL = 'CREATE TABLE ' + tableName + '_titles' \
                                                     '(title TEXT, section TEXT, extra TEXT, title_long TEXT)'
    c.execute(CREATE_TABLE_SQL)
    conn.commit()

    INSERT_INTO_TABLE_SQL = 'INSERT INTO ' + tableName + '_titles' \
                                                         ' values(?,?,?,?)'

    headers = zip(titles, generalInfo, columnDescription, titlesDescription)

    for h in headers:
        c.execute(INSERT_INTO_TABLE_SQL, h)
    conn.commit()

    print(CREATE_TABLE_SQL)
    print(INSERT_INTO_TABLE_SQL)

conn.close()