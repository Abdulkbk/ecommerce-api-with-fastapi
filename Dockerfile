FROM python:3.10 as python-base

RUN mkdir ecom
WORKDIR /ecom
COPY /pyproject.toml /ecom

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .
EXPOSE 8000
CMD [ "gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app"]