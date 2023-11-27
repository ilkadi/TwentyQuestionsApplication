#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from typing import List

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

from model_adapter import ModelAdapter

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

model_path = "../model"

model_adapter = ModelAdapter(model_path)


class QuestionAnswer(BaseModel):
    question: str
    answer: str


class SessionData(BaseModel):
    qa_list: List[QuestionAnswer]
    final_guess: str


app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, Please call predict with expected JSON input"}


@app.post("/predict")
def predict(session: SessionData):
    logger.info("request received %s", session.dict())
    session_data_dict = session.dict()
    return model_adapter.process_session(session_data_dict)


# =============================================================================
# EXECUTE
# =============================================================================
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9001)
