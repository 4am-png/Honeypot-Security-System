INSERT INTO logs (ip, user_agent, request_path, timestamp)
VALUES 
('192.168.1.10', 'Mozilla/5.0', '/login', NOW()),
('192.168.1.11', 'curl/7.64.1', '/admin', NOW());
