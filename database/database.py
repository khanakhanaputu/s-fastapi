from sqlmodel import create_engine, SQLModel

sql_url = "mysql+pymysql://root:@localhost:3306/belajar_fastapi"
engine = create_engine(sql_url)
