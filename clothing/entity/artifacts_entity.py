from dataclasses import dataclass
# Data ingestion artifacts return the file path of the train, test and valid data after ingestion
@dataclass
class DataIngestionArtifacts:
    train_file_path: str
    test_file_path: str
    valid_file_path: str

# 2 paths and returning the number of classes (11)
@dataclass
class DataTransformationArtifacts:
    transformed_train_object: str 
    transformed_test_object: str
    number_of_classes: int

@dataclass
class ModelTrainerArtifacts:
    trained_model_path: str

@dataclass
class ModelEvaluationArtifacts:
    is_model_accepted: bool
    all_losses: str


@dataclass
class ModelPusherArtifacts:
    bucket_name: str
    s3_model_path: str
