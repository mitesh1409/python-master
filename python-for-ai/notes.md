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

Step #3 Install latest Python version

```bash
pyenv install 3.14.3
```

You can get the available versions by running:

```bash
pyenv install --list
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

```
Python 3.14.3
```

```bash
which python
which python3
```

Both should point to:

```
~/.pyenv/shims/...
```

✔ Keep system Python untouched
✔ Use pyenv for development
✔ Never rely on global Homebrew Python

