import os
import mlflow
import mlflow.sklearn
from sklearn.linear_model import LinearRegression
import numpy as np

# add Endpoint to MLflow & MinIO
os.environ["MLFLOW_TRACKING_URI"] = "http://localhost:5000"
os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://localhost:9000"
os.environ["AWS_ACCESS_KEY_ID"] = "minioadmin"
os.environ["AWS_SECRET_ACCESS_KEY"] = "minioadmin123"
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

mlflow.set_experiment("cilium-lab-smoke-test")

# train model
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])
model = LinearRegression().fit(X, y)

with mlflow.start_run(run_name="baseline-linear-model") as run:
    mlflow.log_param("model_type", "LinearRegression")
    mlflow.log_metric("r2_score", model.score(X, y))
    mlflow.sklearn.log_model(model, artifact_path="model")

    print(f"Run ID: {run.info.run_id}")
    print(f"Artifact URI: {run.info.artifact_uri}")