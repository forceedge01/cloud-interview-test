# PART 1 - Code Locally and Test

## Guide time

~25 minutes

## Goal

Run the API locally, validate it works, and commit your code changes.

## 1) Clone and checkout branch

```bash
git clone -b <your-first-name> https://github.com/forceedge01/cloud-interview-test.git
cd cloud-interview-test/code
```

The code is in the 'code' folder. You'll find basic ORM files in the orm folder. The db folder has the basic schema against which you're developing. The docker-compose file will allow you to spin up a local database to work with.

## 4) Run API locally

```bash
python main.py
```

## 5) Test endpoint

```bash
curl -H "Authorization: Bearer ${API_TOKEN}" http://localhost:5000/users/1
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
git add .
git commit -m "Part 1: local run and test"
git push origin <your-first-name>
```