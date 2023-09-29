FROM python:3.9-slim

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN apt-get update && \
    apt-get upgrade --yes && \
    apt-get install --yes curl && \
    python3 -m venv $VIRTUAL_ENV && \
    python3 -m pip install --upgrade pip

EXPOSE 80
WORKDIR /code
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /code/

# "FastApiApp:app" because it's the "app" object defined in FastApiApp/__init__.py
# CMD ["/bin/bash"]
CMD ["uvicorn", "FastApiApp:app", "--host", "0.0.0.0", "--port", "80"]


# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "FastApiApp:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]