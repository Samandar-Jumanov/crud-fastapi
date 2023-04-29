from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import content
from models.databse import connect_db
app = FastAPI()

#db connection 

connect_db()
#Cors 
origins = ["*"]  
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(content.router)




