# Distributed System Design Concept Showcase with AWS EKS, S3, Amazon ECR, Docker, and Kubernetes
Welcome to the COMP 6231 DSD Final Project, where we explore and 
### exemplify key concepts in Distributed System Design 
using cutting-edge technologies such as AWS EKS, AWS S3, Amazon ECR, Docker, and Kubernetes. Follow the outlined steps to delve into the intricacies of our project:
### DATASET LINK: https://www.kaggle.com/datasets/sohaibanwaar1203/taxidemandfarepredictiondataset?select=yellow_tripdata_2015-03.csv

## Data Storage on S3:

Create a new S3 bucket (bucket1) to efficiently store data files.
Establish a separate S3 bucket (bucket2) for data replication, with the flexibility to choose between same-region or cross-region replication. 
### (CONCEPT-1 Replication)
## Elastic Kubernetes Service (EKS) Cluster:

Set up a new EKS cluster to harness the power of Kubernetes for managing containerized applications seamlessly.
## Node Configuration:

Specify the desired number of EC2 instances (EKS Cluster Nodes) along with their instance types, such as t3.micro, m5.large, etc. We opted for t3.large (2vCPU's, 8GiB RAM) to align with our project requirements.
## Identity and Access Management:

Create IAM roles and users to ensure secure access and authorization, aligning with project-specific requirements.
## Autoscaling for Fault Tolerance:

Implement an autoscaling group during the EKS cluster setup to dynamically manage and maintain the desired number of Nodes at all times. 
### (CONCEPT-2 Fault Tolerance)
## Data Processing with Python:

Develop a Python script utilizing Boto3 to retrieve data CSV from S3.
Leverage Pandas to run queries on the CSV and generate desired results.
## Containerization with Docker:

Dockerize the Python script and upload the resulting image to Amazon ECR. 
### (CONCEPT-3 Containerization)
## Pod Creation with Kubernetes:

Utilize Kubernetes to create Pods from the Docker image within the EKS Cluster Nodes (EC2 instances).
## Scalability with Deployments and Services:

Employ Deployment and Service YAML files to efficiently scale Pods up and down within the EKS Cluster. 
### (CONCEPT-4 Scalability)
