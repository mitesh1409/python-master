# Python for AI - Full Beginner Course

Course link:  
[Python for AI - Full Beginner Course](https://www.youtube.com/watch?v=ygXn5nV5qFc)

## Python Setup on Mac

Step #1 Install Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Step #2 Install pyenv

```bash
brew install pyenv
```

Add following lines to shell configuration file (.zshrc or .bashrc):

```bash
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

Then run:

```bash
source ~/.zshrc
```

Then restart the terminal.

Step #3 Install the required Python version

You can get the available versions by running:

```bash
pyenv install --list
```

Install required version:

```bash
pyenv install 3.14.3
```

Set global:

```bash
pyenv global 3.14.3
```

Verify the installation:

```bash
python --version
python3 --version
```

Step #4 Verify Python installation

```bash
python --version
python3 --version
```

Both should show:

```bash
Python 3.14.3
```

```bash
which python
which python3
```

Both should point to:

```bash
~/.pyenv/shims/...
```

✔ Keep system Python untouched
✔ Use pyenv for development
✔ Never rely on global Homebrew Python

---

## 📘 Python Project Setup (professional)

---

### 1. System Requirements

* System Python must remain untouched.
* `pyenv` must be installed and configured.
* Required Python versions should be managed via `pyenv`.

---

### 2. Create Project Directory

```bash
mkdir my-project
cd my-project
```

---

### 3. Install Required Python Version (if not already installed)

Check installed versions:

```bash
pyenv versions
```

If the required version is missing:

```bash
pyenv install <required-version>
```

Example:

```bash
pyenv install 3.12.2
```

---

### 4. Set Local Python Version for the Project

```bash
pyenv local <required-version>
```

This creates:

```
.python-version
```

This file defines the Python version for the project directory.

Commit this file to version control.

---

### 5. Verify Active Interpreter

Before creating the virtual environment:

```bash
python --version
which python
```

Expected output:

* Correct Python version
* Path pointing to `~/.pyenv/shims/python`

---

### 6. Create Virtual Environment

```bash
python -m venv .venv
```

This creates an isolated environment using the locally selected Python version.

---

### 7. Activate Virtual Environment

```bash
source .venv/bin/activate
```

Your shell prompt will indicate activation.

Verify:

```bash
which python
```

Should point to:

```
./.venv/bin/python
```

---

### 8. Upgrade pip

```bash
python -m pip install --upgrade pip
```

Ensures latest packaging tools inside the environment.

---

### 9. Install Project Dependencies

Example:

```bash
pip install pandas numpy
```

---

### 10. Freeze Dependencies

```bash
pip freeze > requirements.txt
```

Commit:

```
requirements.txt
```

This ensures reproducibility.

---

### 11. Git Configuration

Add to `.gitignore`:

```
.venv/
```

Commit the following files:

* `.python-version`
* `requirements.txt`
* Source code

Do NOT commit:

* `.venv/`

---

### 🔁 Teammate Setup After `git clone`

```bash
pyenv install <required-version>   # if needed
pyenv local <required-version>
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Environment recreated deterministically.

---

### 🏗 Final Project Structure

```
my-project/
│
├── .python-version
├── requirements.txt
├── .gitignore
├── src/
└── .venv/  (ignored)
```

---

### 🎯 Architecture Guarantees

* System Python untouched
* Project-level version locking
* Isolated dependency management
* Reproducible environments
* Cross-machine consistency
* Clean separation of concerns
