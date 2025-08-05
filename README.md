# Data Orchestrator

This project provides two robust solutions for orchestrating data workflows on AWS.  
Both leverage Kubernetes (EKS) and Docker for scalable deployments, but differ in their storage and interface components.
### Dataset Link: https://www.kaggle.com/datasets/sohaibanwaar1203/taxidemandfarepredictiondataset?select=yellow_tripdata_2015-03.csv

---

## Solutions Overview

| Solution                | Storage | UI      | Main Technologies           |
|-------------------------|---------|---------|----------------------------|
| **1. EKS + Docker + S3**        | S3      | None    | EKS, Docker, AWS S3        |
| **2. EKS + Docker + DynamoDB + UI** | DynamoDB | Streamlit | EKS, Docker, DynamoDB, Streamlit |

---

## Main Features

Both solutions include:

1. **Scalable Kubernetes (EKS) Deployment:**  
   Containerized workloads managed by AWS EKS.

2. **Dockerized Microservices:**  
   All components packaged for easy deployment and portability.

3. **Cloud Storage:**  
   - **Solution 1:** AWS S3 for CSV data storage  
   - **Solution 2:** DynamoDB for NoSQL data management

4. **Workflow Automation:**  
   Modular design for data ingestion, processing, and orchestration.

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
├── app_eks_dynamodb_streamlit/
│  └── app.py        (Streamlit app + DynamoDb + Docker + EKS -> Solution 2)
│  └── ...           (other supporting utils and configs)
├── app_eks_s3/      (CLI + S3 + Docker + EKS -> Solution 1)
├── README.md
├── requirements.txt 
```

---

## Contributing

Pull requests and issues are welcome!

---
