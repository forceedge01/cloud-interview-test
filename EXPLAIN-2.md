What concerns would you have with this code?

```python
@app.route("/user") 
def get_user():
    if request.headers.get("METHOD") != "GET": 
        return "Invalid request type", 401

    api_token = request.headers.get("Authorization")

    if api_token != os.environ['API_TOKEN']:
        return "Unauthorised", 403

    user_id = request.args.get('user_id')
    return get_user(user_id)
```
