# Interview Exercise Instructions

## Purpose

This exercise is designed to assess your ability to navigate a range of technical challenges and deliver a working solution end-to-end.

## Pre-requisites

Before starting ensure you have:

- Python 3.13+ installed on terminal.
- Docker installed on terminal.
- Credentials for Github and AWS Console.
- Git is installed locally.
- A code editor of your choice.

Before the timer starts, complete AWS access setup:

1. Sign in to AWS Console with the credentials provided:
	- https://eu-north-1.signin.aws.amazon.com/
2. In the AWS Console (top-right), select **Switch role**.
3. Enter:
	- **Account**: `<provided-account-number>`
	- **Role**: `interviewee-dev-role`
4. Open a **new CloudShell session** after switching role.
5. Verify role in CloudShell:

```bash
aws sts get-caller-identity
```

The returned ARN must show the switched role session.

We will start the exercise clock once these are confirmed.

## Time-boxed Assessment Areas and Delivery Flow

Follow the exercise in this order:

1. **Part 1 - Code locally and test** (guide: ~25 minutes)
	- Focus: Python, database relations, querying
	- Instructions: [PART1.md](PART1.md)
2. **Part 2 - Build and push to ECR** (guide: ~15 minutes)
	- Focus: Containerisation skills
	- Instructions: [PART2.md](PART2.md)
3. **Part 3 - Deploy using image from ECR** (guide: ~30 minutes)
	- Focus: AWS cloud know-how
	- Instructions: [PART3.md](PART3.md)

## Objective

Deploy the provided API to AWS in a working state, using the approach you think is best.

## Constraints

- The API server must **not** be directly accessible from the public internet.
- The deployment must include protection against common web attacks.

Examples of acceptable protections include (but are not limited to):

- Placing the API behind a managed entry point such as API Gateway or an Application Load Balancer.
- Restricting network access with security groups and private subnets.
- Enabling HTTPS/TLS.
- Using AWS WAF (or equivalent controls) to mitigate common attack patterns.

## Source Code

The code to deploy is in the **code** folder.

## Deployment Approach

You may choose any of the following:

- **Terraform**
- **CloudFormation**
- **Manual AWS commands/setup**

Any valid approach is acceptable as long as the API is successfully deployed and functional.

## AI Usage

Use of AI is permitted during this exercise.

## Git Requirement

You must push your working solution to Git. Credentials will be provided.

## Containerisation Exercise Environment

The containerisation portion will be conducted using **AWS CloudShell**.

We will guide you on how to log in to CloudShell before that part begins.

## What We Are Looking For

- Clear technical decision-making
- Practical problem-solving under time constraints
- Working deployment outcome
- Ability to explain trade-offs and implementation choices

## Post-Deployment API Usage Example

After deploying the API, verify it by calling the user endpoint.

Example request:

```bash
curl -X GET "https://<your-api-endpoint>/users/1"
```

Example JSON response:

```json
{
	"id": 1,
	"username": "alice",
	"email": "alice@example.com",
	"rbac": {
		"role": "admin",
		"permissions": [
			"users:read",
			"users:write",
			"reports:read"
		]
	}
}
```

## Next Step

Start with [PART1.md](PART1.md).
