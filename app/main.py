from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import Settings

#automatically runs database tables creation
#models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
#origins = ["https://www.google.com"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

# a path or a route
@app.get("/")
def root() -> Dict:
    return {"message": "Welcome to my app"}
