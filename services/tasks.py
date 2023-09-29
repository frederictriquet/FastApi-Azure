
from services.datatypes import AsyncRequest, SyncRequest


def uppercase_string_task(req: AsyncRequest):
  return req.string.upper()

def square_number_task(req: SyncRequest):
  return req.nb*req.nb
