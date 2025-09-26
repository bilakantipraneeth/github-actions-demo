# Day 4 (Module 4): Securing Infrastructure: IaC and Containers (Detailed Theory)

---

### **Part 1: Infrastructure as Code (IaC) Security**

**1.1 What is Infrastructure as Code (IaC)?**

*   **Definition:** IaC is the practice of managing and provisioning infrastructure (servers, databases, networks) through machine-readable definition files (code), rather than through manual configuration.
*   **Analogy:** Instead of manually building a LEGO model from a picture, IaC is like having a precise, step-by-step instruction booklet that builds the exact same model every time.
*   **Key Tool:** Terraform.

**1.2 Why IaC is a Security Game-Changer:**

*   **Auditability:** The entire state of your infrastructure is in Git, providing a perfect audit trail of every change.
*   **Repeatability:** You can destroy and recreate infrastructure in minutes, eliminating "configuration drift."
*   **Automated Scanning:** We can use static analysis tools to scan infrastructure code for security misconfigurations *before* deployment.

**1.3 Securing Terraform with IaC Scanning:**

*   **The Problem:** A developer defines a new server and, for convenience, opens the SSH port (22) to the entire internet (`0.0.0.0/0`).
*   **The DevSecOps Solution:** An IaC scanner like **Checkov** is integrated into the CI/CD pipeline. It automatically scans the Terraform code and fails the build if it finds insecure configurations like an unrestricted ingress rule. The developer gets immediate feedback and is blocked from merging the insecure code.

---

### **Part 2: Container Security (Docker)**

Containers have revolutionized how we package applications, but they introduce new security considerations.

**2.1 Image Hardening: Building Secure Dockerfiles**

*   **Principle: Use Minimal Base Images**
    *   **Theory:** Don't build on a full OS like `ubuntu:latest`. It contains thousands of packages an attacker could abuse. Use minimal "distroless" or `scratch` images.
    *   **Secure Practice (Multi-stage Builds):** Use a "builder" stage with all the tools to compile your app. The final stage starts from a minimal base image and copies *only* the compiled application binary into it.

*   **Principle: Run as a Non-Root User**
    *   **Theory:** By default, containers run as `root`. If an attacker exploits your app, they are now `root` in the container, which is a major risk.
    *   **Secure Practice:** In your Dockerfile, create a dedicated, unprivileged user (`adduser`) and switch to that user (`USER appuser`) before running the application.

**2.2 Image Scanning**

*   **Theory:** A container image is a collection of layers, each of which can contain OS packages and libraries with known vulnerabilities (CVEs). An image scanner like **Trivy** analyzes every layer and compares its contents against public vulnerability databases.
*   **Use Case:** This is a mandatory CI/CD step. After `docker build`, the pipeline runs `trivy image my-app:latest`. If Trivy finds a critical vulnerability in a base layer, the pipeline fails, forcing the developer to update to a patched base image.

---

### **Part 3: Introduction to Container Orchestration Security (Kubernetes)**

Kubernetes (K8s) automates the deployment, scaling, and management of containerized applications at scale.

*   **Analogy:** If Docker provides the shipping container, Kubernetes is the entire automated port and fleet of ships.

Here are three core Kubernetes security concepts:

*   **1. RBAC (Role-Based Access Control)**
    *   **Theory:** RBAC is the mechanism for enforcing least privilege on the Kubernetes control plane. It controls who can do what to which resources.
    *   **Use Case:** Create a `Role` for your CI/CD pipeline that allows it to `create` and `update` Deployments, but explicitly denies it access to `secrets` or the ability to `delete` anything.

*   **2. Network Policies**
    *   **Theory:** By default, all pods (groups of containers) in a cluster can communicate freely. Network Policies act as an internal firewall, allowing you to define which pods can talk to each other.
    *   **Use Case:** Create a policy stating that `app=backend` pods can only accept incoming traffic from `app=frontend` pods. This prevents a compromised frontend from directly attacking a database pod.

*   **3. Pod Security Standards**
    *   **Theory:** These are preventative, cluster-level policies that can block pods with insecure configurations from ever being allowed to start.
    *   **Use Case:** Apply the `restricted` standard to a namespace to automatically enforce policies like "do not run as root" and "do not allow privilege escalation."
