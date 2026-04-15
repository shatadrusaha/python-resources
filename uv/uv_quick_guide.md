# UV - Quick Guide !!!

_N.B.: Installation process is specific to `MacOS` and `Linux`. Check `uv` [documentation](https://docs.astral.sh/uv/getting-started/installation/) for `Windows`._

## 1. Setup

### 1.1. Install

`uv` can be installed in many ways. Check the official documentation for all possible ways. Use either of them to install it.

```bash
# Standalone installer
curl -LsSf https://astral.sh/uv/install.sh | sh

# Standalone installer with spedific version
curl -LsSf https://astral.sh/uv/0.11.6/install.sh | sh

# Homebrew
brew install uv
```

### 1.2. Upgrade

When uv is installed via the standalone installer, it can update itself on-demand.

```bash
uv self update
```

When another installation method is used, self-updates are disabled. Use the package manager's upgrade method instead. For example,

```bash
# pip
pip install --upgrade uv

# Homebrew
brew upgrade uv
```

### 1.3. Shell autocompletion

Enable shell autocompletion for uv commands.

```bash
echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
```

Enable shell autocompletion for uvx.

```bash
echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc
```


### 1.4. Uninstall

To remove `uv` from the system, do the following:

- Clean up stored data (optional).

    ```bash
    uv cache clean
    rm -r "$(uv python dir)"
    rm -r "$(uv tool dir)"
    ```

- Remove the `uv` and `uvx` binaries.

    ```
    # Standalone installer
    rm ~/.local/bin/uv ~/.local/bin/uvx
    
    # Homebrew
    brew uninstall uv
    ```


## 2. Usage

### 2.1. Python

#### 2.1.1. Installing Python

To install Python versions managed by `uv`, use one of the below commands.

| Command | Description |
|---------|-------------|
| `uv python install` | Install the latest Python version. |
| `uv python install 3.12` | Install the latest patch version. |
| `uv python install 3.12.3` | Install a Python version at a specific version. |
| `uv python install '>=3.10,<3.13'` | Install a version that satisfies constraints. |
| `uv python install 3.11 3.12 3.13` | Install multiple Python versions. |
| `uv python install pypy@3.11` | Install a specific implementation (e.g., PyPy). |

#### 2.1.2. Upgrading Python versions

Upgrade installed Python versions to the latest supported patch release.

| Command | Description |
|---------|-------------|
| `uv python upgrade 3.12` | Upgrade a specific Python version to the latest patch. |
| `uv python upgrade` | Upgrade all uv-managed Python versions. |

#### 2.1.3. Viewing Python installations

View available and installed Python versions.

| Command | Description |
|---------|-------------|
| `uv python list` | List installed and available Python versions. |
| `uv python list 3.13` | Filter to show all Python 3.13 interpreters. |
| `uv python list pypy` | Filter to show all PyPy interpreters. |
| `uv python list --all-versions` | View all versions (includes old patch versions and downloads for other platforms). |
| `uv python list --all-platforms` | View Python versions for other platforms. |
| `uv python list --only-installed` | Exclude downloads and only show installed Python versions. |

#### 2.1.4. Reinstalling Python

Reinstall previously installed Python versions using the `--reinstall` flag.

| Command | Description |
|---------|-------------|
| `uv python install --reinstall` | Reinstall all previously installed Python versions. |


#### 2.1.5. Finding Python executable

Find a Python executable using the `uv python find` command. By default, this will display the path to the first available Python executable. If a `.venv` directory or `VIRTUAL_ENV` environment variable is set, it takes precedence over Python executables on the PATH.

| Command | Description |
|---------|-------------|
| `uv python find` | Display the path to the first available Python executable. |
| `uv python find '>=3.11'` | Find a Python executable with a version of 3.11 or newer (supports version constraints). |
| `uv python find --system` | Ignore virtual environments and search only system Python executables. |

#### 2.1.6. Others

| Command | Description |
|---------|-------------|
| `uv python pin` | Pin the current project to use a specific Python version. |
| `uv python uninstall` | Uninstall a Python version. |



### 2.2. Projects

Brief summary on Python projects' usage, i.e., with a `pyproject.toml`.

| Command | Description |
|---------|-------------|
| `uv init` | Create a new Python project. |
| `uv add` | Add a dependency to the project. |
| `uv remove` | Remove a dependency from the project. |
| `uv sync` | Sync the project's dependencies with the environment. |
| `uv lock` | Create a lockfile for the project's dependencies. |
| `uv run` | Run a command in the project environment. |
| `uv tree` | View the dependency tree for the project. |
| `uv build` | Build the project into distribution archives. |
| `uv publish` | Publish the project to a package index. |

#### 2.2.1. xyz

### 2.3. Dependencies

### 2.4. Publishing packages


## 3. Miscellaneous

### 3.1. Utility

| Command | Description |
|---------|-------------|
| `uv cache clean` | Remove cache entries. |
| `uv cache prune` | Remove outdated cache entries. |
| `uv cache dir` | Show the uv cache directory path. |
| `uv tool dir` | Show the uv tool directory path. |
| `uv python dir` | Show the uv installed Python versions path. |
| `uv self update` | Update uv to the latest version. |

### 3.2. Help menus

| Command | Description |
|---------|-------------|
| `uv --help` | View the condensed help menu for uv. |
| `uv <command> --help` | View the condensed help menu for a specific command (e.g., `uv init --help`). |
| `uv help` | View the longer help menu for all commands. |
| `uv help <command>` | View the long help menu for a specific command (e.g., `uv help init`). |

> **Note:** When using the long help menu, `uv` will attempt to use `less` or `more` to "page" the output so it is not all displayed at once. To exit the pager, press `q`.

### 3.3. Verbose output

| Flag | Description |
|------|-------------|
| `-v` | Display verbose output for a command (e.g., `uv sync -v`). |
| `-vv` | Increase verbosity level (can be repeated, e.g., `uv sync -vv`). |

### 3.4 View version

| Command | Description |
|---------|-------------|
| `uv self version` | Check the installed version of uv. |
| `uv --version` | Same output as `uv self version`. |
| `uv -V` | Check version (excludes build commit and date). |
