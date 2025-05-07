# UV - macOS !!!

# TODO - correct the ToC

## Table of Contents
- [Getting started](#getting-started-)
  - [Installation](#installation)
  - [Upgrading uv](#upgrading-uv)
  - [Shell autocompletion](#shell-autocompletion)
  - [Uninstallation](#uninstallation)
- [Features](#features)
  - [Python versions](#python-versions)
  - [Scripts](#scripts)
  - [Projects](#projects)
  - [Tools](#tools)
  - [Utility](#utility)
- [Guides](#guides)
  - [Installing Python](#installing-python)
  - [Projects](#projects-1)
    - [Creating a new project](#creating-a-new-project)
    - [Custom project](#custom-project)
    - [More on projects](#more-on-projects)
    - [Managing dependencies](#managing-dependencies)
    - [Building distributions](#building-distributions)
  - [Python versions](#python-versions-1)
- [Getting help](#getting-help)

## Getting started -

### [Installation](https://docs.astral.sh/uv/getting-started/installation/)

- _Installing uv_

    ```bash
    # Standalone installer
    curl -LsSf https://astral.sh/uv/install.sh | sh

    # Homebrew
    brew install uv
    ```

- _Upgrading uv_

    When uv is installed via the standalone installer, it can update itself on-demand:

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

- _Shell autocompletion_

    To enable shell autocompletion for uv commands, run one of the following:

    ```bash
    echo 'eval "$(uv generate-shell-completion zsh)"' >> ~/.zshrc
    ```

    To enable shell autocompletion for uvx, run one of the following:
    ```bash
    echo 'eval "$(uvx --generate-shell-completion zsh)"' >> ~/.zshrc
    ```


- _Uninstallation_

    ```bash
    # Standalone installer

    # Clean up stored data (optional):
    uv cache clean
    rm -r "$(uv python dir)"
    rm -r "$(uv tool dir)"

    # Remove the uv and uvx binaries:
    rm ~/.local/bin/uv ~/.local/bin/uvx
    ```

    ```bash
    # Homebrew
    brew uninstall uv
    ```


### [Features](https://docs.astral.sh/uv/getting-started/features/)

uv provides essential features for Python development — from installing Python and hacking on simple scripts to working on large projects that support multiple Python versions and platforms.

uv's interface can be broken down into sections, which are usable independently or together.

- _Python versions_

    Installing and managing Python itself.

    ```bash
    uv python install # Install Python versions.
    uv python list # View available Python versions.
    uv python find # Find an installed Python version.
    uv python pin # Pin the current project to use a specific Python version.
    uv python uninstall # Uninstall a Python version.
    ```
    See the [guide on installing Python](https://docs.astral.sh/uv/guides/install-python/) to get started.

- _Scripts_

    Executing standalone Python scripts, e.g., ```example.py```.

    ```bash
    uv run # Run a script.
    uv add --script # Add a dependency to a script.
    uv remove --script # Remove a dependency from a script.
    ```
    See the [guide on running scripts](https://docs.astral.sh/uv/guides/scripts/) to get started.

- _Projects_

    Creating and working on Python projects, i.e., with a ```pyproject.toml```.

    ```bash
    uv init # Create a new Python project.
    uv add # Add a dependency to the project.
    uv remove # Remove a dependency from the project.
    uv sync # Sync the project's dependencies with the environment.
    uv lock # Create a lockfile for the project's dependencies.
    uv run # Run a command in the project environment.
    uv tree # View the dependency tree for the project.
    uv build # Build the project into distribution archives.
    uv publish # Publish the project to a package index.
    ```

    See the [guide on projects](https://docs.astral.sh/uv/guides/projects/) to get started.

- _Tools_

    Running and installing tools published to Python package indexes, e.g., ```ruff``` or ```black```.

    ```bash
    uv tool run # Run a tool in a temporary environment.
    uv tool install # Install a tool user-wide.
    uv tool uninstall # Uninstall a tool.
    uv tool list # List installed tools.
    uv tool update-shell # Update the shell to include tool executables.
    ```
    See the [guide on tools](https://docs.astral.sh/uv/guides/tools/) to get started.

- _Utility_

    Managing and inspecting uv's state, such as the cache, storage directories, or performing a self-update:

    ```bash
    uv cache clean # Remove cache entries.
    uv cache prune # Remove outdated cache entries.
    uv cache dir # Show the uv cache directory path.
    uv tool dir # Show the uv tool directory path.
    uv python dir # Show the uv installed Python versions path.
    uv self update # Update uv to the latest version.
    ```


## Guides - 

### [Installing Python](https://docs.astral.sh/uv/guides/install-python/)
If Python is already installed on your system, uv will detect and use it without configuration. However, uv can also install and manage Python versions. uv automatically installs missing Python versions as needed — you don't need to install Python to get started.

```bash
# To install the latest Python version.
uv python install

# To install a specific Python version.
uv python install 3.12

# To install multiple Python versions.
uv python install 3.11 3.12

# To install a version that satisfies constraints.
uv python install '>=3.8,<3.10'
```

### [Projects](https://docs.astral.sh/uv/concepts/projects/)

- [_Creating a new project_](https://docs.astral.sh/uv/guides/projects/)
    
    Create a new Python project using the `uv init` command.
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

    _N.B. : If there's a `pyproject.toml`, `uv` will exit with an error._

- _Custom project_
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

- [_More on projects_](https://docs.astral.sh/uv/concepts/projects/init/#creating-projects)

    When creating projects, uv supports two basic templates: `applications` and `libraries`. By default, `uv` will create a project for an application. The `--lib` flag can be used to create a project for a library instead.

    - _Applications_

        Application projects are suitable for web servers, scripts, and command-line interfaces. Applications are the default target for `uv init`, but can also be specified with the `--app `flag.

        ```bash
        uv init example-app
        uv init --app example-app
        ```
        
        The project includes a `pyproject.toml`, a sample file (`main.py`), a readme, and a Python version pin file (`.python-version`).

        ```bash
        tree example-app
        example-app
        ├── .python-version
        ├── README.md
        ├── main.py
        └── pyproject.toml
        ```

        The `pyproject.toml` includes basic metadata. It does not include a build system, it is not a package and will not be installed into the environment.

        ```bash
        pyproject.toml

        [project]
        name = "example-app"
        version = "0.1.0"
        description = "Add your description here"
        readme = "README.md"
        requires-python = ">=3.11"
        dependencies = []
        ```

    - _Packaged applications_
        
        Many use-cases require a package. For example, if you are creating a command-line interface that will be published to PyPI or if you want to define tests in a dedicated directory.
        
        The --package flag can be used to create a packaged application:


        ```bash
        uv init --package example-pkg
        ```
        
        The source code is moved into a src directory with a module directory and an `__init__.py` file.

        ```bash
        tree example-pkg
        example-pkg
        ├── .python-version
        ├── README.md
        ├── pyproject.toml
        └── src
            └── example_pkg
                └── __init__.py
        ```

        A `build-system` is defined, so the project will be installed into the environment, and a command definition (`project.scripts`) is included.

        ```bash
        pyproject.toml

        [project]
        name = "example-pkg"
        version = "0.1.0"
        description = "Add your description here"
        readme = "README.md"
        requires-python = ">=3.11"
        dependencies = []

        [project.scripts]
        example-pkg = "example_pkg:main"

        [build-system]
        requires = ["hatchling"]
        build-backend = "hatchling.build"
        ```

    - _Libraries_

        A library provides functions and objects for other projects to consume. Libraries are intended to be built and distributed, e.g., by uploading them to `PyPI`.

        Libraries can be created by using the `--lib` flag.

        ```bash
        uv init --lib example-lib
        ```

        _N.B. : Using `--lib` implies `--package`. Libraries always require a packaged project._

        As with a packaged application, a `src` layout is used. A `py.typed` marker is included to indicate to consumers that types can be read from the library.


        ```bash
        tree example-lib
        example-lib
        ├── .python-version
        ├── README.md
        ├── pyproject.toml
        └── src
            └── example_lib
                ├── py.typed
                └── __init__.py
        ```

        A build system is defined, so the project will be installed into the environment:

        ```bash
        pyproject.toml

        [project]
        name = "example-lib"
        version = "0.1.0"
        description = "Add your description here"
        readme = "README.md"
        requires-python = ">=3.11"
        dependencies = []

        [build-system]
        requires = ["hatchling"]
        build-backend = "hatchling.build"
        ```

- [_Managing dependencies_](https://docs.astral.sh/uv/concepts/projects/dependencies/)

    Add dependencies to the `pyproject.toml` with the `uv add` command. This will also update the lockfile and project environment.

    ```bash
    uv add requests

    # Specify a version constraint
    uv add 'requests==2.31.0'

    # Add a git dependency
    uv add git+https://github.com/psf/requests
    ```

    To remove a package, use `uv remove`.
    ```bash
    uv remove requests
    ```

    To upgrade a package, `run uv` lock with the `--upgrade-package` flag.
    ```bash
    uv lock --upgrade-package requests
    ```

    The `--upgrade-package` flag will attempt to update the specified package to the latest compatible version, while keeping the rest of the lockfile intact.
    
- _Update/Create and activate an enviornment_
    ```bash
    uv sync
    source .venv/bin/activate
    ```

- [_Building distributions_](https://docs.astral.sh/uv/concepts/projects/build/)

    `uv build` can be used to build source distributions and binary distributions (wheel) for your project.
    
    By default, `uv build` will build the project in the current directory, and place the built artifacts in a `dist/` subdirectory:

    ```bash
    uv build
    ls dist/
    # hello-world-0.1.0-py3-none-any.whl
    # hello-world-0.1.0.tar.gz
    ```


### [Python versions](https://docs.astral.sh/uv/concepts/python-versions/#requesting-a-version)

```bash
uv help python
# q --> to exit
```

[_Viewing available Python versions_]((https://docs.astral.sh/uv/concepts/python-versions/#viewing-available-python-versions)) - [uv-python-list](https://docs.astral.sh/uv/reference/cli/#uv-python-list)

```bash
# To list installed and available Python versions
uv python list

# To filter the Python versions, provide a request, e.g., to show all Python 3.13 interpreters
uv python list 3.13
```

By default, downloads for other platforms and old patch versions are hidden.
```bash
# To view all versions
uv python list --all-versions

# To view Python versions for other platforms
uv python list --all-platforms

# To exclude downloads and only show installed Python versions
uv python list --only-installed
```



_Requesting a version_ -    
A specific Python version can be requested with the --python flag in most uv commands. For example, when creating a virtual environment:

```bash
# Requesting a version
uv venv --python 3.11.6
uv venv --python 3.11
uv venv --python '>=3.11,<3.13'
```

_Finding a Python executable_ -

```bash
# To find a Python executable, use the uv python find command
uv python find
```

By default, this will display the path to the first available Python executable. See the [discovery rules](https://docs.astral.sh/uv/concepts/python-versions/#discovery-of-python-versions) for details about how executables are discovered.

This interface also supports many [request formats](https://docs.astral.sh/uv/concepts/python-versions/#requesting-a-version), e.g., to find a Python executable that has a version of 3.11 or newer.

```bash
uv python find '>=3.11'
```

By default, uv python find will include Python versions from virtual environments. If a .venv directory is found in the working directory or any of the parent directories or the VIRTUAL_ENV environment variable is set, it will take precedence over any Python executables on the PATH.

To ignore virtual environments, use the --system flag.

```bash
uv python find --system
```

_Requiring or disabling managed Python versions_ -
By default, uv will attempt to use Python versions found on the system and only download managed Python versions when necessary. To ignore system Python versions, and only use managed Python versions, use the --managed-python flag.

```bash
uv python list --managed-python
```

Similarly, to ignore managed Python versions and only use system Python versions, use the --no-managed-python flag.

```bash
uv python list --no-managed-python
```


### [Getting help](https://docs.astral.sh/uv/getting-started/help/)

- _Help menus_

    The ```--help``` flag can be used to view the help menu for a command, e.g., for ```uv```:

    ```bash
    uv --help
    ```

    To view the help menu for a specific command, e.g., for ```uv init```:

    ```bash
    uv init --help
    ```

    When using the ```--help``` flag, uv displays a condensed help menu. To view a longer help menu for a command, use ```uv help```:

    ```bash
    uv help
    ```

    To view the long help menu for a specific command, e.g., for ```uv init```:

    ```bash
    uv help init
    ```

    When using the long help menu, uv will attempt to use ```less``` or ```more``` to "page" the output so it is not all displayed at once.

    ___To exit the pager, press ```q```.___

- _Viewing the version_

    When seeking help, it's important to determine the version of uv that you're using — sometimes the problem is already solved in a newer version.

    To check the installed version:

    ```bash
    uv version
    ```
    
    The following are also valid:

    ```bash
    uv --version      # Same output as `uv version`
    uv -V             # Will not include the build commit and date
    uv pip --version  # Can be used with a subcommand
    ```
