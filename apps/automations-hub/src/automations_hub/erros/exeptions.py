from fastapi import status


class AppError(Exception):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    message = "Internal server error"

    def __init__(self, *args, **kwargs):
        self.detail = self.message.format(*args, **kwargs)
        super().__init__(self.detail)


class InvalidAutomationSlug(AppError):
    status_code = status.HTTP_404_NOT_FOUND
    message = "Automation '{0}' not found."


class ExecutionNotFound(AppError):
    status_code = status.HTTP_404_NOT_FOUND
    message = "Execution '{0}' not found."


class ExecutionAlreadyRunning(AppError):
    status_code = status.HTTP_409_CONFLICT
    message = "Execution '{0}' is already running."