# Day 6 (Module 6): Cloud Security & Policy as Code (GCP) (Detailed Theory)

---

### **Part 1: The Shared Responsibility Model in GCP**

This model defines which security tasks are handled by Google and which are handled by you.

*   **Analogy:** Renting an apartment. Google (the landlord) is responsible for the security *of the building* (physical data centers, global network, hardware). You (the tenant) are responsible for the security *in your apartment* (locking your door, managing keys, securing your data).

*   **Google's Responsibility (Security *of* the Cloud):** Physical security, hardware security, network infrastructure, and the virtualization layer.

*   **Your Responsibility (Security *in* the Cloud):**
    *   **Data:** Securing and encrypting your own data.
    *   **Identity & Access Management (IAM):** Configuring who has access to what. This is a critical responsibility.
    *   **Network Configuration:** Correctly configuring VPCs, firewall rules, and load balancers.
    *   **Application Security:** Securing your own code against vulnerabilities like the OWASP Top 10.
    *   **OS & Patching:** For IaaS services like Compute Engine VMs, you are responsible for patching the guest operating system.

---

### **Part 2: Cloud Security Posture Management (CSPM) with Google Security Command Center**

*   **The Problem:** Cloud environments are too vast and dynamic to audit manually. Misconfigurations are a leading cause of breaches.

*   **What is CSPM?** An automated security tool that continuously monitors a cloud environment for misconfigurations and compliance violations.

*   **Google Security Command Center (SCC):**
    *   **What it is:** Google's native, centralized CSPM platform that provides a single dashboard for security risks.
    *   **Use Case:** A developer accidentally makes a Cloud Storage bucket public. Within minutes, SCC's "Security Health Analytics" automatically detects this and generates a high-severity finding. The security team is immediately alerted and can remediate the issue before a data leak occurs.

---

### **Part 3: Serverless Security: Securing Google Cloud Functions**

*   **The Shift in Responsibility:** In a serverless model, Google manages the OS and runtime, but your responsibility for securing your code and its permissions becomes even more critical.

*   **Key Serverless Security Risks & Mitigations:**
    *   **Insecure Function Permissions (IAM):**
        *   **Problem:** Granting a Cloud Function overly broad permissions (e.g., the "Editor" role).
        *   **Risk:** If an attacker finds a flaw in the function's code, they can use its powerful permissions to damage other resources in the project.
        *   **Mitigation (Least Privilege):** Create a dedicated service account for each function with a custom role that grants only the single permission it needs on the specific resource it needs to access.

    *   **Injection Flaws & Vulnerable Dependencies:**
        *   **Problem:** A serverless function is still code and can have vulnerabilities in its own logic or in its third-party libraries.
        *   **Mitigation:** Run SAST and SCA scans on your function's code as part of your CI/CD pipeline before every deployment.

---

### **Part 4: Policy as Code (PaC) with Open Policy Agent (OPA)**

*   **The Problem:** CSPM tools are reactive (they *detect* problems). PaC is proactive (it *prevents* problems).

*   **What is Policy as Code (PaC)?** The practice of writing your security and compliance policies as code. A policy engine then automatically enforces these policies against your Infrastructure as Code.

*   **Analogy:** If IaC (Terraform) is the "instruction booklet" for building infrastructure, PaC (OPA) is the "quality inspector" who checks each step against a rulebook *before* it is executed.

*   **Open Policy Agent (OPA):**
    *   **What it is:** An open-source, general-purpose policy engine. Policies are written in a language called **Rego**.
    *   **Use Case:** A company policy requires all Compute Engine disks to be encrypted with a customer-managed key (CMEK).
        1.  **Write the Policy:** A security engineer writes an OPA policy in Rego to check for this condition.
        2.  **Enforce in CI/CD:** In the pipeline, after `terraform plan` is run, a tool like `conftest` uses the OPA policy to check the plan file.
        3.  **The Impact:** If a developer submits Terraform code for a disk without the required encryption key, the OPA check fails the pipeline, blocking the insecure infrastructure from ever being deployed.
