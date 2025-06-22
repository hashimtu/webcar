from sqlalchemy import create_engine, text

engine = create_engine('mysql+pymysql://sql12786184:Um2DwxGJLs@sql12.freesqldatabase.com:3306/sql12786184'
)
result = connection.execute(text("SELECT * FROM your_table_name"))
for row in result:
    print(row)