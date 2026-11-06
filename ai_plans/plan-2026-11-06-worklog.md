# Plan - 2026-11-06 Worklog

## Feature: Restructure interview exercise to 2 parts and tighten ECS public IP controls

### Tracker
- [completed] Update Part 1 to focus on top 5 issues, fix top 1, and run the app.
- [completed] Replace current Part 2 content with deployment-from-ECR exercise and remove Part 3 navigation.
- [completed] Update README flow and timings so both parts fit into 1 hour total.
- [completed] Add IAM deny guard in Terraform so `interviewee-dev-role` cannot deploy ECS workloads with public IP enabled.
- [completed] Add pre-created ALB, target group, and HTTP listener in Terraform baseline for the interview environment.
- [completed] Add interview OWASP challenge issues in `code/main.py` (beyond existing broken access control).
- [not-started] Replace MySQL container image with a MariaDB image selection.
- [not-started] Run Terraform formatting validation for the policy update.

### Tests (to run)
- `terraform -chdir=oso-engineer-interivew-setup-admin/iac/interviewee-exercise fmt -check`
- `python interview-exercise/code/main.py`
