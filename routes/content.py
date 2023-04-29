from controller import content
from fastapi import APIRouter, Depends
from models.content import PostSchema  
from models.databse import connect_db, SessionLocal  
from sqlalchemy.orm import Session
from models.content import PostSchema

db = SessionLocal()
router = APIRouter(
    prefix = '/posts'
)

db = SessionLocal()
@router.post('/create')
def post_new(post:PostSchema, db:Session=Depends(connect_db)):
    return content.create_post(post = post , db = db) 

@router.get('/get')
def get_all( db:Session=Depends(connect_db)):
    return content.read_all( db = db )

@router.get('/get/{postid}')
def get_post_by_id( postid:int ,  db:Session=Depends(connect_db)):
    return content.get_by_id(postid = postid ,   db = db )


@router.put('/update/{postid}')
def update( post:PostSchema,  postid : int , db : Session = Depends(connect_db)):
    return content.update_post( post=post,  postid = postid , db = db )


@router.delete('/delete/{postid}')

def delete_post(postid : int , db : Session = Depends(connect_db)):
    return content.delete(postid = postid , db = db )