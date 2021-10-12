from typing import Optional
from fastapi import FastAPI, Header, HTTPException
from calculation_enum import PostCalculation, GetCalculation
from calculation_operator import CalculationOperator

app = FastAPI()


@app.post("/{operation}/")
async def read_item(operation, params: Optional[str] = "1", username: Optional[str] = Header(""),
                    password: Optional[str] = Header("")):
    if operation in list(map(lambda calc: calc.value, PostCalculation._member_map_.values())):
        return CalculationOperator.check_post_parameter_count(operation, params, username, password)
    else:
        raise HTTPException(status_code=405,
                            detail="Request method not supported")


@app.get("/{operation}/")
async def read_item(operation, params: Optional[str] = "1", username: Optional[str] = Header(""),
                    password: Optional[str] = Header("")):
    if operation in list(map(lambda calc: calc.value, GetCalculation._member_map_.values())):
        return CalculationOperator.check_get_parameter_count(operation, params, username, password)
    else:
        raise HTTPException(status_code=405,
                            detail="Request method not supported")
