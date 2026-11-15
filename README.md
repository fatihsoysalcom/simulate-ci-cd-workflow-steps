# Simulate CI CD Workflow Steps

This Python script simulates a basic Continuous Integration/Continuous Delivery (CI/CD) pipeline job. It demonstrates typical steps like environment setup, project build, automated testing, and artifact deployment. The script's output mimics the logs produced by a CI/CD runner, illustrating the flow and potential failure points within a pipeline. This example helps visualize the tasks that different CI/CD runner types (GitHub-hosted, self-hosted, managed) would execute.

## Language

`python`

## How to Run

1. Save the code as `ci_cd_simulation.py`.
2. Open a terminal or command prompt.
3. Run the script using Python: `python ci_cd_simulation.py`
4. To simulate deployment to a different target, run: `DEPLOY_TARGET=production python ci_cd_simulation.py`

## Original Article

This example accompanies the Turkish article: [GitHub-hosted, Self-hosted ve Managed Runner'lar: CI/CD Süreçlerinizi Nasıl Optimize Edersiniz?](https://fatihsoysal.com/blog/github-hosted-self-hosted-ve-managed-runnerlar-ci-cd-sureclerinizi-nasil-optimize-edersiniz/).

## License

MIT — see [LICENSE](LICENSE).
