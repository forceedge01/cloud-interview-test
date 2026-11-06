# PART 2 - Deploy Image from ECR

Previous: [PART1.md](PART1.md)

## Guide time

~35 minutes

## Goal

Deploy the API using an image stored in ECR to any suitable AWS service.

## Candidate implementation freedom

You may choose your deployment path (for example ECS, App Runner, or another AWS service), as long as the required outcomes are met.

## Required outcomes (Definition of done)

1. Deploy the API using an image from ECR.
2. Expose the API through a managed secure entry point (for example ALB or API Gateway).
3. Manage sensitive values through AWS Secrets Manager.

An example deployment design:

ALB -> ECS -> App

## Bonus outcomes

5. Use production RDS credentials from AWS Secrets Manager (no hardcoded DB credentials).
6. Enable HTTPS/TLS with a valid certificate.
7. Serve traffic via candidate-test.co.uk.
8. Add web protections such as AWS WAF.

## Validation

Example request:

```bash
curl -X GET "https://<your-api-endpoint>/users/1" \
	-H "Authorization: Bearer ${API_TOKEN}"
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

## End

This is the end of the technical exercise.
