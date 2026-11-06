# PART 1 - Code Review, Fix, and Local Run

Next: [PART2.md](PART2.md)

## Guide time

~25 minutes

### Approach
- Spend a few minutes reviewing the codebase and call out the top 5 issues you see.
- Pick the most important issue and implement a fix for that single issue.
- Run the application locally and show evidence that it starts.
- If time runs out, explain your remaining approach clearly.

### Part 1 challenge focus

- Identify and explain the top 5 issues in the codebase (security, correctness, reliability, or maintainability).
- Fix only the top 1 issue.
- Run the API locally.

## 1) Clone and checkout branch

```bash
git clone -b <your-first-name> https://github.com/forceedge01/cloud-interview-test.git
code cloud-interview-test/code
make -C cloud-interview-test/code setup
```

## 2) Run API locally

After creating a Python virtual environment, run the API from the main file.

```bash
python main.py
```

## 3) Optional local endpoint check

```bash
curl -H "Authorization: Bearer ${API_TOKEN}" http://<local-address>:5000/users/1
```

Example expected response for /users endpoint.

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

## 4) Build image locally (optional)

```bash
docker build -t interview-api:local .
```

No ECR push is required in this part.

## 5) Commit and push

```bash
git checkout -b <your-first-name>
git status
git add .
git commit -m "Part 1: top issue fix and local run"
git push origin <your-first-name>
```

## Next Step

Next: [PART2.md](PART2.md)
