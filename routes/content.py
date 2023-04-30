from controller import content
from fastapi import APIRouter, Depends, status
from models.content import PostSchema  
from models.databse import connect_db, SessionLocal  
from sqlalchemy.orm import Session
from models.content import PostSchema

db = SessionLocal()
router = APIRouter(
    prefix = '/posts'
)

db = SessionLocal()
@router.post('/create', status_code=status.HTTP_201_CREATED)
def post_new(post:PostSchema, db:Session=Depends(connect_db)):
    return content.create_post(post = post , db = db) 

@router.get('/get', status_code=status.HTTP_200_OK)
def get_all( db:Session=Depends(connect_db)):
    return content.read_all( db = db )

@router.get('/get/{postid}' , status_code=status.HTTP_200_OK)
def get_post_by_id( postid:int ,  db:Session=Depends(connect_db)):
    return content.get_by_id(postid = postid ,   db = db )


@router.put('/update/{postid}', status_code=status.HTTP_200_OK)
def update( post:PostSchema,  postid : int , db : Session = Depends(connect_db)):
    return content.update_post( post=post,  postid = postid , db = db )


@router.delete('/delete/{postid}' , status_code=status.HTTP_204_NO_CONTENT)

def delete_post(postid : int , db : Session = Depends(connect_db)):
    return content.delete(postid = postid , db = db )