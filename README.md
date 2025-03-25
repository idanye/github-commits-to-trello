# 🚀 GitHub to Trello Commit Sync

A Python script that fetches the most recent commits from a GitHub repository and automatically creates Trello cards for each commit. 
It archives all existing cards in the target Trello list before syncing.

---

## 📦 Features

- ✅ Fetches the 5 most recent commits from a specified GitHub repo  
- ✅ Creates Trello cards for each commit in a specified Trello list  
- ✅ Archives all existing cards in the list before syncing  
- 🔐 Uses `.env` for secure configuration of API keys and settings

---

## 🛠️ Technologies Used

- Python 3.9+
- `requests`
- `python-dotenv`
- GitHub REST API
- Trello REST API

---

## 📂 File Structure

github-to-trello-commit-sync/
├── github_api.py         # GitHub API: fetch and parse commits
├── trello_api.py         # Trello API: create and archive cards
├── main.py               # Entry point that connects GitHub to Trello
├── .env                  # Environment variables (not committed)
├── .gitignore            # Ignores .env, venv, and __pycache__
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

