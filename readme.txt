# Community Resource Navigator Agent

## Project Overview

The Community Resource Navigator Agent is an AI-based multi-agent system designed to assist underserved and disaster-affected communities in quickly finding and accessing critical local resources such as hospitals, shelters, and aid centers. This project demonstrates the use of agent AI concepts like session management, persistent memory, and modular design to create an intelligent assistant focused on social good.

Due to Google Maps and Places API billing constraints, this prototype uses a dummy SQLite database to simulate resource discovery and session persistence, making it ideal for competition environments without billing capabilities.

---

## Features

- Multi-agent inspired architecture with modular components for resource finding and session memory.
- Persistent session and interaction memory using SQLite.
- Dummy data simulates nearby resource searches without actual Google API calls.
- Easily extensible to real API integration when billing is enabled.
- Designed to run in Kaggle or Google Colab environments.
- Well-documented code and structured for development and competition use.

---

## Repository Structure

| Path                     | Description                                             |
|--------------------------|---------------------------------------------------------|
| `src/`                   | Source code modules for core functionality               |
| `src/agent_memory.py`    | Session and memory management using SQLite               |
| `src/resource_finder.py` | Resource lookup using dummy database                      |
| `src/main_agent.py`      | Main agent logic handling user requests and responses    |
| `notebooks/demo.ipynb`   | Interactive notebook demo with inline documentation       |
| `requirements.txt`       | Required Python packages for environment setup            |
| `README.md`              | Project overview, setup instructions, and documentation  |
| `LICENSE`                | Open source license (MIT recommended)                    |

---

## Setup Instructions

1. **Clone the repository**
