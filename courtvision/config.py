from pathlib import Path

from pydantic_settings import BaseSettings


class CourtVisionTrainingSettings(BaseSettings):
    datasets_path: Path
    ball_models_dir: Path
    ball_model_name: str
    ball_checkpoints_dir: Path
    ball_checkpoints_weights_only: Path

    wb_project: str
    wb_save_dir: str

    class Config:
        extra = "ignore"
        env_prefix = "COURTVISION_"
        env_file = ".env"
        env_file_encoding = "utf-8"


class CourtVisionInferenceSettings(BaseSettings):
    # Tracker(s)
    ball_tracker_num_particles: int = 10_000

    # Models
    ball_detection_model_path: Path
    player_detection_model_path: Path
    # Calibrations
    camera_info_path: Path
    # Visualizations
    court_mesh_path: Path
    # Data
    annotation_path: Path

    class Config:
        extra = "ignore"
        env_prefix = "COURTVISION_"
        env_file = ".env"
        env_file_encoding = "utf-8"
