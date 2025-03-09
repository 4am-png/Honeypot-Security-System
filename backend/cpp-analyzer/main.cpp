#include <iostream>
#include <fstream>
#include <string>

void logAttack(const std::string& ip) {
    std::ofstream logFile("logs/attacks.log", std::ios::app);
    if (logFile.is_open()) {
        logFile << "Suspicious activity detected from: " << ip << std::endl;
        logFile.close();
    } else {
        std::cerr << "Error opening log file!" << std::endl;
    }
}

int main() {
    std::string suspiciousIP = "192.168.1.100"; // Заглушка, замінити на реальний аналіз
    std::cout << "Monitoring network traffic..." << std::endl;

    // Симуляція виявлення підозрілого трафіку
    logAttack(suspiciousIP);

    std::cout << "Suspicious activity logged." << std::endl;
    return 0;
}
