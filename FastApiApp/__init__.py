import logging

from fastapi import BackgroundTasks, FastAPI, Response

from services.datatypes import AsyncRequest, SyncRequest
from services.tasks import square_number_task, uppercase_string_task

from .lib import launch_task

logging.basicConfig(encoding='utf-8', level=logging.DEBUG)

app = FastAPI()

@app.post("/sync")
def sync_task(req: SyncRequest):
  return square_number_task(req)

@app.post('/async')
def async_task(req: AsyncRequest, background_tasks: BackgroundTasks, response: Response):
  return launch_task(uppercase_string_task, req, lambda req: len(req.string) > 20, background_tasks, response)

@app.post('/debug')
def post_debug(req: dict):
  logging.info(req)
  return { 'result': 'Debug done', 'req': req }

@app.get("/")
def ping():
  return { 'status': 'up' }