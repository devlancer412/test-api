from db.database import Database

database = Database()
engine = database.get_db_connection()

# Dependencies
async def get_db_session():
  session = database.get_db_session(engine)
  try:
    yield session
  finally:
    session.close()