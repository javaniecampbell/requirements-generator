# Create a Web API using FastAPI with route to products
import os
from fastapi import Depends, FastAPI, Form, Request, UploadFile
from pydantic import BaseModel, ConfigDict

from shared.logging import Logger


logger = Logger()

app = FastAPI()


# Generate all the endpoints for the API using FastAPI and Pydantic based on the table below
"""
## Endpoints


| Method | Endpoint                                            | Description                                                  |
| ------ | --------------------------------------------------- | ------------------------------------------------------------ |
| POST   | /projects/request/upload                            | User should be able to upload request with title and description, uploaded file, document (*.pdf, *.docx, *.excel, *.csv, *.markdown, *.md) for generation with other actions to be performed later by a job queue |
| POST   | /projects/:project-id/requirements/upload           | User should be able to upload requirements document or text, title, description document (*.pdf, *.docx, *.excel, *.csv, *.markdown, *.md) as starting point for generation to be added to a job queue |
| POST   | /projects/:project-id/feature-list/upload           | User should be able to upload feature-list document (*.pdf, *.docx, *.excel, *.csv, *.markdown, *.md) or text, title, description as starting point for generation to be added to a job queue |
| POST   | /projects/:project-id/stories/upload                | User should be able to upload user stories as a document (*.pdf, *.docx, *.excel, *.csv, *.markdown, *.md)  or text, title, description as starting point for generation to be added to a job queue. |
| POST   | /projects/:project-id/requirements/:job-id/generate | User should be able to trigger or schedule the generation of the job for requirements generation  in background worker or job scheduler from request uploaded. |
| POST   | /projects/:project-id/feature-list/:job-id/generate | User should be able to trigger or schedule the generation of the job for feature list breakdown in another background worker or job scheduler from the requirements previously generated. |
| POST   | /projects/:project-id/stories/:job-id/generate      | User should be able to trigger or schedule the generation of the job for user stories breakdown in another background worker or job scheduler from the feature list previously generated. |
"""


# Create a class for each endpoint using Pydantic BaseModel
class ProjectRequest(BaseModel):
    title: str
    description: str
    uploaded_filename: str | None = None
    document: str

    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        description: str = Form(...),
        uploaded_filename: str = Form(...),
        document: str = Form(...),
    ):
        return cls(
            title=title,
            description=description,
            uploaded_filename=uploaded_filename,
            document=document,
        )


class Requirements(BaseModel):
    title: str
    description: str
    uploaded_filename: str | None = None
    document: str

    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        description: str = Form(...),
        uploaded_filename: str = Form(...),
        document: str = Form(...),
    ):
        return cls(
            title=title,
            description=description,
            uploaded_filename=uploaded_filename,
            document=document,
        )


class FeatureList(BaseModel):
    title: str
    description: str
    uploaded_filename: str | None = None
    document: str

    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        description: str = Form(...),
        uploaded_filename: str = Form(...),
        document: str = Form(...),
    ):
        return cls(
            title=title,
            description=description,
            uploaded_filename=uploaded_filename,
            document=document,
        )


class Stories(BaseModel):
    title: str
    description: str
    uploaded_filename: str | None = None
    document: str

    @classmethod
    def as_form(
        cls,
        title: str = Form(...),
        description: str = Form(...),
        uploaded_filename: str = Form(...),
        document: str = Form(...),
    ):
        return cls(
            title=title,
            description=description,
            uploaded_filename=uploaded_filename,
            document=document,
        )


class GenerateRequirements(BaseModel):
    job_id: str


class GenerateFeatureList(BaseModel):
    job_id: str


class GenerateStories(BaseModel):
    job_id: str


# Create the endpoints using FastAPI
@app.post("/projects/request/upload")
async def upload_request(
    request: Request,
    form_data: ProjectRequest = Depends(ProjectRequest.as_form),
    uploaded_file: UploadFile | None = None,
):
    logger.info("Entering upload_request")
    project_id = "123"
    save_to: str = ""
    # Save the uploaded file
    if uploaded_file:
        if not os.path.exists(f"uploads/projects/{project_id}"):
            os.makedirs(f"uploads/projects/{project_id}")
        if form_data.uploaded_filename:
            save_to = f"uploads/projects/{project_id}/{form_data.uploaded_filename}.{uploaded_file.filename.split('.')[-1]}"
        else:
            form_data.uploaded_filename = uploaded_file.filename
            save_to = f"uploads/projects/{project_id}/{uploaded_file.filename}"
        with open(save_to, "wb") as f:
            f.write(uploaded_file.read())
    else:
        logger.info("No file uploaded")
        save_to = None
    return form_data


@app.post("/projects/{project_id}/requirements/upload")
async def upload_requirements(project_id: str, requirements: Requirements):
    return requirements


@app.post("/projects/{project_id}/feature-list/upload")
async def upload_feature_list(project_id: str, feature_list: FeatureList):
    return feature_list


@app.post("/projects/{project_id}/stories/upload")
async def upload_stories(project_id: str, stories: Stories):
    return stories


@app.post("/projects/{project_id}/requirements/{job_id}/generate")
async def generate_requirements(project_id: str, job_id: str) -> GenerateRequirements:
    return generate_requirements


@app.post("/projects/{project_id}/feature-list/{job_id}/generate")
async def generate_feature_list(project_id: str, job_id: str) -> GenerateFeatureList:
    return generate_feature_list


@app.post("/projects/{project_id}/stories/{job_id}/generate")
async def generate_stories(project_id: str, job_id: str) -> GenerateStories:
    return generate_stories


class Product(BaseModel):
    name: str
    description: str
    price: float
    tax: float

    model_config = ConfigDict(protected_namespaces=(), extra="ignore")


@app.post("/products/")
async def create_product(product: Product):
    return product


@app.get("/products/")
async def get_products():
    return {
        "products": [
            {
                "name": "Product2",
                "description": "Description1",
                "price": 9.99,
                "tax": 1.99,
            }
        ]
    }
