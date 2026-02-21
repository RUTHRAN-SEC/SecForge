# Phishing Awareness Simulator
--- 

## Overview about the project

Phishing Awareness Simulator is a Python Flask-based security training tool designed to simulate phishing email clicks and measure user susceptibility.
The system records user interaction with simulated phishing links and generates a reporting dashboard for awareness analysis.
This project is intended for educational and security awareness purposes only.

---

## Problem Statement

Phishing is the number one initial access vector in modern cyber attacks.
Organizations require measurable data to understand employee susceptibility to phishing attacks and to improve security awareness programs.
This project demonstrates how simulated phishing campaigns can be tracked and analyzed in a controlled environment.

---

## Features Added

- Simulated phishing link tracking
- Email-based click identification
- Timestamp logging
- SQLite database integration
- Admin reporting dashboard
- Awareness notification landing page

---

## Technology Stack

- Python
- Flask
- SQLite
- HTML

---

## Project Structure

```
phishing-awareness-simulator/
│
├── app.py
├── README.md
│
└── templates/
|   ├── landing.html
|   └── report.html
|
└── Screen Shorts.md
```

---

## How It Works

1. A simulated phishing link is generated with a user email parameter.
2. When the link is clicked, the system:
    - Captures the email
    - Logs the timestamp
    - Stores the data in the SQLite database
3. The admin can access a report page to view all recorded interactions.

---

## Installation and Setup

Clone the repository:

```
gitclone https://github.com/RUTHRAN-SEC/phishing-awareness-simulator.gitcd phishing-awareness-simulator
```

Create virtual environment:

```
python -m venv venv
```

Activate virtual environment Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
python -m pip install flask
```

Run the application:

```
python app.py
```

---

## Usage

Simulate a phishing click:

```
http://127.0.0.1:5000/offer?user=test@example.com
```

View report dashboard:

```
http://127.0.0.1:5000/report
```

---

## Security Considerations

- This project is for controlled lab environments only.
- It should not be used for unauthorized phishing activities.
- Always obtain proper authorization before conducting phishing simulations.

---

## Business Value

This project demonstrates:

- Understanding of social engineering attack vectors
- Backend development and data logging
- Database design and tracking mechanisms
- Risk measurement implementation
- Security awareness simulation techniques

It reflects real-world security awareness programs used by organizations to measure phishing risk and improve defensive posture.

---

## Future Improvements

- IP address logging
- User-agent tracking
- Click rate percentage calculation
- CSV export functionality
- Admin authentication
- Email campaign automation

---

## ⚠️ Disclaimer

This project is intended strictly for educational and ethical purposes.
All testing must be performed only on systems you own or have explicit authorization to test.
The author is not responsible for any misuse or illegal activity resulting from the use of this project.

## Author

### RUTHRAN-SEC
