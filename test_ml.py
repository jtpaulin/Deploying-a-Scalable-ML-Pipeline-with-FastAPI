import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from ml.data import process_data
from ml.model import train_model, compute_model_metrics


# Test that process_data returns numpy arrays for features and labels
def test_process_data_output_type():
    """
    Ensure that process_data returns X and y as np.arrays.
    """
    # Dummy data
    import pandas as pd
    df = pd.DataFrame({
        "feature1": [1, 2],
        "feature2": ["A", "B"],
        "salary": [0, 1]
    })
    categorical_features = ["feature2"]
    X, y, _, _ = process_data(df, categorical_features=categorical_features, label="salary", training=True)

    assert isinstance(X, np.ndarray), "X should be a numpy array"
    assert isinstance(y, np.ndarray), "y should be a numpy array"


# Test that train_model returns a RandomForestClassifier
def test_train_model_algorithm():
    """
    Ensure that train_model returns a RandomForestClassifier instance.
    """
    X_train = np.array([[0, 1], [1, 0]])
    y_train = np.array([0, 1])
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier), "Model should be a RandomForestClassifier"


# Test that compute_model_metrics returns floats between 0 and 1
def test_compute_model_metrics_range():
    """
    Ensure compute_model_metrics returns precision, recall, fbeta all between 0 and 1.
    """
    y_true = np.array([0, 1, 1, 0])
    y_preds = np.array([0, 1, 0, 0])
    precision, recall, fbeta = compute_model_metrics(y_true, y_preds)
    for metric in (precision, recall, fbeta):
        assert isinstance(metric, float), "Metric should be a float"
        assert 0 <= metric <= 1, "Metric should be between 0 and 1"