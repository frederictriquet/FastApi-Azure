import json
import logging

from services.datatypes import SometimesLong
from fastapi import Response, status, BackgroundTasks

def long_task(func):
  def inner(data: SometimesLong):
    logging.info('start task')
    result = func(data)
    str_result = json.dumps(result) #[:30]
    logging.info(f'Here, we should POST {str_result}... to {data.callback_url}')
    logging.info('end task')
  return inner


def launch_task(task: callable, req: object, check_if_too_long: callable, background_tasks: BackgroundTasks, response: Response):
  # logging.info(check_if_too_long(req))
  if not check_if_too_long(req):
    return task(req)
  response.status_code = status.HTTP_202_ACCEPTED
  background_tasks.add_task(long_task(task), req)
  return { 'result': 'job created' }
