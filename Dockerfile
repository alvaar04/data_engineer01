FROM python:3.10-slim

WORKDIR /pipeline

COPY ./ /pipeline/

RUN pip install -r /pipeline/requirements.txt

CMD ["python", "/pipeline/src/run_pipeline.py"]