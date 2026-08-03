# from typing import Any,Optional,Callable
# from fastapi.requests import Request
# from fastapi.responses import JSONResponse
# from fastapi import FastAPI,status
# class BooklyExeption(Exception):
#     """Base class for all exceptions in the Bookly application."""
#     pass 

# class InvalidToken(BooklyExeption):
#     """Base class for all exceptions in the Bookly application."""
#     pass 
# class InvalidToken(BooklyExeption):
#     """Base class for all exceptions in the Bookly application."""
#     pass 

# class RevokeToken(BooklyExeption):
#     """Exception raised when a token is revoked."""
#     pass
# class AcessTokenRequired(BooklyExeption):
#     """Exception raised when an access token is required."""
#     pass
# class RefreshTokenRequired(BooklyExeption):
#     """Exception raised when a refresh token is required."""
#     pass
# class UserAlreadyExists(BooklyExeption):
#     """Exception raised when a user already exists."""
#     pass
# class InsufficientPermissions(BooklyExeption):
#     """Exception raised when a user does not have sufficient permissions to perform an action."""
#     pass
# class BookNotFound(BooklyExeption):
#     """when a book is not found."""
#     pass

# class UserNotFound(BooklyExeption):
#     """Exception raised when a user is not found."""
#     pass
# class TagNotFound(BooklyExeption):
#     """Exception raised when a tag is not found."""
#     pass
# class InvalidCredentials(BooklyExeption):
#     """user has provided email or password wrong."""
#     pass
# class TagAlreadyExists(BooklyExeption):
#     """Exception raised when a tag already exists."""
#     pass
# def create_exeption_handler(status_code:int,detail:Any)-> Callable[[Request,Exception],JSONResponse]:
#     async def exeption_hanlder(request:Request,exc:BaseException):
#         return JSONResponse(
#             content=detail,
#             status_code=status_code
#         )
#     return exeption_hanlder
# class AccountIsNotVerified(BooklyExeption):
#     """Exception raised when a user account is not verified."""
#     pass
# def register_all_errors(app:FastAPI):
#     app.add_exception_handler(
#     UserAlreadyExists,
#     create_exeption_handler(
#         status_code=400,
#         detail={"error_code": "User already exists"}
#     )
# )
#     app.add_exception_handler(
#         InvalidCredentials,
#         create_exeption_handler(
#             status_code=401,
#             detail={"error_code": "Invalid credentials"}
#         )
#     )
#     app.add_exception_handler(
#         UserNotFound,
#         create_exeption_handler(
#             status_code=404,
#             detail={"error_code": "User not found"}
#         )
#     )
#     app.add_exception_handler(
#         InvalidToken,
#         create_exeption_handler(
#             status_code=401,
#             detail={"error_code": "Invalid token"}
#         )
#     )
#     app.add_exception_handler(
#         RevokeToken,
#         create_exeption_handler(
#             status_code=403,
#             detail={"error_code": "Token revoked"}
#         )
#     )
#     app.add_exception_handler(
#         BooklyExeption,
#         create_exeption_handler(
#             status_code=500,
#             detail={"error_code": "Internal server error"}
#         )
#     )
#     app.add_exception_handler(
#         BookNotFound,
#         create_exeption_handler(
#             status_code=404,
#             detail={"error_code": "Book not found"}
#         )
#     )
#     app.add_exception_handler(
#         TagAlreadyExists,
#         create_exeption_handler(
#             status_code=400,
#             detail={"error_code": "Tag already exists"}
#         )
#     )
#     app.add_exception_handler(
#         AccountIsNotVerified,
#         create_exeption_handler(
#             status_code=403,
#             detail={"error_code": "Account is not verified"}
#         )
#     )
#     @app.exception_handler(500)
#     async def internal_server_error(request,exc):
#         return JSONResponse(
#             status_code=500,
#             content={"error_code": "Internal server error", "detail": str(exc)}
#         )