import jwt
from fastapi import HTTPException, Security, status
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
)
from passlib.context import CryptContext
from datetime import datetime, timedelta


class AuthHandler:
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    secret = "SECRET"

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def encode_token(self, user_id):
        payload = {
            "exp": datetime.utcnow() + timedelta(days=0, seconds=10),
            "iat": datetime.utcnow(),
            "sub": user_id,
        }
        print(payload)
        test = jwt.encode(payload, self.secret, algorithm="HS256")
        print(test)
        return jwt.encode(payload, self.secret, algorithm="HS256")

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=["HS256"])
            print(payload)
            print(payload["sub"])

        except jwt.ExpiredSignatureError:
            print("Expired")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Signature has expired"
            )

        except jwt.InvalidTokenError as e:
            print(e)
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        print(self.decode_token(auth.credentials))
        return self.decode_token(auth.credentials)
