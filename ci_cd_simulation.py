import os
import time
import random

def log_step(step_name, status="START"):
    """Logs the start or end of a CI/CD step, mimicking runner output."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {step_name} - {status}")

def setup_environment():
    """Simulates setting up the build environment, a common first step for any runner."""
    log_step("Environment Setup", "START")
    print("  - Checking Python version...")
    print(f"  - Python version: {os.sys.version.splitlines()[0]}")
    print("  - Installing dependencies (simulated)...")
    time.sleep(1) # Simulate work
    log_step("Environment Setup", "COMPLETE")
    return True

def build_project():
    """Simulates building a project, a core task for CI pipelines."""
    log_step("Project Build", "START")
    print("  - Compiling source code (simulated)...")
    time.sleep(2) # Simulate work
    # Simulate a build failure occasionally to show pipeline robustness
    if random.random() < 0.1: # 10% chance of failure
        log_step("Project Build", "FAILED")
        return False
    log_step("Project Build", "COMPLETE")
    return True

def run_tests():
    """Simulates running automated tests, crucial for Continuous Integration."""
    log_step("Running Tests", "START")
    num_tests = random.randint(5, 15)
    passed_tests = 0
    failed_tests = 0
    for i in range(num_tests):
        test_name = f"test_feature_{i+1}"
        if random.random() < 0.05: # 5% chance of a test failing
            print(f"  - [FAIL] {test_name}")
            failed_tests += 1
        else:
            print(f"  - [PASS] {test_name}")
            passed_tests += 1
        time.sleep(0.1) # Simulate test execution time

    if failed_tests > 0:
        print(f"  - {passed_tests} tests passed, {failed_tests} tests failed.")
        log_step("Running Tests", "FAILED")
        return False
    else:
        print(f"  - All {passed_tests} tests passed.")
        log_step("Running Tests", "COMPLETE")
        return True

def deploy_artifact():
    """Simulates deploying the built artifact, a key part of Continuous Delivery."""
    log_step("Deploy Artifact", "START")
    # Demonstrates how runners can pass environment variables to influence jobs
    env_target = os.getenv("DEPLOY_TARGET", "staging")
    print(f"  - Deploying to target: {env_target}")
    print("  - Uploading package (simulated)...")
    time.sleep(1.5) # Simulate work
    log_step("Deploy Artifact", "COMPLETE")
    return True

def main():
    print("--- CI/CD Pipeline Simulation ---")
    # This script simulates a simple CI/CD pipeline job.
    # It would be executed by any CI/CD runner (GitHub-hosted, self-hosted, or managed).
    # The choice of runner impacts where and how this script runs, but the script itself defines the job.

    if not setup_environment():
        print("Pipeline aborted: Environment setup failed.")
        return

    if not build_project():
        print("Pipeline aborted: Project build failed.")
        return

    if not run_tests():
        print("Pipeline aborted: Tests failed.")
        return

    # Deployment typically only proceeds if all previous steps pass successfully
    if not deploy_artifact():
        print("Pipeline aborted: Deployment failed.")
        return

    print("--- CI/CD Pipeline Completed Successfully ---")

if __name__ == "__main__":
    main()
