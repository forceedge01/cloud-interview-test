# PART 3 - Deploy Using Image from ECR

## Guide time

~30 minutes

## Goal

Deploy the service by pulling the image from ECR and exposing it through a protected AWS entry point. You may use IaC or the AWS UI console to perform these tasks.

## Candidate implementation freedom

This is a senior-level assessment. You may use AWS Web Console or AWS CloudFormation (AWS CloudShell).

No fixed path is required as long as all required outcomes below are satisfied.

## Pre-requisites

Refer to the main pre-requisites in [README.md](README.md#pre-requisites).


## Required outcomes

1. Deploy the API using the image produced in Part 2 (from ECR).
2. Ensure the API container/service is not directly exposed to the public internet.
3. Expose the API through a managed secure entry point (for example: ALB or API Gateway).
4. Serve the API through the domain candidate-test.co.uk (this domain registered and setup for you in [route53](https://console.aws.amazon.com/route53/v2/hostedzones?region=eu-west-2#ListRecordSets/Z09387322ANGIEFFO5CCP)).
4.1. Verify by `curl "https://dns.google/resolve?name=candidate-test.co.uk&type=NS" | jq -r '.Answer[] | .data'` which should list all awsdns entries.
5. Enable HTTPS/TLS with a valid certificate (for example ACM-managed certificate).
6. Apply protections against common web attacks.
7. Manage sensitive values securely.
8. Use production RDS credentials from AWS Secrets Manager (do not hardcode DB credentials in code, task definitions, or repository files).

## Validation

Example request:

```bash
curl -X GET "https://candidate-test.co.uk/users/1"
```

Expected output example:

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

## Evidence to provide

- Architecture summary (1-2 paragraphs)
- Key security controls implemented
- Endpoint URL used for validation
- Brief trade-off notes

## Next Step

This is the end of the technical exercise. Thanks for your time, please let the team know to proceed.
