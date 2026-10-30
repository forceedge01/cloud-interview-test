# Database Structure

## Tables

### `users`

```sql
CREATE TABLE users (
	id INT AUTO_INCREMENT PRIMARY KEY,
	username VARCHAR(255) NOT NULL UNIQUE,
	email VARCHAR(320) NOT NULL UNIQUE,
	password VARCHAR(320) NOT NULL UNIQUE
);
```

### `rbac`

```sql
CREATE TABLE rbac (
	user_id INT NOT NULL,
	role_name VARCHAR(100) NOT NULL,
	role_description VARCHAR(255) NULL,
	permission_name VARCHAR(150) NOT NULL,
	permission_description VARCHAR(255) NULL,
	PRIMARY KEY (user_id, role_name, permission_name),
	FOREIGN KEY (user_id) REFERENCES users(id)
);
```
