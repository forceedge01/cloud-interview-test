# PART 2 - Build and Push Image to ECR

## Guide time

~15 minutes

## Goal

Build a container image from the API code and push it to Amazon ECR.

## Environment for this part

You should develop/update the `dockerfile` locally.

You may test the image locally with `docker build`, but the ECR push step must be executed from **AWS CloudShell**.

## 1) Prerequisites

- All code is pushed to the Git repository under your own branch
- AWS CloudShell access is enabled
- Git access to clone the interview repository branch

## 2) Fix the dockerfile locally first

Before CloudShell build/push, update the `dockerfile` in your local branch so it is ready for a successful image build.

Commit and push your dockerfile changes.

## 3) Clone the same branch in CloudShell

```bash
rm -rf cloud-interview-test
git clone -b <branch-name> https://github.com/forceedge01/cloud-interview-test.git
cd cloud-interview-test
```

## 4) Build and push to ECR

Environment setup:

```bash
export AWS_ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
export ECR_REPO="test-interviewee/<your-first-name>"
export IMAGE_TAG="v1"
export ECR_REPO_URL"$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO"

# login to ECR
make ecr-login
```

Build the project image using containerisation and push to the following ECR repository:

test-interviewee/<your-first-name>

Note: The repository should already exist on ECR.

## Next Step

Continue to [PART3.md](PART3.md).
