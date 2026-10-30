# Database Structure

## Tables

### `users`

```sql
CREATE TABLE users (
	id INT AUTO_INCREMENT,
	username VARCHAR(255) NULL,
	email VARCHAR(320) NOT NULL,
	password VARCHAR(320) NOT NULL
);
```

### `rbac`

```sql
CREATE TABLE rbac (
    username VARCHAR(100) NOT NULL,
	role_name VARCHAR(100) NOT NULL,
	permissions VARCHAR(150) NOT NULL
);
```
