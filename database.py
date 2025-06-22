from sqlalchemy import create_engine, text

engine = create_engine(
    'mysql+pymysql://sql12786184:Um2DwxGJLs@sql12.freesqldatabase.com:3306/sql12786184'
)
with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  