import os

from fastapi import APIRouter, File, UploadFile
from uuid import uuid4
from starlette.responses import FileResponse
from simple_file_storage_api.dto.file import File as FileDTO
from simple_file_storage_api.config import service_config

file_router = APIRouter()


@file_router.post("/upload", response_model=FileDTO)
async def upload_file(file: UploadFile = File(...)) -> FileDTO:
    file_dto = FileDTO(id=uuid4())
    path = f"{service_config.storage_path}/{file_dto.id}"
    with open(path, "wb") as buffer:
        buffer.write(await file.read())
    return file_dto


@file_router.get("/download/{file_id}", response_class=FileResponse)
async def download_file(file_id: str):
    path = f"{service_config.storage_path}/{file_id}"
    if not os.path.exists(path):
        raise FileNotFoundError
    return FileResponse(path)
