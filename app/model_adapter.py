import logging
from pathlib import Path


QUESTION_COUNT_MAX = 20
logger = logging.getLogger(__name__)


class ModelAdapter:
    def __init__(self, model_path):
        self.label_set = ["O"]
        model_dir = Path(model_path, "model")
        self.model_artifacts = model_dir

    @staticmethod
    def process_session(session_data_dict):
        answered_questions_count = len(session_data_dict["qa_list"])
        if answered_questions_count >= QUESTION_COUNT_MAX:
            session_data_dict["final_guess"] = "42"
            return session_data_dict
        else:
            next_index = answered_questions_count + 1
            new_question = {f"Question N{next_index}?": ""}
            session_data_dict["qa_list"].append(new_question)
            return session_data_dict
