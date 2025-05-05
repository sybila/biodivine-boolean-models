class MissingIdException(Exception):
    def __init__(self, model_id, message="Missing cellcollective_id for model"):
        self.model_id = model_id
        super().__init__(f"{message}: {model_id}")
