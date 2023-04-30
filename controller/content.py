from models import content 
from models.databse import connect_db, SessionLocal  
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status


#create a post
db = SessionLocal()
def create_post(post: content.PostSchema , db:Session=Depends(connect_db) ):
    new_post = content.PostModel(
        title = post.title,
        content = post.content
    )
    try:
        db.add(new_post)
        print('Created succesfuly')
        db.commit()
        db.refresh(new_post)
        return {"new_post": new_post , "status_code":201}
    except Exception as error:
        print(error)
        raise error

#get all posts 
def read_all( db : Session = Depends(connect_db)):
    all_posts = db.query(content.PostModel).all()
    try:
        if not all_posts:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Internal server error')
    except  Exception as error:
        raise HTTPException(status_code = status.HTTP_500_INTERNAL_SERVER_ERROR, detail = error)
    finally:
       return {"all_posts": all_posts,  "status_code": 200}
    
#get post by id 

def get_by_id (postid: int , db : Session= Depends(connect_db)):
    post = db.query(content.PostModel).filter(content.PostModel.id == postid).first()
    if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = 'Cannot find id ')
    return post


#update post by id 

def update_post( post:content.PostSchema,  postid : int , db : Session = Depends(connect_db) ):
    post_db = db.query(content.PostModel).filter(content.PostModel.id == postid).first()

    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Cannot find post ')
    
    post_db.title = post.title 
    post_db.content = post.content 

    db.commit()
    db.refresh(post_db)
    return post_db

   
def delete(postid:int , db : Session = Depends(connect_db)):
    post = db.query(content.PostModel).filter(content.PostModel.id == postid).first()

    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Cannot find post')
    
    db.delete(post)
    db.commit()

    return {"message":"Deleted", "status_code" : 204 }