# SRE Level 2 Test – Cloud Native Application

 Overview

This project demonstrates a complete **cloud-native application lifecycle**, including development, containerization, CI/CD, and Kubernetes deployment using Helm.

It was built as part of an SRE-level technical assessment, focusing on **automation, scalability, and reliability**.

---

 Architecture

The solution is composed of:

* **Python Application** (Flask-based)
* **Docker** for containerization
* **Kubernetes** for orchestration
* **Helm** for package management
* **GitHub Actions** for CI/CD
* **Backup Job** via CronJob
* **Horizontal Pod Autoscaler (HPA)** for scaling

---

 Project Structure

```
.
├── app/                    # Application source code
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── helm-chart/             # Helm chart for Kubernetes deployment
│   └── sre-app/
│       ├── templates/
│       │   ├── deployment.yaml
│       │   ├── service.yaml
│       │   ├── hpa.yaml
│       │   ├── configmap.yaml
│       │   ├── cronjob-backup.yaml
│       │   ├── pvc-backup.yaml
│       │   └── _helpers.tpl
│       ├── Chart.yaml
│       └── values.yaml
│
├── scripts/                # Backup scripts
│   ├── backup.sh
│   └── Dockerfile.backup
│
├── tests/                  # Unit tests
│   └── test_app.py
│
└── .github/workflows/      # CI/CD pipeline
    └── ci-cd.yml
```

---

Features

Application

* Lightweight Python API
* Dependency-managed via `requirements.txt`
* Test coverage included

Containerization

* Multi-stage Docker builds
* Separate container for backup process

Kubernetes (via Helm)

* Deployment with configurable replicas
* Service exposure
* ConfigMap support
* Persistent Volume Claim (PVC) for backups
* CronJob for automated backups

Autoscaling

* Horizontal Pod Autoscaler (HPA)
* CPU-based scaling

CI/CD Pipeline

* Automated pipeline using GitHub Actions
* Triggers:

  * Push to `main` and `develop`
  * Pull requests to `main`
* Pipeline stages:

  * Install dependencies
  * Run tests
  * Build Docker images
  * (Optional) Deploy

---

Getting Started

1. Clone the repository

```bash
git clone https://github.com/<your-username>/sre-level2-test.git
cd sre-level2-test
```

---

 2. Run locally

```bash
cd app
pip install -r requirements.txt
python app.py
```

---

3. Build Docker image

```bash
docker build -t sre-app ./app
```

---

4. Deploy with Helm

```bash
helm install sre-app ./helm-chart/sre-app
```

---

Running Tests

```bash
pytest tests/
```

---

CI/CD Workflow

The pipeline is defined in:

```
.github/workflows/ci-cd.yml
```

Main steps:

1. Checkout code
2. Install dependencies
3. Run tests
4. Build containers
5. Prepare deployment

---

Backup Strategy

* Backup handled via Kubernetes CronJob
* Script located in:

  ```
  scripts/backup.sh
  ```
* Persistent storage via PVC ensures data durability

---

Scalability & Reliability

* Stateless application design
* Horizontal scaling via HPA
* Automated deployments
* Separation of concerns (app vs backup)

---

Security Considerations

* CI/CD pipeline structured for validation before deployment
* Environment-based configuration via Helm values
* Containerized workloads reduce host dependency risks

---

Future Improvements

* Add observability (Prometheus + Grafana)
* Implement centralized logging (ELK/EFK stack)
* Add canary or blue/green deployments
* Integrate secrets management (Vault / Kubernetes Secrets)

---

👨‍💻 Author

Developed as part of an SRE technical assessment.

---

License

This project is for educational and evaluation purposes.
