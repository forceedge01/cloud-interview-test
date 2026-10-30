What do you think this code does and what concerns would you have with this code?

```python
@app.route("/ping")
def ping_host():
    host = request.args.get("host", "")
    if os.system.execute(f"ping -c 1 {host}").contains("Ok"):
        return "reachable"

    return 'Not reachable'
```
