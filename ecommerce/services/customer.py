from fastapi import HTTPException
from schema.customer import customers, CustomerCreate

class CustomerService:

    @staticmethod
    def validate_username(payload: CustomerCreate):
        username: str = payload.username
        for customer in customers:
            if customer.username == username:
                raise HTTPException(status_code=400, detail="Customer with username already exists")
        return payload
        