What do you think this code does and what concerns would you have with this code?

```python
@app.route("/invoices/<invoice_id>", methods=["GET"])
def get_invoice(invoice_id):
    invoice = db.get_invoice(invoice_id)  # returns owner_id, amount, card_last4, etc.

    if not invoice:
        return "Not found", 404

    user = current_user()
    if user.is_authenticated():
        return jsonify(invoice), 200

    return "Unauthorized", 401
```
