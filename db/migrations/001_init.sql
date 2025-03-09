CREATE TABLE logs (
    id SERIAL PRIMARY KEY,
    ip VARCHAR(45),
    user_agent TEXT,
    request_path TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
