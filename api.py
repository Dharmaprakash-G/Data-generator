from fastapi import FastAPI, Body, HTTPException
from fastapi.responses import StreamingResponse

from generator.engine import generate_dataset
from exporters.csv_exporter import generate_csv_string
from schemas.schema_models import DatasetSchema


app = FastAPI(
    title = "GeneratorX",
    description  = "Schema-driven data generation engine",
    version = "1.0.0"
)


@app.post("/generate")
def generate_dataset_api(schema: DatasetSchema): #schema from fastapi as json, FastAPI converts JSON → Python dict
    try:
        data = generate_dataset(schema.dict())
    except ValueError as e:
        raise HTTPException(status_code = 422, detail = str(e))
    
    return data


@app.post("/generate/csv")
def generate_csv(schema: DatasetSchema):
    try:
        data = generate_dataset(schema.dict())
    except ValueError as e:
        raise HTTPException(status_code = 422, detail = str(e))

    csv_buffer = generate_csv_string(data)

    filename = f"{schema.table_name}.csv"

    return StreamingResponse(
        csv_buffer,
        media_type = "text/csv",
        headers = {
            "Content-Disposition": f"attachment; filename = {filename}"
        }
    )
   