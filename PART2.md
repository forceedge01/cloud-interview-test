# PART 2 - Build and Push Image to ECR

## Guide time

~15 minutes

## Goal

Build a container image from the API code and push it to Amazon ECR.

## Environment for this part

This part is executed in **AWS CloudShell** (not your local terminal).

## 1) Prerequisites

- All code is pushed to the Git repository under your own branch
- AWS CloudShell access is enabled
- Git access to clone the interview repository branch

## 2) Sign in and switch role first

1. Sign in to AWS Console with the credentials provided:
	- https://eu-north-1.signin.aws.amazon.com/
2. In the AWS Console (top-right), select **Switch role**.
3. Enter:
	- **Account**: `<provided-account-number>`
	- **Role**: `interviewee-dev-role`
4. Open a **new CloudShell session** after switching role.

Verify role in CloudShell:

```bash
aws sts get-caller-identity
```

The returned ARN must show the switched role session.

## 3) Clone the same branch in CloudShell

```bash
git clone -b <branch-name> https://github.com/forceedge01/cloud-interview-test.git
cd cloud-interview-test
```

## 4) Build and push to ECR

Build the project image using containerisation and push to the following ECR repository:

test-interviewee/<your-first-name>

Note: The repository should already exist on ECR.
