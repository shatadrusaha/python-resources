# `uv` - Guide

> ℹ️ Installation process is specific to `macOS` and `Linux`. Check `uv` [documentation](https://docs.astral.sh/uv/getting-started/installation/) for `Windows`.

## Table of Contents

- [1. Setup](#1-setup)
  - [1.1. Install](#11-install)
  - [1.2. Upgrade](#12-upgrade)
  - [1.3. Shell autocompletion](#13-shell-autocompletion)
  - [1.4. Uninstall](#14-uninstall)
- [2. Usage](#2-usage)
  - [2.1. Python](#21-python)
    - [2.1.1. Installing Python](#211-installing-python)
    - [2.1.2. Upgrading Python versions](#212-upgrading-python-versions)
    - [2.1.3. Viewing Python installations](#213-viewing-python-installations)
    - [2.1.4. Reinstalling Python](#214-reinstalling-python)
    - [2.1.5. Finding Python executable](#215-finding-python-executable)
    - [2.1.6. Others](#216-others)
  - [2.2. Projects](#22-projects)
    - [2.2.1. Applications](#221-applications)
    - [2.2.2. Packaged applications](#222-packaged-applications)
    - [2.2.3. Libraries](#223-libraries)
  - [2.3. Dependencies](#23-dependencies)
  - [2.4. Publishing packages](#24-publishing-packages)
- [3. Miscellaneous](#3-miscellaneous)
  - [3.1. Utility](#31-utility)
  - [3.2. Help menus](#32-help-menus)
  - [3.3. Verbose output](#33-verbose-output)
  - [3.4. View version](#34-view-version)

---

## 1. Setup

### 1.1. Install

`uv` can be installed in many ways. Check the official documentation for all possible ways. Use either of them to install it.

| Method | Command |
|--------|---------|
| Standalone installer | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| Standalone installer (specific version) | `curl -LsSf https://astral.sh/uv/0.11.6/install.sh \| sh` |
| Homebrew | `brew install uv` |

### 1.2. Upgrade

Upgrade `uv` depending on the installation method used:

| Installation Method | Command |
|---------------------|---------|
| Standalone installer (self-update) | `uv self update` |
| pip | `pip install --upgrade uv` |
| Homebrew | `brew upgrade uv` |

> ℹ️ When `uv` is installed via the standalone installer, it can update itself on-demand. When another installation method is used, self-updates are disabled. Use the package manager's upgrade method instead.


### 1.3. Shell autocompletion

Enable shell autocompletion for `uv` and `uvx` commands:

| Tool | Command |
|------|---------|
| `uv` | `echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc` |
| `uvx` | `echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc` |


### 1.4. Uninstall

To remove `uv` from the system, do the following:

- Clean up stored data (optional).

    ```bash
    uv cache clean
    rm -r "$(uv python dir)"
    rm -r "$(uv tool dir)"
    ```

- Remove the `uv` and `uvx` binaries.

    ```bash
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
| `uv python list --managed-python` | Show only uv-managed Python versions. |
| `uv python list --no-managed-python` | Show only system Python versions (exclude uv-managed). |

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

`uv` supports creating a project with `uv init`.

```bash
uv init hello-world
cd hello-world
```

Alternatively, initialize a project in the working directory.
```bash
mkdir hello-world
cd hello-world
uv init
```

> ℹ️ If there's a `pyproject.toml`, `uv` will exit with an error.

Custom project can also be created using `uv`.

```bash
# Initialise a project by defining the project-name and navigate to the project-folder.
uv init --python 3.11 demo_project_uv
uv init --python 3.11.6 demo_project_uv
uv init --python '==3.11.*' demo_project_uv
uv venv --python '>=3.11,<3.13' demo_project_uv

cd demo_project_uv

# Initialise a project in the existing folder/directory.
uv init --python 3.11
uv init --python 3.11.6
uv init --python '==3.11.*'
uv venv --python '>=3.11,<3.13'
```

```bash
# Create the 'venv' for/in the project/project-folder.
uv venv
```

When creating projects, uv supports two basic templates: `applications` and `libraries`. By default, uv will create a project for an application. The `--lib` flag can be used to create a project for a library instead.

#### 2.2.1. Applications

Application projects are suitable for web servers, scripts, and command-line interfaces.

Applications are the default target for uv init, but can also be specified with the --app flag.

```bash
uv init example-app
```

The project includes a pyproject.toml, a sample file (main.py), a readme, and a Python version pin file (.python-version).
```bash
tree example-app
```
```text
example-app
├── .python-version
├── README.md
├── main.py
└── pyproject.toml
```

#### 2.2.2. Packaged applications

Many use-cases require a package. For example, if you are creating a command-line interface that will be published to PyPI or if you want to define tests in a dedicated directory.

The `--package` flag can be used to create a packaged application:

```bash
uv init --package example-pkg
```

The source code is moved into a src directory with a module directory and an `__init__.py` file:

```bash
tree example-pkg
```
```text
example-pkg
├── .python-version
├── README.md
├── pyproject.toml
└── src
    └── example_pkg
        └── __init__.py
```

#### 2.2.3. Libraries

A library provides functions and objects for other projects to consume. Libraries are intended to be built and distributed, e.g., by uploading them to PyPI.

Libraries can be created by using the `--lib` flag:

```bash
uv init --lib example-lib
```

> ℹ️ Using --lib implies --package. Libraries always require a packaged project.

As with a packaged application, a src layout is used. A `py.typed` marker is included to indicate to consumers that types can be read from the library:

```bash
tree example-lib
```
```text
example-lib
├── .python-version
├── README.md
├── pyproject.toml
└── src
    └── example_lib
        ├── py.typed
        └── __init__.py
```


### 2.3. Dependencies

Add dependencies to the `pyproject.toml` with the `uv add` command. This will also update the lockfile and project environment. Some useful commands are listed below:

| Command | Description |
|---------|-------------|
| `uv add httpx` | Add a basic package |
| `uv add "httpx>=0.20"` | Add a package with version constraint |
| `uv add git+https://github.com/encode/httpx` | Add a git dependency over HTTP(S) |
| `uv add git+ssh://git@github.com/encode/httpx` | Add a git dependency over SSH |
| `uv add git+https://github.com/encode/httpx --tag 0.27.0` | Add a specific git tag |
| `uv add git+https://github.com/encode/httpx --branch main` | Add a specific git branch |
| `uv add /example/foo-0.1.0-py3-none-any.whl` | Add a package from a path |
| `uv add --dev pytest` | Add a development dependency |
| `uv add --group lint ruff` | Add to a dependency group |
| `uv remove requests` | Remove a package |
| `uv lock` | Create a lockfile for the project's dependencies. |
| `uv lock --upgrade-package requests` | Upgrade a specific package |
| `uv lock --upgrade` | Update all packages |
| `uv sync` | Sync virtual environment with lockfile |
| `uv run example.py` | Run a Python script. |
| `uv tree` | View the dependency tree for the project. |


### 2.4. Publishing packages

Manage versioning and publish your Python packages with uv commands. Build, update version numbers, and publish to PyPI.

| Command | Description |
|---------|-------------|
| `uv build` | Build your package |
| `uv version 1.0.0` | Update to an exact version |
| `uv version --bump major` | Bump the major version |
| `uv version --bump minor` | Bump the minor version |
| `uv version --bump patch` | Bump the patch version |
| `uv publish` | Publish your package |

By default, `uv build` will build the project in the current directory, and place the built artifacts in a `dist/` subdirectory:

```bash
uv build
ls dist/
```
```text
hello-world-0.1.0-py3-none-any.whl
hello-world-0.1.0.tar.gz
```

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
| `uv help <command>` | View the long help menu for a specific command (e.g., `uv help init`, `uv help python`). |

> ℹ️  When using the long help menu, `uv` will attempt to use `less` or `more` to "page" the output so it is not all displayed at once. To exit the pager, press `q`.

### 3.3. Verbose output

| Flag | Description |
|------|-------------|
| `-v` | Display verbose output for a command (e.g., `uv sync -v`). |
| `-vv` | Increase verbosity level (can be repeated, e.g., `uv sync -vv`). |

### 3.4. View version

| Command | Description |
|---------|-------------|
| `uv self version` | Check the installed version of uv. |
| `uv --version` | Same output as `uv self version`. |
| `uv -V` | Check version (excludes build commit and date). |
