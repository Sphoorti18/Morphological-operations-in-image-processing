# Project Setup Guide

## Prerequisites

Make sure you have **Python** installed on your system before proceeding.

---

## 1. Create a Virtual Environment

Open your terminal in the project directory and run:

```bash
python -m venv venv
```

This creates a folder named `venv` containing an isolated Python environment.

---

## 2. Activate the Virtual Environment

**Windows:**
```bash
venv\Scripts\activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

Once activated, you should see `(venv)` appear at the beginning of your terminal prompt.

---

## 3. Install Required Packages

If you notice **squiggly lines** (import errors) in your editor, it means some packages are missing. Install them using `pip`:

```bash
pip install <package-name>
```

For example:
```bash
pip install requests numpy pandas
```

To install all dependencies at once (if a `requirements.txt` file is provided):
```bash
pip install -r requirements.txt
```

---

## 4. Run the Application

Launch the GUI by running:

```bash
python gui.py
```

---

## Deactivating the Virtual Environment

When you're done, deactivate the virtual environment with:

```bash
deactivate
```

---

> **Tip:** Always make sure the virtual environment is activated (you see `(venv)` in your terminal) before installing packages or running the app.
