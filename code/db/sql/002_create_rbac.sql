CREATE TABLE IF NOT EXISTS rbac (
    user_id INTEGER NOT NULL REFERENCES users(id),
    role_name VARCHAR(100) NOT NULL,
    role_description VARCHAR(255),
    permission_name VARCHAR(150) NOT NULL,
    permission_description VARCHAR(255)
);
