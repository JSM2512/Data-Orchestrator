# Data Orchestrator

This project provides two robust solutions for orchestrating data workflows on AWS.  
Both leverage Kubernetes (EKS) and Docker for scalable deployments, but differ in their storage and interface components.
### Dataset Link: https://www.kaggle.com/datasets/sohaibanwaar1203/taxidemandfarepredictiondataset?select=yellow_tripdata_2015-03.csv

**This repository was used to display 4 major distributed system design principles:**

1. **Scalability by Replication in Kubernetes (EKS):**  
   Kubernetes deployments in EKS use replica sets to scale workloads horizontally, ensuring the system can handle increased load efficiently.

2. **High Availability with Multi-Region S3 & DynamoDB:**  
   AWS S3 and DynamoDB are configured for multi-region access, providing data redundancy and minimizing downtime in case of regional failures.

3. **Fault Tolerance via Multiple Replicas and Pod Recreation:**  
   The system automatically recovers from node or pod failure using Kubernetes' self-healing features, maintaining service continuity through active replicas.

4. **Containerization by Docker:**  
   All microservices and workflow components are packaged as Docker containers for environment consistency, rapid deployment, and portability.

---

## Solution Architectures

| Solution | Storage | UI | Tech Stack | Description |
|----------|---------|----|------------|-------------|
| **1. EKS + Docker + S3** | AWS S3 | None | EKS, Docker, S3 | Containerized services on EKS interact with AWS S3 for distributed storage and workflow orchestration. |
| **2. EKS + Docker + DynamoDB + UI** | DynamoDB | Streamlit | EKS, Docker, DynamoDB, Streamlit | Improved version: adds a Streamlit UI for user interaction, and DynamoDB for fast, scalable NoSQL storage. |

---

## How Each Principle Is Demonstrated

**Both solutions implement:**

- **Scalability:**  
  Multiple replicas and scaling in EKS deployments (`replicas` in deployment manifest).

- **High Availability:**  
  S3 and DynamoDB support multi-region redundancy; EKS schedules pods across multiple nodes.

- **Fault Tolerance:**  
  Kubernetes automatically recreates pods and maintains the desired number of active nodes.

- **Containerization:**  
  All services use Docker for packaging and deployment.

---

## Solution 1: EKS + Docker + S3

### Check the report Below:
[![PDF](https://img.shields.io/badge/View%20PDF-Taxi_Demand_Fare_Report-blue)](https://github.com/JSM2512/Data-Orchestrator/blob/main/app_eks_s3/Taxi_Demand_Fare_Report.pdf)

**Description:**  
A cloud-native orchestration pipeline using Docker containers on EKS, storing and retrieving data from AWS S3.

**Architecture:**
```
+---------------------+
|    AWS EKS Cluster  |
|  +---------------+  |
|  |  Dockerized   |  |
|  | Microservices |  |
|  +---------------+  |
+---------------------+
            |
            v
      +-------------+
      |    S3       |
      +-------------+
```

**Setup & Usage:**
1. **Build Docker images:**  
   `docker build -t my-service .`
2. **Push images to ECR (Elastic Container Registry)**
3. **Deploy to EKS via Kubernetes manifests**
4. **Configure AWS credentials for S3 access**

**Pros:**  
- Simple, reliable cloud storage  
- Good for batch workflows

---

## Solution 2: EKS + Docker + DynamoDB + UI (Improved Version)

**Description:**  
An enhanced solution with a web UI (Streamlit) for monitoring and managing workflows, using DynamoDB for fast NoSQL storage.

**Architecture:**
```
+---------------------+
|    AWS EKS Cluster  |
|  +---------------+  |
|  |  Dockerized   |  |
|  | Microservices |  |
|  +---------------+  |
+---------------------+
      |         |
      v         v
+--------+ +--------+
|  UI    | | DynamoDB|
|Streamlit| +--------+
+--------+ 
```

**Setup & Usage:**
1. **Build Docker images:**  
   `docker build -t my-service .`
2. **Push images to ECR**
3. **Deploy to EKS**
4. **Set up DynamoDB table and AWS credentials**
5. **Access UI via Streamlit (URL or port)**

**Pros:**  
- Real-time UI for workflow management  
- NoSQL data handling with DynamoDB  
- Extensible and user-friendly

---

## Getting Started

### Prerequisites
- AWS CLI configured
- kubectl installed
- Docker
- (Optional) Streamlit for UI (Solution 2)

### Quick Start (Solution 2 shown)
```sh
# Build and push Docker images
docker build -t data-orchestrator-ui .
# ...push to ECR

# Apply Kubernetes manifests
kubectl apply -f k8s/deployment.yaml

# Access Streamlit UI
streamlit run app.py
```

---

## Folder Structure

```
data-orchestrator/
├──app_eks_s3/                    # Solution 1: S3-based workflow
│  ├── Dockerfile
│  ├── boto_script2.py
│  ├── boto_script3.py
│  ├── sql4.py
│  ├── sql_final.py
├──app_eks_dynamodb_streamlit/    # Solution 2: DynamoDB + Streamlit UI
│  ├── DockerFile
│  ├── config.py
│  ├── dynamodb_client.py
│  ├── streamlit_app.py
│  ├── deployments.yaml
├── README.md
├── requirements.txt 
```

---

## Contributing

Pull requests and issues are welcome!

---
