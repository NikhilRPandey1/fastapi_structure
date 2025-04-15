from fastapi import  Depends, HTTPException, status
from sqlalchemy.future import select
from api.accounts.schemas.users import LoginRequest, SignupRequest
from sqlalchemy.ext.asyncio import AsyncSession
from db.session import get_db
from api.accounts.models.user import User
from core.helper import verify_password, create_access_token


class UserAuth:

    async def login(self, schema: LoginRequest, db: AsyncSession = Depends(get_db)):
        query_stmt = select(User).where(User.email == schema.email)
        result = await db.execute(query_stmt)

        user = result.scalar_one_or_none()

        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email",
            )

        if not verify_password(schema.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid password",
            )

        token = create_access_token({"sub": user.email})

        return {"message": "Login success", "status": True, "data": token}

    async def sign_up(self, schema: SignupRequest, db: AsyncSession = Depends(get_db)):
        user = User(**schema.model_dump())

        db.add(user)
        await db.commit()
        await db.refresh(user)

        del user.password
        return {"message": "Signup success", "status": True, "data": user}

