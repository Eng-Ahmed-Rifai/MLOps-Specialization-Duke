"""ONNX Model Optimization and Inference Helper.

Enables cross-framework neural network serialization (PyTorch/TensorFlow to ONNX)
and low-latency scoring using ONNX Runtime.
"""

from typing import Dict, Any, List, Optional
import os


class ONNXRuntimeEngine:
    """Manages ONNX inference sessions with execution providers."""

    def __init__(self, model_path: str, execution_providers: Optional[List[str]] = None):
        self.model_path = model_path
        self.execution_providers = execution_providers or ["CPUExecutionProvider"]

    def validate_model_path(self) -> bool:
        """Verify model file exists and has .onnx extension."""
        return os.path.isfile(self.model_path) and self.model_path.endswith(".onnx")
