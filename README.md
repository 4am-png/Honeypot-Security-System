# Honeypot Security System

A simple Honeypot designed to detect malicious activity by mimicking vulnerable services and logging attack data for analysis.

## 🚀 Features
- **Fake services**: Simulates vulnerable services to attract malicious traffic.
- **Logging attacks**: Captures IP addresses, user agents, and requested paths.
- **Real-time monitoring**: Monitors traffic and displays metrics using Prometheus and Grafana.
- **Containerized setup**: Easily deploys using Docker and Kubernetes.

## ⚙️ Technologies Used
- **Backend**: Python (Flask)
- **Database**: PostgreSQL
- **Web Server**: Nginx
- **Monitoring**: Prometheus, Grafana
- **Containers**: Docker, Docker Compose, Kubernetes
- **Infrastructure as Code**: Terraform (for future scalability)

## 🛠️ Getting Started

To get started with the Honeypot Security System, you will need Docker and Docker Compose installed.

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/honeypot-security.git
cd honeypot-security
```

### 2. Set up the environment
Install the Python dependencies using the provided `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 3. Start the services
Run the entire system using Docker Compose:
```bash
docker-compose up --build
```

This will start:
- The **Honeypot** service on port `5000`
- **PostgreSQL** as the database to store log data
- **Nginx** to proxy requests to the Honeypot
- **Prometheus** for monitoring (available at `http://localhost:9090`)
- **Grafana** for visualizing data (available at `http://localhost:3000`)

### 4. Configure Grafana
Once Grafana is running, open `http://localhost:3000` and log in with default credentials:
- Username: `admin`
- Password: `admin`

Import the Honeypot dashboard by uploading the `honeypot-dashboard.json` from the `monitoring/grafana/` folder.

### 5. View Logs
Logs of all attacks are stored in the PostgreSQL database. You can access them using any PostgreSQL client or by querying directly from the application.

## 🧩 Project Structure
```
honeypot/
│── docker-compose.yml        # Docker Compose setup
│── .gitignore                # Git ignore file
│── README.md                 # Project documentation
│── LICENSE                   # License for the project
│── app/                      
│   ├── main.py               # Main application (Flask server)
│   ├── database.py           # Database connection logic
│   ├── Dockerfile            # Dockerfile for the Flask application
│── nginx/
│   ├── default.conf          # Nginx configuration
│   ├── Dockerfile            # Dockerfile for Nginx service
│── db/
│   ├── init.sql              # SQL file to initialize PostgreSQL database
│── monitoring/
│   ├── prometheus.yml        # Prometheus configuration file
│   ├── grafana/
│       ├── dashboards.yml    # Grafana dashboard configuration
│       ├── honeypot-dashboard.json  # JSON dashboard for Grafana
│── requirements.txt          # Python dependencies
│── logs/                     # Directory to store log files
```

## 📊 Monitoring and Analytics
- **Prometheus** collects metrics such as request counts, response times, and error rates.
- **Grafana** is used for visualizing these metrics via pre-configured dashboards.

## 🛡️ License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## 📢 Contributions
Feel free to contribute to the project! Fork the repository, create a new branch, and submit a pull request.

---

### 🚧 To Do:
- Implement Terraform for deploying to cloud services.
- Add more fake vulnerable services to increase interaction with attackers.
- Improve logging and alerting based on certain behaviors (e.g., brute-force attacks).

---

## 💡 Ideas for Future Enhancements
- **Email alerts**: Send email notifications when an attack is detected.
- **Advanced analytics**: Integrate machine learning for detecting attack patterns.
- **More fake services**: Include SSH, FTP, and other vulnerable services for a broader range of attacks.