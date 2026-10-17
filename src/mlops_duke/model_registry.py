"""MLflow Experiment Tracker and Model Lifecycle Manager.

Standardizes MLflow run context, hyperparameter logging, metric tracking,
and staging transitions in the MLflow Model Registry.
"""

from typing import Dict, Any, Optional


class MLflowTracker:
    """Wrapper for standardized MLflow experiments and artifacts."""

    def __init__(self, experiment_name: str = "default_experiment", tracking_uri: Optional[str] = None):
        self.experiment_name = experiment_name
        self.tracking_uri = tracking_uri

    def format_run_metadata(
        self,
        params: Dict[str, Any],
        metrics: Dict[str, float],
        tags: Optional[Dict[str, str]] = None
    ) -> Dict[str, Any]:
        """Format parameters, metrics, and git metadata for logging."""
        metadata = {
            "experiment": self.experiment_name,
            "params": params,
            "metrics": metrics,
            "tags": tags or {"framework": "pytorch", "pipeline": "mlops_duke"}
        }
        return metadata
