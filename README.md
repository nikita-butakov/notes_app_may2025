# 📝 Notes App — DevOps Portfolio Project (Flask + AWS)

Hi! I’m Nikita, a DevOps Engineer, and this is my personal project where I built and deployed a containerized note-taking web application with **Flask**, **PostgreSQL**, and using AWS services such as **ECS Fargate**, **RDS**, and **Application Load Balancer**. The project follows DevOps best practices including CI/CD with GitHub Actions.

---

## 🔗 Demo & Repository

- 📂 **Project Repository**: [github.com/nikita-butakov/notes_app_may2025](https://github.com/nikita-butakov/notes_app_may2025)

---

## 🛠️ Tech Stack

- ⚙️ **Flask** – Python web backend  
- 🐳 **Docker** – containerization  
- ☁️ **Amazon ECS (Fargate)** – serverless app hosting  
- 🛢️ **Amazon RDS (PostgreSQL)** – managed relational database  
- 📦 **Amazon ECR** – Docker image registry  
- 🔁 **GitHub Actions** – CI/CD automation  
- 🌐 **Amazon Route 53 / Cloudflare** – DNS and domain setup (domain steps not included in this repo)  
- 📊 **CloudWatch** – monitoring and logging  
- 🧱 **Application Load Balancer** – traffic distribution  
- 📶 **Target Group (TG)** – routes traffic to ECS tasks  
- 🔐 **Security Groups (SG)** – network access control  
- 🌍 **VPC with Private Subnets** – isolated backend infrastructure  

---

## 🧱 Infrastructure Overview

- ✅ **VPC** with public (for ALB) and private (for RDS) subnets  
- ✅ **Security Groups** for ALB, ECS Tasks, and RDS  
- ✅ **Application Load Balancer** with Target Group  
- ✅ **Amazon RDS** (PostgreSQL) with private subnet placement  
- ✅ **Amazon ECR** hosting backend and frontend Docker images  
- ✅ **ECS Fargate Cluster** running both containers  
- ✅ **CI/CD Pipeline** via GitHub Actions (auto-deploy on push)  
- ✅ **HTTPS** enabled with AWS ACM  
- ✅ **Domain** support via Route 53 or Cloudflare  

---

## 🔧 App Features

- 📝 Add, edit, and delete notes  
- 📡 REST API available at `/api/notes`  
- 🔐 Secure, scalable, stateless architecture  
- 🚀 Automated deployment pipeline  
- 📈 Monitoring and logging with CloudWatch  

---

## 🖼️ Architecture Diagram

<img src="./architecture_diagram.png" alt="Architecture Diagram" width="100%" />

📎 Also available as a [PDF version](./architecture_diagram.pdf) for printing or zooming.


---

## 📸 Screenshots

---

### ⚖️ Application Load Balancer

<p align="center">
  <img src="./screenshots/ALB1.jpg" width="600" />
</p>

<p align="center">
  <img src="./screenshots/ALB2.jpg" width="600" />
</p>

---

### 📦 Elastic Container Registry (ECR)

<p align="center">
  <img src="./screenshots/ECR.jpg" width="600" />
</p>

---

### 🐳 Elastic Container Service (ECS)

<p align="center">
  <img src="./screenshots/ECS1.jpg" width="600" />
</p>

<p align="center">
  <img src="./screenshots/ECS2.jpg" width="600" />
</p>

<p align="center">
  <img src="./screenshots/ECS3.jpg" width="600" />
</p>

---

### 🛢️ Amazon RDS (PostgreSQL)

<p align="center">
  <img src="./screenshots/RDS.jpg" width="600" />
</p>

---

### 🌐 Networking (VPC, Subnets, SG, TG)

<p align="center">
  <img src="./screenshots/SG.jpg" width="600" />
</p>

<p align="center">
  <img src="./screenshots/Subnets.jpg" width="600" />
</p>

<p align="center">
  <img src="./screenshots/TG.jpg" width="600" />
</p>

<p align="center">
  <img src="./screenshots/VPC.jpg" width="600" />
</p>

---

### 🔁 GitHub Actions (CI/CD)

<p align="center">
  <img src="./screenshots/gitactions.jpg" width="600" />
</p>

<p align="center">
  <img src="./screenshots/gitactions2.jpg" width="600" />
</p>

---

### 🧾 Web App Interface

<p align="center">
  <img src="./screenshots/index1.jpg" width="600" />
</p>

<p align="center">
  <img src="./screenshots/index_edit.jpg" width="600" />
</p>

---

## 👤 Author

**Nikita Butakov**  
DevOps • Cloud • Automation

- 🔗 [LinkedIn](https://www.linkedin.com/in/nikita-butakov/)  
- 🐙 [GitHub](https://github.com/nikita-butakov)
