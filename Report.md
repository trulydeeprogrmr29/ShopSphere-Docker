# ShopSphere Docker — Technical Project Report

**Project Title:** ShopSphere — Containerized E-Commerce Microservices  
**Author:** Deepak Chaudhary 
**Repository:** https://github.com/trulydeeprogrmr29/ShopSphere-Docker  
**Development Environment:** Ubuntu Linux  
**Date:** November 2026

---

## 1. Abstract

ShopSphere is a small e-commerce demonstration application developed to explore containerization and microservices orchestration using Docker and Docker Compose. The application separates user management, product information, and order handling into individual backend services.

An Nginx API gateway provides a single entry point for client requests and forwards traffic to the appropriate backend service. Docker Compose manages the containers, service dependencies, and health checks. The Orders service can be scaled horizontally to demonstrate load balancing across multiple replicas.

A browser-based dashboard provides an interactive interface for testing the application's API operations.

## 2. Objectives

The primary objectives of this project are:

1. Understand microservices architecture.
2. Containerize backend services using Docker.
3. Orchestrate multiple containers using Docker Compose.
4. Configure Nginx as a reverse proxy and API gateway.
5. Demonstrate service scaling and load balancing.
6. Implement health checks and service dependencies.
7. Integrate backend APIs with a browser-based frontend.
8. Publish the project source code through GitHub.

## 3. System Architecture

The application is composed of the following components:

### 3.1 Users Service

The Users service handles user-related operations. It is exposed internally on port 5001.

### 3.2 Products Service

The Products service provides product information and is exposed internally on port 5002.

### 3.3 Orders Service

The Orders service handles order-related operations. It communicates with the Users and Products services using environment-configured service URLs. Its internal port is 5003.

The Orders service can be scaled to multiple replicas using Docker Compose.

### 3.4 Nginx API Gateway

Nginx serves as the application gateway. It routes requests according to their URL paths:

- `/users` → Users service
- `/products` → Products service
- `/orders` → Orders service

The gateway also serves the interactive frontend from the mounted frontend directory.

### 3.5 Interactive Frontend

The frontend is implemented using HTML, CSS, and JavaScript. It provides controls to retrieve user details, retrieve product details, and interact with order functionality through HTTP requests.

## 4. Technology Stack

| Technology | Role |
|---|---|
| Docker | Containerization |
| Docker Compose | Container orchestration |
| Python | Backend implementation |
| Nginx | API gateway and reverse proxy |
| HTML | Frontend structure |
| CSS | Frontend styling |
| JavaScript | API interaction |
| Ubuntu Linux | Development environment |
| Git and GitHub | Version control and source hosting |

## 5. Implementation

### 5.1 Docker Image Construction

A common Dockerfile is used to build service-specific images. The `SERVICE` build argument selects the service implementation during image construction.

The resulting images are:

- `shop-users:1.0`
- `shop-products:1.0`
- `shop-orders:1.0`

### 5.2 Docker Compose Configuration

The Compose configuration defines the backend services and gateway. It specifies build contexts, image names, environment variables, health checks, restart policies, and service dependencies.

The Users and Products services include health checks. The Orders service waits for these dependencies to become healthy before starting.

### 5.3 Reverse Proxy Configuration

The Nginx configuration contains upstream definitions for backend services and routes requests based on URL paths.

The gateway is published on host port 8080, allowing the dashboard and API endpoints to be accessed through a single local address.

### 5.4 Load Balancing

The Orders service is scaled using:

```bash
docker compose up -d --scale orders=3
```

Nginx uses Docker's internal DNS resolver for dynamic service discovery of Orders replicas. This allows it to resolve the service name as the replica set changes.

Repeated requests through the gateway produced responses associated with different Orders container IDs, demonstrating traffic distribution across the replicas.

## 6. Testing and Verification

The project was tested in the local Ubuntu environment.

| Test | Procedure | Result |
|---|---|---|
| Compose validation | Run `docker compose config` | Passed |
| Service startup | Run `docker compose up -d` | Passed |
| Users API | Access Users endpoint through gateway | Passed |
| Products API | Access Products endpoint through gateway | Passed |
| Frontend integration | Open dashboard at `http://localhost:8080` | Passed |
| Orders scaling | Scale Orders to three replicas | Passed |
| Load balancing | Send repeated requests and inspect container IDs | Passed |
| Gateway integration | Access application through port 8080 | Passed |

### Example API Responses

Users endpoint example:

```json
{
  "id": 1,
  "name": "Deepak"
}
```

Products endpoint example:

```json
{
  "id": 101,
  "name": "Laptop",
  "price": 50000
}
```

These examples demonstrate successful API responses observed during local testing.

## 7. Execution Instructions

### Start the application

```bash
cd ~/shop-docker
docker compose up -d
```

### Verify service status

```bash
docker compose ps
```

### Access the dashboard

```text
http://localhost:8080
```

### Scale Orders

```bash
docker compose up -d --scale orders=3
```

### Stop the application

```bash
docker compose down
```

## 8. Advantages

- Modular service design.
- Independent containerization of backend components.
- Centralized request routing.
- Reproducible development environment.
- Service health monitoring.
- Demonstration of horizontal scaling.
- Easy local startup and shutdown.
- Interactive frontend for API testing.

## 9. Limitations

- The application is a demonstration project rather than a production-ready e-commerce system.
- Authentication and authorization are not implemented as production-grade mechanisms.
- Data persistence and database integration are limited by the current implementation.
- The local Docker Compose architecture is not directly equivalent to a managed cloud deployment.
- Public deployment requires platform-specific configuration for service networking and port binding.

## 10. Future Enhancements

Potential future improvements include:

1. Integrate a persistent database.
2. Implement user authentication and authorization.
3. Add a shopping cart and richer order workflow.
4. Introduce automated API tests.
5. Add CI/CD using GitHub Actions.
6. Add monitoring and centralized logging.
7. Deploy a public demo using Render or another cloud platform.
8. Add screenshots and a live demo URL to the README.

## 11. Conclusion

ShopSphere demonstrates the practical application of Docker containerization, Docker Compose orchestration, Nginx reverse proxy routing, and horizontal scaling in a microservices-based application.

The project successfully runs locally with an interactive dashboard and multiple backend services. It provides a foundation for further work in cloud deployment, automated testing, persistence, and production-oriented architecture.

## 12. References

- Docker documentation: https://docs.docker.com/
- Docker Compose documentation: https://docs.docker.com/compose/
- Nginx documentation: https://nginx.org/en/docs/
- Render documentation: https://render.com/docs
- Project repository: https://github.com/trulydeeprogrmr29/ShopSphere-Docker
