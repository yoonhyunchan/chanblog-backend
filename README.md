<p align="center">
    <img src="https://skillicons.dev/icons?i=python,fastapi,kubernetes,docker" />
</p>
# Backend Blog - For Kubernetes Deployment 

A microservices-based backend blog application deployed on Kubernetes with AWS EC2 and ALB Ingress Controller.

## 🏗️ Architecture Overview

This project consists of four microservices:
- **Article Service** - Blog post management
- **Category Service** - Category management  
- **Auth Service** - User authentication and authorization
- **Image Service** - Image upload and storage

All services are containerized and deployed on Kubernetes with shared database configuration.

## 🚀 Quick Start

### Prerequisites

- Kubernetes cluster (on AWS EC2 Instances)
- `kubectl` configured to access your cluster
- AWS ALB Ingress Controller installed
- Harbor container registry access
- PostgreSQL database (AWS RDS)

### 1. Build and Push Images

```bash
# Build all services
docker build -t harbor.chanandy.internal/backend/{project}:latest ./{project}

# Push to Harbor registry
docker push harbor.chanandy.internal/backend/{project}:latest

```

### 2. Deploy to Kubernetes

First, use ArgoCD to manage and deploy the services via GitOps.

ex) Deploy services in the following order:

```bash
# 1. Create namespace
kubectl apply -f {project}/manifest/1_ns.yaml

# 2. Create ConfigMap (shared database config)
kubectl apply -f {project}/manifest/2_configmap.yaml

# 3. Deploy all services
kubectl apply -f {project}/manifest/3_deployment.yaml
kubectl apply -f {project}/manifest/4_svc.yaml
kubectl apply -f {project}/manifest/5_ingress.yaml
```

## 📋 Kubernetes Resources

### Namespace
- **Name**: `backend`
- **Purpose**: Isolates all backend services

### ConfigMap
- **Name**: `dbconfig`
- **Purpose**: Shared database configuration for all services
- **Mount**: `/app/.env` in each container


### Services
All services are exposed as `NodePort`:
- **Article Service**: `article-service`
- **Category Service**: `category-service` 
- **Auth Service**: `auth-service`

### Ingress
- **Class**: AWS ALB Ingress Controller
- **Domain**: `api.chanandy.store`
- **SSL**: AWS ACM certificate

#### Ingress Rules
- `/articles/*` → Article Service
- `/categories/*` → Category Service  
- `/auth/*` → Auth Service
