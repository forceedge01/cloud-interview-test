```python
@app.route("/admin/users") 
def get_admin_users():
    if request.headers.get("X-Admin") == "true": 
        return get_all_users() 

    return "Access denied", 403
```
