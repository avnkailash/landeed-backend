from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .api import router
from .db import engine, Base

# Create the database tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Set up CORS
origins = [
    "http://localhost:3000",  # React app running on localhost:3000
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include routers
app.include_router(router)
