CREATE TABLE IF NOT EXISTS attacks (
    id SERIAL PRIMARY KEY,
    attack_type VARCHAR(255),
    source_ip VARCHAR(50),
    timestamp TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);
