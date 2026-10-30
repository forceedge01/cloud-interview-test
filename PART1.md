# PART 1 - Code Locally and Test

Next: [PART2.md](PART2.md)

## Guide time

~25 minutes

## Goal

Run the Flask API locally, validate it works, and commit your code changes. We would like to see design improvements where possible but most of all a working API is priority. Add automated tests where possible.

### Approach
- Take a few minutes to ingest the code in main.py.
- Explain what you see and your concerns.
- Attempt to resolve the challenge and run the app.
- In the last 5 mintues if the challenge is not met, you can explain the remainder of your approach.

### Part 1 challenge focus

- Implement a secure `GET /users/<id>` endpoint.
- Enforce bearer token auth using `Authorization: Bearer ${TOKEN}`.
- Tie user lookup to RBAC data so the response includes permissions (`rbac.role` and `rbac.permissions`).

## 1) Clone and checkout branch

```bash
git clone -b <your-first-name> https://github.com/forceedge01/cloud-interview-test.git
code cloud-interview-test/code
make -C cloud-interview-test/code setup
```

The API code is in the 'code' folder. You'll find basic Flask API implementation along with ORM files in the orm folder. The db folder has the basic schema against which you're developing. The docker-compose file will allow you to spin up a local database to work with.

For remote deployment to the server environment, configure the application to use the **production RDS instance** (not local DB settings). The database username and password are stored in **AWS Secrets Manager** and must be fetched from there. The db name is 'interview_db' (same as local).

## 4) Run API locally

After creating a python virtual environment run the API by invoking the main file

```bash
python main.py
```

## 5) Test endpoint

```bash
curl -H "Authorization: Bearer ${API_TOKEN}" http://<local-address>:5000/users/1
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

## 6) Commit and push

```bash
git checkout -b <your-first-name>
git status # Check you're on your own branch
git add .
git commit -m "Part 1: local run and test"
git push origin <your-first-name>
```

## Next Step

Next: [PART2.md](PART2.md)
