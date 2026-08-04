from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from rich import print
from .exeptions import AppError
from typing import cast
async def app_error_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:

    error = cast(AppError, exc)

    return JSONResponse(
        status_code=error.status_code,
        content={
            "detail": error.detail,
        },
    )


def _walk(cls):
    for sub in cls.__subclasses__():
        yield sub
        yield from _walk(sub)


def register_error_handlers(app: FastAPI):
    print("[red]Registering error handlers...[/red]")
    for exc in _walk(AppError):
        app.add_exception_handler(exc, app_error_handler)
    print("[green]Error handlers registered successfully![/green]")