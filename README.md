# Interview Exercise Instructions

## Purpose

This exercise is designed to assess your ability to navigate a range of technical challenges and deliver a working solution end-to-end.

## Time-boxed Assessment Areas

1. **Python, RDS, database relations, and querying** (15 minutes)
2. **Containerisation skills** (15 minutes)
3. **AWS cloud know-how** (15 minutes)

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

You must push your working solution to Git.

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
