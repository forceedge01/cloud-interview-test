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

## 4) Set variables

```bash
export AWS_REGION="eu-west-2"
export AWS_ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
export ECR_REPO="cloud-interview-test-api"
export IMAGE_TAG="v1"
```

## 5) Create repository (if missing)

```bash
aws ecr describe-repositories --repository-names "$ECR_REPO" --region "$AWS_REGION" || \
aws ecr create-repository --repository-name "$ECR_REPO" --region "$AWS_REGION"
```

## 6) Login to ECR from CloudShell

```bash
aws ecr get-login-password --region "$AWS_REGION" | docker login --username AWS --password-stdin "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com"
```

## 7) Build and tag image

```bash
cd code
docker build -f dockerfile -t "$ECR_REPO:$IMAGE_TAG" .
docker tag "$ECR_REPO:$IMAGE_TAG" "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:$IMAGE_TAG"
```

## 8) Push image

```bash
docker push "$AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:$IMAGE_TAG"
```

## 9) Verify image in ECR

```bash
aws ecr describe-images --repository-name "$ECR_REPO" --region "$AWS_REGION"
```
