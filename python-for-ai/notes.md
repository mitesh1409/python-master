# Python for AI - Full Beginner Course

Course link:  
[Python for AI - Full Beginner Course](https://www.youtube.com/watch?v=ygXn5nV5qFc)

---

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

### System Python

System Python remains untouched:

For example, on macOS:

```bash
/usr/bin/python3 → 3.9.6
```

That’s correct and safe.

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

You can get the available versions by running:

```bash
pyenv install --list
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

This is the isolated environment for the project.
Please ensure you are in the project directory when activating the environment to avoid confusion with other projects.
And remember to always activate the environment before installing dependencies or running project code to ensure you are using the correct Python version and packages.
You will need to activate the environment each time you start a new terminal session and want to work on the project.

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

---

## Interactive Python

**Prerequisites**  

Interactive Python requires the IPython kernel. Let’s install it:  

Make sure your virtual environment is activated:  
# You should see (venv) in your terminal

Install the required package:  

```bash
pip install ipykernel
```

This package allows Jupyter to run Python code interactively.

**Set up Interactive Python**  

Now let’s enable the interactive feature:  

1. Open VS Code settings:
    Press `Ctrl/Cmd + ,` (comma) Or File > Preferences > Settings
2. Search for “execute selection”
3. Find this setting: Jupyter > Interactive Window > Text Editor: Execute Selection
4. Check the box to enable it

What this does: When you press `Shift + Enter`, your selected code will run in the  
Jupyter interactive window instead of the Python terminal.  
This gives you a much richer, more visual experience.

That’s it! You’re ready to use interactive mode.
​
**Interactive superpowers**  
​
Run selected code  

* Highlight any code
* Press Shift + Enter
* Only that selection runs
​
Variables stay in memory  

Run this step by step:

```python
# First, create a variable
message = "Hello"

# Later, use it (even in a different cell)
print(message + " World!")

# Modify it
message = message.upper()
print(message)
```

The variable `message` stays available throughout your session!
