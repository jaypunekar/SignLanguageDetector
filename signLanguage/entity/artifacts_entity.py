from dataclasses import dataclass

@dataclass
class DataIngestionArtifact:
    data_zip_file_path: str
    feature_store_path: str

class DataValidationArtifact:
    def __init__(self, validation_status: bool):
        self.validation_status = validation_status

@dataclass
class ModelTrainerArtifact:
    trained_model_file_path: str
