from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import LocalSession, engine, Base
from models import User, Note
from schema import UserCreate, UserData, UserOnly, NoteCreate, NoteData

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_session():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

# URL

@app.get('/users', response_model=List[UserOnly])
def read_users(db_session: Session = Depends(get_session)):
    users = db_session.query(User).all()
    return users


@app.get('/users/{user_id}', response_model=UserData)
def read_user(user_id: int, db_session: Session = Depends(get_session)):
    user= db_session.query(User).where(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return user

@app.post('/users', response_model=UserData, status_code=201)
def add_users(user : UserCreate, db_session: Session = Depends(get_session)):

    db_user = User(**user.model_dump())
    db_session.add(db_user)
    print(db_user.id)

    db_session.commit()
    db_session.refresh(db_user)
    print(db_user.id)
    return db_user

@app.post('/notes', response_model=NoteData, status_code=201)
def add_note(note: NoteCreate, db_session: Session = Depends(get_session)):
    db_note = Note(**note.model_dump())
    db_session.add(db_note)
    db_session.commit()
    db_session.refresh(db_note)
    return db_note

@app.get('/notes', response_model=List[NoteData])
def read_notes(db_session: Session = Depends(get_session)):
    notes = db_session.query(Note).all()
    return notes


import uvicorn

uvicorn. run(app, host="0.0.0.0", port=8000)
