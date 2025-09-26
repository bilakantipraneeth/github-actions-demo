# Day 8 & 9: Capstone Project Walkthrough - Building a Secure CI/CD Pipeline

This document details the step-by-step process of building a secure CI/CD pipeline for our vulnerable capstone application, applying the DevSecOps principles and tools learned throughout the course.

---

## Phase 1: Application Setup and Initial Repository Configuration (Day 8)

### Step 1: Create the Vulnerable Capstone Application

**Goal:** Set up a simple Python Flask application with intentional vulnerabilities to serve as our target for security improvements.

**Files Created:**
- `devsecops/capstone_app/app.py`: Main Flask application with SQL Injection and hardcoded secret.
- `devsecops/capstone_app/requirements.txt`: Dependencies, including a vulnerable Flask version.
- `devsecops/capstone_app/init_db.py`: Script to initialize the SQLite database.
- `devsecops/capstone_app/Dockerfile`: Basic, insecure Dockerfile.

**Commands Executed (by Gemini):**
```bash
# Creation of app.py
# Creation of requirements.txt
# Creation of init_db.py
# Creation of Dockerfile
```

### Step 2: Initialize Local Git Repository (Initial Attempt)

**Goal:** Prepare the `capstone_app` for version control.

**Command Executed (by Gemini):**
```bash
git init
# Directory: D:\gemini-projects\github-actions\github-actions-demo\devsecops\capstone_app
```
**Outcome:** A new, nested Git repository was initialized.

### Step 3: Integrate Capstone App into Main Repository

**Goal:** Avoid nested Git repositories and add the `capstone_app` as a folder to the main `github-actions-demo` repository.

**Commands Executed (by Gemini):**
```bash
# Remove the nested .git directory
rmdir /s /q .git
# Directory: D:\gemini-projects\github-actions\github-actions-demo\devsecops\capstone_app

# Check status in main repository
git status
# Directory: D:\gemini-projects\github-actions\github-actions-demo
# Outcome: devsecops/ directory shown as untracked.

# Stage the new devsecops/ directory
git add devsecops/
# Directory: D:\gemini-projects\github-actions\github-actions-demo

# Commit the initial application code and course notes
git commit -m "feat: Add Capstone project application and course notes"
# Directory: D:\gemini-projects\github-actions\github-actions-demo

# Push to GitHub
git push
# Directory: D:\gemini-projects\github-actions\github-actions-demo
```
**Outcome:** The capstone application code and all course notes were successfully pushed to the main GitHub repository.

---

## Phase 2: Building the CI/CD Pipeline - Initial Setup (Day 9)

### Step 4: Create GitHub Actions Workflow File

**Goal:** Set up the basic structure for our CI/CD pipeline using GitHub Actions.

**Files Created:**
- `.github/workflows/capstone_pipeline.yml`: Initial workflow definition.

**Commands Executed (by Gemini):**
```bash
# Create workflow directory (already existed)
mkdir .github\workflows
# Directory: D:\gemini-projects\github-actions\github-actions-demo

# Create the initial workflow file
# Content:
# name: Capstone Security Pipeline
# on:
#   push:
#     branches: [ main ]
#   pull_request:
#     branches: [ main ]
#   workflow_dispatch:
# jobs:
#   build-and-scan:s
#     runs-on: ubuntu-latest
#     steps:
#       - name: Checkout repository
#         uses: actions/checkout@v4
#       - name: Set up Python 3.8
#         uses: actions/setup-python@v4
#         with:
#           python-version: '3.8'
#       - name: Install dependencies
#         working-directory: ./devsecops/capstone_app
#         run: |
#           python -m pip install --upgrade pip
#           pip install -r requirements.txt
```

### Step 5: Commit and Push Initial Pipeline

**Goal:** Get the basic CI/CD pipeline into GitHub to verify its functionality.

**Commands Executed (by Gemini):**
```bash
# Stage the new workflow file
git add .github/workflows/capstone_pipeline.yml
# Directory: D:\gemini-projects\github-actions\github-actions-demo

# Commit the initial pipeline
git commit -m "ci: Add initial CI pipeline for capstone project"
# Directory: D:\gemini-projects\github-actions\github-actions-demo

# Push to GitHub
git push
# Directory: D:\gemini-projects\github-actions\github-actions-demo
```
**Outcome:** The basic pipeline was pushed and ran successfully on GitHub.

---

## Phase 3: Integrating Security Gates - SCA Scan

### Step 6: Add SCA Scan with Trivy

**Goal:** Integrate a Software Composition Analysis (SCA) tool to find vulnerable third-party dependencies.

**File Modified:**
- `.github/workflows/capstone_pipeline.yml`

**Change:** Added a new step for Trivy SCA scan.

**Commands Executed (by Gemini):**
```bash
# Modify the workflow file to add the Trivy step
# (Details of replace operation)

# Stage the modified workflow file
git add .github/workflows/capstone_pipeline.yml
# Directory: D:\gemini-projects\github-actions\github-actions-demo

# Commit the SCA scan integration
git commit -m "ci: Add SCA scan with Trivy"
# Directory: D:\gemini-projects\github-actions\github-actions-demo

# Push to GitHub
git push
# Directory: D:\gemini-projects\github-actions\github-actions-demo
```
**Expected Outcome:** Pipeline runs on GitHub and **fails** at the "SCA Scan with Trivy" step due to the vulnerable Flask version.

### Step 7: Fix SCA Vulnerability

**Goal:** Update the vulnerable Flask dependency to a secure version.

**File Modified:**
- `devsecops/capstone_app/requirements.txt`

**Change:** Updated `Flask==1.1.2` to `Flask==2.3.3`.

**Commands Executed (by Gemini):**
```bash
# Modify requirements.txt
# (Details of replace operation)

# Stage the modified requirements.txt
git add devsecops/capstone_app/requirements.txt
# Directory: D:\gemini-projects\github-actions\github-actions-demo

# Commit the fix
git commit -m "fix: Update Flask to a secure version"
# Directory: D:\gemini-projects\github-actions\github-actions-demo

# Push to GitHub
git push
# Directory: D:\gemini-projects/github-actions/github-actions-demo
```
**Expected Outcome:** Pipeline runs on GitHub and **passes** the "SCA Scan with Trivy" step.

---

## Phase 4: Integrating Security Gates - SAST Scan

### Step 8: Set up SonarCloud for SAST Scan (Theoretical)

**Goal:** Configure SonarCloud to analyze our application's source code for vulnerabilities and integrate its authentication token into GitHub Secrets.

**User Actions Required (Theoretical):**
1.  Log in to [https://sonarcloud.io/](https://sonarcloud.io/) with GitHub.
2.  Create a new SonarCloud organization (if needed).
3.  Create a new SonarCloud project for the `github-actions-demo` repository. Make a note of the **Organization Key** and **Project Key**.
4.  Generate a new analysis token from "My Account" -> "Security" in SonarCloud. Copy this token immediately.
5.  Add this token as a GitHub Repository Secret named `SONAR_TOKEN` in your `github-actions-demo` repository settings (`Settings -> Secrets and variables -> Actions`).

**Outcome:** A SonarCloud project is ready for analysis, and the `SONAR_TOKEN` is securely stored in GitHub Secrets, allowing our pipeline to authenticate to SonarCloud.

### Step 9 (Theoretical): Integrating SAST with SonarCloud

**Goal:** Integrate Static Application Security Testing (SAST) into our CI/CD pipeline to automatically analyze our application's source code for vulnerabilities like SQL Injection and hardcoded secrets.

**9.1 Introduction to SAST in the Pipeline:**

*   **Recap:** SAST (Static Application Security Testing) analyzes source code without executing it. It's like a spell-checker for security bugs, finding vulnerable patterns and anti-patterns.
*   **Shift-Left Value:** Integrating SAST into the pipeline means we catch these code-level vulnerabilities as early as possible—ideally, before the code is even merged into the main branch. This is significantly cheaper and faster than finding them later.
*   **Our Tool:** We will use **SonarCloud**, a cloud-based SAST solution that integrates seamlessly with GitHub Actions.

**9.2 Theoretical `capstone_pipeline.yml` Modification:**

To integrate SonarCloud, we would add a new step to our `capstone_pipeline.yml` file, right after the `Install dependencies` step.

```yaml
      - name: Install dependencies
        working-directory: ./devsecops/capstone_app
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: SAST Scan with SonarCloud
        uses: SonarSource/sonarcloud-github-action@v2
        with:
          organization: ${{ secrets.SONAR_ORGANIZATION_KEY }} # Your SonarCloud organization key
          projectKey: ${{ secrets.SONAR_PROJECT_KEY }}       # Your SonarCloud project key
          token: ${{ secrets.SONAR_TOKEN }}                  # The GitHub Secret for SonarCloud token
          args: >
            -Dsonar.sources=devsecops/capstone_app/app.py
            -Dsonar.python.version=3.8
            -Dsonar.projectBaseDir=devsecops/capstone_app
```

**Explanation of the new step:**

*   `name: SAST Scan with SonarCloud`: A descriptive name for the step.
*   `uses: SonarSource/sonarcloud-github-action@v2`: This specifies the pre-built GitHub Action that will run the SonarCloud scanner.
*   `with:`: This section passes parameters to the SonarCloud action:
    *   `organization`: This would be your unique SonarCloud organization key (e.g., `my-github-username`).
    *   `projectKey`: This would be the unique key for your project in SonarCloud (e.g., `my-github-username_github-actions-demo`).
    *   `token: ${{ secrets.SONAR_TOKEN }}`: This is how the action authenticates to SonarCloud. It securely retrieves the `SONAR_TOKEN` from your GitHub repository secrets. This token grants the pipeline permission to upload analysis results to your SonarCloud project.
    *   `args`: These are additional arguments passed directly to the SonarCloud scanner.
        *   `-Dsonar.sources=devsecops/capstone_app/app.py`: Tells SonarCloud which files to analyze.
        *   `-Dsonar.projectBaseDir=devsecops/capstone_app`: Tells SonarCloud the base directory of our project.

**9.3 Theoretical Authentication (The `SONAR_TOKEN`):**

*   As discussed in Day 5 (Advanced Secrets Management), secrets should never be hardcoded.
*   The `SONAR_TOKEN` is a personal access token generated in SonarCloud. It acts as a password for your GitHub Actions workflow to communicate with SonarCloud.
*   It is stored as a **GitHub Repository Secret**. This means it is encrypted by GitHub, never exposed in logs, and only injected into the workflow runner's environment at runtime. This adheres to the principle of secure secrets management.

**9.4 Expected Output (Theoretical Log Analysis):**

When this step runs in the pipeline, we would expect the following in the logs:

1.  **SonarCloud Scanner Output:** Messages indicating the scanner is initializing, analyzing files, and uploading results.
2.  **Vulnerability Findings:** Crucially, SonarCloud would report the vulnerabilities it finds. For our `app.py` file, we would expect to see:
    *   **SQL Injection:** A "Critical" or "High" severity issue reported on the line:
        ```python
        users = conn.execute("SELECT * FROM users WHERE id = '" + user_id + "'").fetchall()
        ```
        SonarCloud would provide a detailed description of the vulnerability, its severity, and often suggest remediation steps.
    *   **Hardcoded Secret:** A "Code Smell" or "Security Hotspot" for the line:
        ```python
        app.config['SECRET_KEY'] = 'super-secret-key-that-should-not-be-in-code'
        ```
        SonarCloud would flag this as a potential secret leak.
3.  **Analysis Status:** The logs would indicate whether the analysis was successful and if any "Quality Gate" conditions were met or failed.

**9.5 Expected Outcome (Theoretical Pipeline Behavior):**

*   **Pipeline Failure:** Based on SonarCloud's default Quality Gate (which often fails the build for new critical/high severity issues), the pipeline would **fail** at the "SAST Scan with SonarCloud" step.
*   **Why it's a Success:** This failure is a security gate working exactly as intended. It means:
    *   The pipeline successfully analyzed our code.
    *   It correctly identified critical vulnerabilities (SQL Injection, hardcoded secret).
    *   It prevented this insecure code from being merged or deployed further.
    *   It provided immediate, actionable feedback to the developer, telling them exactly what needs to be fixed.

**9.6 Theoretical Mitigation Strategy:**

*   **SQL Injection Fix:** We would modify the `get_users` function in `app.py` to use a parameterized query, separating data from code:
    ```python
    @app.route('/users', methods=['GET'])
    def get_users():
        user_id = request.args.get('id')
        conn = get_db_connection()
        if user_id:
            # SECURE: Using a parameterized query
            users = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchall()
        else:
            users = conn.execute('SELECT * FROM users').fetchall()
        conn.close()
        return jsonify([dict(ix) for ix in users])
    ```
*   **Hardcoded Secret Fix:** We would move the `SECRET_KEY` out of the code. In a real application, this would come from an environment variable or a secrets manager like HashiCorp Vault (as discussed in Day 5). For our pipeline, we would likely use a GitHub Secret.
    ```python
    import os
    # ...
    app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'default-insecure-key-for-dev')
    ```
    And then we would add `FLASK_SECRET_KEY` as a GitHub Secret.

---

### **Step 10 (Theoretical): Pre-Commit Hooks for Secret Scanning**

**Goal:** Understand how to prevent sensitive information (secrets) from ever being committed into a Git repository using local pre-commit hooks.

**10.1 Introduction to Pre-Commit Hooks:**

*   **Recap:** Pre-commit hooks are scripts that run on a developer's local machine *before* a `git commit` operation is allowed to complete. They are the "far left" of the "shift left" security strategy, providing instant feedback.
*   **Purpose:** To enforce code quality, formatting, and, crucially, security policies (like secret detection) at the earliest possible stage.

**10.2 The Problem: Hardcoded Secrets**

*   **Our Vulnerability:** In our `devsecops/capstone_app/app.py` file, we have the line:
    ```python
    app.config['SECRET_KEY'] = 'super-secret-key-that-should-not-be-in-code'
    ```
    This is a hardcoded secret. If this code were pushed to a public repository, or even a private one with many contributors, it would be a severe security risk.

**10.3 The Tool: `gitleaks`**

*   **What it is:** `gitleaks` is a popular, open-source command-line tool specifically designed to scan Git repositories for hardcoded secrets. It uses a large, regularly updated set of regular expressions and heuristics to identify patterns that look like API keys, tokens, passwords, etc.

**10.4 Theoretical Local Integration Steps:**

A developer would typically integrate `gitleaks` using a pre-commit framework (like the `pre-commit` Python package).

1.  **Install `pre-commit`:** `pip install pre-commit`
2.  **Configure `gitleaks`:** Create a file named `.pre-commit-config.yaml` in the root of their repository (our `github-actions-demo` directory) with content like this:
    ```yaml
    # .pre-commit-config.yaml
    repos:
      - repo: https://github.com/gitleaks/gitleaks
        rev: v8.18.0 # Use the latest stable version
        hooks:
          - id: gitleaks
    ```
3.  **Install the hook:** `pre-commit install`

**10.5 Expected Output (Theoretical Local Log Analysis):**

If a developer tries to commit `app.py` with the hardcoded secret after setting up `gitleaks` as a pre-commit hook:

1.  They would run `git add devsecops/capstone_app/app.py`
2.  Then `git commit -m "feat: add new feature"`
3.  The `gitleaks` hook would automatically run. In the terminal, they would see output similar to this:
    ```
    gitleaks................................................................Failed
    - hook id: gitleaks
    - exit code: 1

    [+] Detected secret: 'super-secret-key-that-should-not-be-in-code'
        File: devsecops/capstone_app/app.py
        Line: 7
        Rule: Generic-API-Key
        Commit: (staged)
    Error: leaks found
    ```

**10.6 Expected Outcome (Theoretical Local Behavior):**

*   The `git commit` command would **fail**.
*   The developer would be **prevented** from completing the commit. The code with the hardcoded secret would not be saved to the local Git history, let alone pushed to GitHub.
*   **Why it's a Success:** This is the ultimate "shift-left" success. The secret is caught and blocked *before* it ever enters version control, preventing a major security incident and avoiding the complex cleanup required to remove secrets from Git history.

**10.7 Theoretical Mitigation Strategy:**

To fix the hardcoded secret, the developer would:

1.  **Remove the secret from the code:** Replace `app.config['SECRET_KEY'] = '...'` with a reference to an environment variable.
    ```python
    import os
    # ...
    app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', 'default-insecure-key-for-dev')
    ```
2.  **Provide the secret securely:** The actual secret value (`super-secret-key-that-should-not-be-in-code`) would then be provided to the application at runtime via an environment variable (e.g., `FLASK_SECRET_KEY`) or fetched from a secrets manager like HashiCorp Vault (as discussed in Day 5).

**10.8 Pipeline Integration (Theoretical Backup):**

While pre-commit hooks are powerful, they can be bypassed (`git commit --no-verify`). Therefore, it is crucial to also run `gitleaks` (or a similar secret scanner) as a step in the CI/CD pipeline. This acts as a server-side backup, ensuring no secrets make it into the main repository, even if local hooks are bypassed.

---

### **Step 11 (Theoretical & Practical): Docker Image Scanning with Trivy**

**Goal:** Understand how to automatically scan our Docker container images for known vulnerabilities in their operating system layers and application dependencies, and then implement this in our CI/CD pipeline.

**11.1 Introduction to Docker Image Scanning:**

*   **Recap:** From Day 4, we know that Docker images are built in layers, often built from base images and including many packages and libraries. These can contain known vulnerabilities (CVEs).
*   **Purpose:** Image scanning is crucial because even if your application code is perfect, a vulnerability in a base OS package (like `openssl` or `glibc`) can expose your entire application to attack.

**11.2 The Problem: Vulnerabilities in Image Layers**

*   Our current `Dockerfile` starts with `FROM python:3.8-slim`. While `slim` is better than a full OS, it still contains a Debian-based operating system with many packages. These packages are likely to have many known vulnerabilities.

**11.3 The Tool: `Trivy` (Image Scanner)**

*   **What it is:** Trivy is an open-source, comprehensive, and easy-to-use vulnerability scanner for container images, filesystems, and Git repositories. We already used it for SCA (filesystem scan). Now we'll use it for image scanning.
*   **How it works (Theory):**
    1.  **Layer Analysis:** Trivy analyzes each layer of a Docker image.
    2.  **Component Identification:** It identifies all operating system packages (e.g., `apt` packages for Debian/Ubuntu, `rpm` for CentOS) and application dependencies (e.g., Python `pip` packages, Node.js `npm` packages).
    3.  **Vulnerability Database Lookup:** It compares these components against various vulnerability databases (e.g., NVD, vendor-specific advisories, language-specific advisories).
    4.  **Report Generation:** It generates a detailed report of all found vulnerabilities, including CVE IDs, severities (Critical, High, Medium, Low), and often provides recommended fixed versions.

**11.4 Practical `capstone_pipeline.yml` Modification:**

We have already modified the `capstone_pipeline.yml` file to include the Docker image build and scan steps. The file now looks like this:

```yaml
name: Capstone Security Pipeline

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
  workflow_dispatch: # Allows manual triggering

jobs:
  build-and-scan:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python 3.8
        uses: actions/setup-python@v4
        with:
          python-version: '3.8'

      - name: Install dependencies
        working-directory: ./devsecops/capstone_app
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Build Docker Image
        working-directory: ./devsecops/capstone_app
        run: |
          docker build -t capstone-app:latest .

      - name: Docker Image Scan with Trivy
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'image'
          image-ref: 'capstone-app:latest'
          format: 'table'
          exit-code: '1'
          severity: 'CRITICAL,HIGH'

      - name: SCA Scan with Trivy
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: './devsecops/capstone_app'
          ignore-unfixed: 'true'
          format: 'table'
          exit-code: '1'
          severity: 'CRITICAL,HIGH'
```

**Explanation of the new steps:**

*   `name: Build Docker Image`: This step uses the `docker build` command to create our container image. We tag it as `capstone-app:latest`.
*   `name: Docker Image Scan with Trivy`: This step uses the same `aquasecurity/trivy-action` but with different parameters:
    *   `scan-type: 'image'`: Tells Trivy to scan a Docker image.
    *   `image-ref: 'capstone-app:latest'`: Specifies the image we just built.
    *   `exit-code: '1'` and `severity: 'CRITICAL,HIGH'`: Configures Trivy to fail the pipeline if it finds any Critical or High severity vulnerabilities in the image.

**11.5 Expected Output (Theoretical Log Analysis):**

When this step runs, Trivy will analyze the `capstone-app:latest` image. We would expect to see a lengthy report in the logs, listing numerous vulnerabilities.

*   **OS Package Vulnerabilities:** Since `python:3.8-slim` is based on Debian, Trivy will likely find many vulnerabilities in core Debian packages (e.g., `libssl`, `glibc`, `apt`).
*   **Application Dependency Vulnerabilities:** Trivy will also scan the Python dependencies (though we fixed Flask, other transitive dependencies might have issues).

**11.6 Expected Outcome (Theoretical Pipeline Behavior):**

*   The pipeline would **fail** at the "Docker Image Scan with Trivy" step.
*   **Why it's a Success:** This failure is a crucial security gate. It prevents us from deploying a container image that contains known vulnerabilities in its underlying operating system or other components. It provides immediate feedback that our image is not secure enough for deployment.

**11.7 Theoretical Mitigation Strategy:**

To fix the vulnerabilities found by the image scan, we would:

1.  **Use a More Secure Base Image:** Update our `Dockerfile` to use a more minimal and secure base image. For Python, this often means using a multi-stage build with a "distroless" image for the final stage, or a hardened `slim-buster` image.
2.  **Keep Base Images Updated:** Regularly rebuild images to pull in the latest security patches from the base image.
3.  **Minimize Installed Packages:** Only install packages absolutely necessary for the application to run.

---
