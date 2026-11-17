# projects_from_python_studies

This repository is primarily a collection of Python study projects. It is used to practice Python concepts such as variables, functions, classes, loops, user input, and object-oriented programming through terminal mini-games.

It also includes a full-stack journal application, with a Python FastAPI backend and a React/TypeScript frontend. These projects demonstrate how Python can be used both for standalone programs and for building web APIs.

## Repository structure

```text
minigames/          Terminal-based Python exercises
journal_app/
  backend/          Python virtual environment, dependencies, FastAPI API, and SQLAlchemy models
  database/         SQLite database storage
  frontend/         React and TypeScript client
```

## Mini-games

The `minigames/` folder contains three terminal-based Python programs:

- **Blackjack:** play against the dealer and try to reach 21 without going over.
- **Cup shuffle:** guess where the hidden ball is after three cups are shuffled.
- **Tic-Tac-Toe:** play a two-player game on a 3x3 board.

### How to play

- **Blackjack:** start by entering a chip bet, then choose `h` to hit or `s` to stand. The dealer plays until reaching 17.
- **Cup shuffle:** enter `0`, `1`, or `2` to guess which position contains the ball.
- **Tic-Tac-Toe:** choose `X` or `O`, then take turns entering a position from `1` to `9`.

### How to run the mini-games

The mini-games use Python 3 and require no third-party packages. From the repository root, run:

```bash
python3 minigames/blackjack.py
python3 minigames/cup_shuffle.py
python3 minigames/tictactoe.py
```


## Journal app

The journal app is a full-stack application for creating and viewing journal entries:

- **FastAPI backend:** provides the API for reading and creating journal entries.
- **SQLAlchemy:** manages database models and communication with SQLite.
- **SQLite database:** stores journal entries locally.
- **React and TypeScript frontend:** provides the interface for writing and viewing entries.
- **Vite:** serves the frontend and proxies `/api` requests to the backend during local development.

The frontend communicates with the backend through `/api/entries`.

### How to run the Journal app

### Pre-requisites

- Python 3
- Node.js and npm

Install the backend dependencies and run the FastAPI server from the repository root:

```bash
cd journal_app
python3 -m venv backend/venv
source backend/venv/bin/activate
python3 -m pip install -r backend/requirements.txt
python -m uvicorn backend.app:app --reload
```

In another terminal, start the React frontend:

```bash
cd journal_app/frontend
npm install
npm run dev
```