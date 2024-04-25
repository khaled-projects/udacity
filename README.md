
Coworking Space Analytics API Deployment Guide

Welcome to the deployment guide for the Coworking Space Analytics API! This guide is designed to streamline the deployment process of the analytics API on Kubernetes.

Getting Started
Dependencies

Ensure that you have the following tools installed:

Python (3.6+)
Docker
kubectl
AWS CLI
helm
GitHub
Setup
1. Create an EKS Cluster

Utilize eksctl to create an EKS cluster tailored to your application's requirements. After creating the cluster, update the Kubeconfig to enable seamless interaction.
  eksctl create cluster --name my-cluster --region us-east-1 --nodegroup-name my-nodes --node-type t3.small --nodes 1 --nodes-min 1 --nodes-max 2
  aws eks --region us-east-1 update-kubeconfig --name my-cluster
2. Configure a Database for the Service

Apply YAML configurations to set up the Postgres database, ensuring proper configuration of PVC, PV, ConfigMap, and the Postgres deployment.

  kubectl apply -f pvc.yaml
  kubectl apply -f pv.yaml 
  kubectl apply -f configmap.yaml
  kubectl apply -f postgresql-deployment.yaml
3. Build the Analytics Application Locally

Install dependencies and run the application locally to ensure functionality.
 
 apt update && apt install -y build-essential libpq-dev
 pip install --upgrade pip setuptools wheel
 pip install -r requirements.txt
Set necessary environment variables and run the application:

 bash:
 export DB_USERNAME=myuser
 export DB_PASSWORD=${POSTGRES_PASSWORD}
 export DB_HOST=127.0.0.1
 export DB_PORT=5433
 export DB_NAME=mydatabase
 python app.py
4. Verify the Application

Generate reports for check-ins grouped by dates and user visits:

 curl <BASE_URL>/api/reports/daily_usage
 curl <BASE_URL>/api/reports/user_visits
5. Deploy the Analytics Application

Proceed with the deployment process, consisting of Dockerizing the application, setting up Continuous Integration with CodeBuild, and deploying the application on Kubernetes.

6. Dockerize the Application

Update Docker and build the Docker image:
 apt update && apt install -y docker-ce docker-ce-cli containerd.io
 docker build -t coworking-analytics .
7. Set up Continuous Integration with CodeBuild

Create an Amazon ECR repository, configure CodeBuild, and automate Docker image pushing upon repository updates.

8. Deploy the Application

Deploy the application using the provided Kubernetes configuration file:

 
 kubectl apply -f coworking.yaml
9. Setup CloudWatch Logging

Run the following commands to set up CloudWatch logging:


aws iam attach-role-policy --role-name my-worker-node-role --policy-arn arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
aws eks create-addon --addon-name amazon-cloudwatch-observability --cluster-name my-cluster-name
Replace my-worker-node-role and my-cluster-name with your EKS cluster's Node Group's IAM role and name respectively.

Trigger logging by accessing your application.

This revised deployment guide provides a clearer, more concise overview of the steps involved in deploying the Coworking Space Analytics API on Kubernetes.
