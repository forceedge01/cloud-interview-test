What concerns would you have with this code?

```python
@app.route("/ping")
def ping_host():
    host = request.args.get("host", "")
    result = os.system.execute(f"ping -c 1 {host}")

    if result == 'OK':
        return result

    return 'Not reachable'
```
