
from pydantic import BaseModel

class SometimesLong(BaseModel):
  callback_url: str

class SyncRequest(BaseModel):
  nb: int

class AsyncRequest(SometimesLong):
  string: str
