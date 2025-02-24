# OTP-Based Admin Authentication & Fee Alert System

## 📌 Project Overview
The **OTP-Based Admin Authentication & Fee Alert System** is designed to enhance security and automate fee alerts for institutions. The system ensures secure admin access through OTP-based authentication and provides timely fee reminders to students via email.

## 🚀 Features
- **OTP-Based Authentication**: Ensures secure admin login by sending a One-Time Password (OTP) to registered email.
- **Fee Alert System**: Sends automatic fee reminders to students based on their payment status.
- **Admin Dashboard**: Manage students, view fee statuses, and send alerts.
- **Secure Email Handling**: Uses SMTP for sending emails securely.
- **User-Friendly Interface**: Simple and intuitive UI for easy navigation.

## 🛠️ Technologies Used
- **Programming Language**: Python
- **SMTP Service**: Gmail SMTP for email-based authentication and notifications
- **Database**: Dictionary-based storage (can be extended to MySQL/PostgreSQL)
- **OTP Generation**: Python `random` module

## 📂 Installation & Setup
### Prerequisites:
- Python 3.x installed
- SMTP email account (e.g., Gmail)

### Steps:
1. **Clone the Repository**
   ```sh
   git clone https://github.com/yourusername/otp-admin-auth-fee-alert.git
   cd otp-admin-auth-fee-alert
   ```
2. **Install Dependencies**
   ```sh
   pip install -r requirements.txt  # Ensure required libraries are installed
   ```
3. **Configure Email Credentials**
   - Store your email credentials securely in a `.env` file instead of hardcoding them in the script.
   
4. **Run the Application**
   ```sh
   python main.py
   ```

## 🔑 Usage
1. **Admin Login**: Enter registered email → Receive OTP → Enter OTP to authenticate.
2. **Manage Students**: Add/update student fee details.
3. **Send Fee Alerts**: System sends automatic reminders via email based on fee status.

## 📜 Security Best Practices
- **Environment Variables**: Store email credentials in an `.env` file instead of hardcoding them.
- **Hashing Sensitive Data**: Ensure OTPs and credentials are encrypted before storage.
- **Rate Limiting**: Prevent brute-force attacks by implementing login attempt limits.
- **Use Secure SMTP**: Utilize secure SMTP services with strong authentication mechanisms.

## 🤝 Contribution
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Submit a Pull Request.
