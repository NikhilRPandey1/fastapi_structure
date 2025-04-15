from fastapi import  APIRouter

from api.accounts.views.auth import UserAuth

account = APIRouter(prefix="/auth")

account.add_api_route(path="/login", endpoint=UserAuth().login, methods=["POST"])
account.add_api_route(path="/signup", endpoint=UserAuth().sign_up, methods=["POST"])