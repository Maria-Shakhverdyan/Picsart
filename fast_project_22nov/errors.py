from fastapi import HTTPException

class ValidationError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=422, detail=detail)

class FileError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=500, detail=detail)

class NotFoundError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=404, detail=detail)
