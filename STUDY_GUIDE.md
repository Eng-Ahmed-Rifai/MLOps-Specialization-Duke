# 🚀 Duke University MLOps Specialization — Comprehensive Study Guide

**Author:** Eng. Ahmed Rifai  
**Credential:** [I1THK805BQLF](https://www.coursera.org/account/accomplishments/specialization/I1THK805BQLF) (Verified 100% Mastery across all 4 Courses)  
**Instructors:** Noah Gift & Alfredo Deza (Duke University / Pragmatic AI Labs)  
**Target:** Production MLOps Engineering, CI/CD Automation, Cloud Platforms (AWS SageMaker, Azure ML), and Tooling (MLflow, ONNX, Hugging Face).

---

## 📑 Table of Contents
1. [Course 1: Python Essentials for MLOps](#course-1-python-essentials-for-mlops)
2. [Course 2: DevOps, DataOps, MLOps Foundations](#course-2-devops-dataops-mlops-foundations)
3. [Course 3: Cloud MLOps Platforms (AWS SageMaker & Azure ML)](#course-3-cloud-mlops-platforms-aws-sagemaker--azure-ml)
4. [Course 4: MLOps Tools (MLflow, Hugging Face & ONNX)](#course-4-mlops-tools-mlflow-hugging-face--onnx)

---

## Course 1: Python Essentials for MLOps

### 1. Production CLI Engineering
- Building modular command-line interfaces using `click` or `argparse`.
- Structuring Python applications with clean separation between CLI logic, domain business logic, and infrastructure adapters.

### 2. Quality Gates & Continuous Integration
- **Testing**: Test-Driven Development (TDD), parameterized testing with `pytest`, fixtures, and coverage enforcement (`pytest --cov=src --cov-fail-under=90`).
- **Code Hygiene**: Automated formatting with `black`/`ruff`, linting with `flake8`, and static type checking with `mypy`.
- **GitHub Actions**: Automating test execution on pull requests across Python matrix versions (`3.10`, `3.11`, `3.12`).

---

## Course 2: DevOps, DataOps, MLOps Foundations

### 1. DevOps & Kaizen Principles
- **Kaizen (Continuous Improvement)**: Eliminating waste (Muda), automating repetitive manual deployments, and reducing Mean Time to Resolution (MTTR).
- **Twelve-Factor App Methodology**: Declarative setup, explicit dependencies, config in environment variables, backing services as attached resources.

### 2. Containerization with Docker
- Multi-stage Docker builds to reduce image footprint:
  ```dockerfile
  # Build stage
  FROM python:3.11-slim as builder
  WORKDIR /app
  COPY requirements.txt .
  RUN pip install --user -r requirements.txt

  # Production runtime stage
  FROM python:3.11-slim
  WORKDIR /app
  COPY --from=builder /root/.local /root/.local
  COPY src/ /app/src/
  ENV PATH=/root/.local/bin:$PATH
  CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]
  ```

### 3. DataOps & Data Version Control (DVC)
- Versioning multi-gigabyte datasets and trained model weights outside Git while maintaining Git-like tracking (`dvc.yaml`, `dvc add data/`).
- Storing binary blobs in remote S3 buckets with pointer hashes checked into Git.

---

## Course 3: Cloud MLOps Platforms (AWS SageMaker & Azure ML)

```mermaid
flowchart LR
    Data["Data in S3 / Blob Storage"] --> Train["SageMaker / Azure ML Training Cluster"]
    Train --> Eval["Automated Evaluation Gate"]
    Eval --> Reg["Model Registry (MLflow / SageMaker)"]
    Reg --> Deploy["Managed Online Endpoint (A/B Test / Blue-Green)"]
    Deploy --> Monitor["Data Drift & Latency Monitoring"]
```

### 1. Amazon Web Services (AWS)
- **SageMaker**: Managed training jobs, processing jobs, hyperparameter tuning, model registry, serverless and real-time endpoints.
- **Pipelines & Step Functions**: DAG workflow orchestration triggering data preprocessing, distributed training, and automated endpoint deployment.

### 2. Microsoft Azure ML
- **Azure ML Studio**: Workspaces, compute instances, compute clusters, registered datasets, and environments.
- **Managed Online Endpoints**: Production model deployment with built-in blue/green traffic splitting and auto-scaling.

---

## Course 4: MLOps Tools (MLflow, Hugging Face & ONNX)

### 1. MLflow Lifecycle Management
- **Tracking**: Logging parameters (`mlflow.log_param`), metrics across training epochs (`mlflow.log_metric`), and model artifacts.
- **Model Registry**: Staging models through explicit lifecycle states (`None` $\to$ `Staging` $\to$ `Production` $\to$ `Archived`).

### 2. ONNX (Open Neural Network Exchange)
- Exporting trained neural networks from PyTorch/TensorFlow to the vendor-neutral ONNX format:
  ```python
  torch.onnx.export(model, dummy_input, "model.onnx", input_names=["input"], output_names=["output"])
  ```
- **ONNX Runtime**: Hardware-optimized inference across CPU and GPU backends, dramatically slashing inference latency.

### 3. Hugging Face Ecosystem
- Publishing models with detailed Model Cards detailing intended use, limitations, and evaluation metrics.
- Rapid deployment of interactive demonstrations using Gradio hosted on Hugging Face Spaces.
