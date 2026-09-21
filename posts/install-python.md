# Install Python

Using "uv" to install and manage multiple Python versions.  

Reference:  

* [uv](https://docs.astral.sh/uv/)
* [uv > Installation](https://docs.astral.sh/uv/getting-started/installation/)
* [uv > Features](https://docs.astral.sh/uv/getting-started/features/)

---

## Step #1: Install uv

https://docs.astral.sh/uv/getting-started/installation/

---

## Step #2: Install Python using uv

`uv python install`  

It will install the latest Python version.

Reference: https://docs.astral.sh/uv/guides/install-python/

`uv python find`  

Find an installed Python version.

---

## Step #3: Make OS to use Python version installed using uv.

`which python3`  

It still shows system Python.

```bash
$ which python3  
/usr/bin/python3  
```

Add uv's Python to PATH (recommended).  

Add this to your ~/.bashrc or ~/.zshrc:

```bash
export PATH="$HOME/.local/share/uv/python/cpython-3.14-linux-x86_64-gnu/bin:$PATH"
```

Then reload:

```bash
source ~/.bashrc
```

Verify:

```bash
which python3        # should now show uv's path
python3 --version    # should show installed Python version
```
