
import csv
import io
from fastapi import FastAPI, Response
from sqlalchemy import create_engine, MetaData, Table, select
from databases import Database
DATABASE_URL = "postgresql://user:password@localhost/dbname"
database = Database(DATABASE_URL)
metadata = MetaData()
# Replace "table_name" with your table name
table_name = Table("table_name", metadata, autoload=True, autoload_with=create_engine(DATABASE_URL))
app = FastAPI()
@app.on_event("startup")
async def startup():
    await database.connect()
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
@app.get("/csv", response_class=Response, media_type="text/csv")
async def get_csv():
    query = select([table_name])  # Add filters if needed
    rows = await database.fetch_all(query)
    stream = io.StringIO()
    csv_writer = csv.writer(stream)
    csv_writer.writerow(table_name.columns.keys())  # Write the header
    csv_writer.writerows(rows)  # Write the data
    return Response(content=stream.getvalue(), media_type="text/csv")



