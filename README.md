# Scalable Microservices Architecture on AWS

## Overview

This project demonstrates how to design, develop, deploy, and manage a scalable microservices architecture using Amazon Web Services (AWS). It specifically focuses on building a crypto application that is structured as microservices, allowing for independent development, seamless updates, and minimal downtime.

The application is built using Python and deployed on AWS, utilizing various AWS services to ensure scalability, reliability, and high availability.

### Key Features

- **Microservices Architecture:** The project divides the application into independent microservices (e.g., a product service, a login service), enabling developers to work on isolated components without affecting the rest of the system.
- **Scalability and Reliability:** With AWS services like ECS, CodePipeline, and Load Balancers, the application can scale as needed, ensuring high availability and minimal downtime.
- **Continuous Integration and Deployment (CI/CD):** Code changes are automatically pushed through a CI/CD pipeline for seamless updates and deployment.
- **Separation of Concerns:** Teams can work independently on their respective microservices (e.g., the Product team and Login team) without interference.

## Project Architecture

The project follows a microservices architecture, where different services are isolated and handle specific functionality within the application. This separation ensures that:

- Changes made to one service do not affect others (e.g., modifying the Login service will not impact the Product service).
- Each service can scale independently based on its specific load.

The architecture is powered by several AWS services, including:

- **AWS CodeCommit:** For version control of the source code.
- **AWS CodePipeline:** For automating the build, test, and deployment process.
- **AWS ECS (Elastic Container Service):** For running and managing Docker containers, ensuring the application is highly available and can scale automatically.
- **AWS Load Balancer:** For distributing traffic across multiple instances of the application, ensuring optimal performance and user access.

![awsprojarch drawio](https://github.com/user-attachments/assets/c8563f92-6323-4e77-9636-eda87d850fa4)

### How It Works

1. **Development:**

   The code for the application is divided between two teams:

   - **Product Team:** Responsible for the product-related functionality.
   - **Login Team:** Manages the login-related features.

   Each team works independently on their respective services.

2. **Code Commit:**

   Developers push code changes to **AWS CodeCommit**, a source control service where the project is hosted.

3. **Continuous Integration/Continuous Deployment (CI/CD):**

   - Changes in the CodeCommit repository trigger AWS CodePipeline.
   - CodePipeline automatically builds and tests the code, then deploys the latest version to the AWS ECS cluster.

4. **Deployment on AWS ECS:**

   The application is deployed to **AWS Elastic Container Service (ECS)**, where it runs inside Docker containers. ECS manages the deployment, scaling, and monitoring of the containers.

5. **Load Balancing:**

   AWS **Load Balancers** ensure that incoming traffic is distributed evenly across the containers. This ensures that users can always access the application without delays or downtime, even during peak traffic times.

6. **Scalability:**

   With this architecture, scalability is ensured. Both the **Product** and **Login** teams can develop and deploy their services independently, without impacting each other's work. Additionally, the application can automatically scale based on traffic, ensuring high availability and service reliability.

## Key Concepts and Benefits of Microservices in This Project

- **Isolation of Services:** Each service can be developed, tested, deployed, and scaled independently, reducing dependencies between different parts of the application.
- **Resilience:** Failure in one microservice does not bring down the entire system, making the application more robust and fault-tolerant.
- **Independent Deployment:** Services can be updated independently without affecting the overall application. For instance, changes to the login page can be made without affecting the product page.
- **Improved Development Velocity:** Teams can work concurrently on different services, speeding up the development process.
- **Scalability:** The application can easily scale as traffic grows, since each microservice can be scaled independently based on its load.
- **High Availability:** Using AWS infrastructure, the system ensures high availability, with load balancers distributing traffic to healthy instances of the application.

### Technologies Used

- **Python:** The application is built using Python for back-end functionality.
- **AWS Services:**
  - **AWS CodeCommit** for version control.
  - **AWS CodePipeline** for CI/CD.
  - **AWS ECS** (Elastic Container Service) for container management.
  - **AWS Load Balancer** for traffic distribution and high availability.
- **Docker:** For containerizing the microservices.
- **AWS CloudWatch:** For monitoring and logging application performance.

# Video Tutorial

For a complete hands-on walkthrough of the project, watch the video tutorial linked below.

https://github.com/user-attachments/assets/524d69f8-9e7d-498c-95ad-5963dced5fcb
