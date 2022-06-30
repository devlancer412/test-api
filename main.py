# Don't edit
__author__ = "Joseph Anderson"
__copyright__ = "Copyright 2022, Modern Time Team"
__license__ = "INTERNAL"
__version__ = "0.1.0"
__maintainer__ = __author__
__email__ = "devanderson0412@gmail.com"
__status__ = "alpha"

import uvicorn
from __internal import bootstrap
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes import router as api_router
from db.database import Database, Base

app = FastAPI(
    title="Modern Time Backend",
    description="Gambling site backend API",
    version="-".join([__version__, __status__]),
)

if __name__ == '__main__':
    uvicorn.run("main:app", port=80, log_level="info", reload = True)
    print("running")
    
bootstrap(app)

database = Database()
engine = database.get_db_connection()

Base.metadata.create_all(bind=engine)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins="*",
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

app.include_router(api_router)
