from sqlalchemy import create_engine, text

engine = create_engine(
    'mysql+pymysql://sql12786184:Um2DwxGJLs@sql12.freesqldatabase.com:3306/sql12786184'
)
with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
result1 = result.all()


def load_jobs_from_db(id):
    with engine.connect() as conn:
        result1 = conn.execute(text('SELECT * FROM jobs WHERE id = :val'),
                               {'val': id})
        rows = result1.all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0]._mapping)
    
        
