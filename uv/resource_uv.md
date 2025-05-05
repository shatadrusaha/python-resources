# UV - macOS !!!

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
    



## Guides - 

### [Installing Python](https://docs.astral.sh/uv/guides/install-python/)

- 






















### Python versions

[requesting-a-version](https://docs.astral.sh/uv/concepts/python-versions/#requesting-a-version)

```bash
uv help python
# q --> to exit
```

- _Requesting a version_ -
    
    A specific Python version can be requested with the --python flag in most uv commands. For example, when creating a virtual environment:

    ```bash
    # Requesting a version
    uv venv --python 3.11.6
    uv venv --python 3.11
    uv venv --python '>=3.11,<3.13'
    ```

- _Installing a Python version_ -

    ```bash
    # To install a Python version at a specific version
    uv python install 3.12.3
    
    # To install the latest patch version
    uv python install 3.12
    
    # To install a version that satisfies constraints
    uv python install '>=3.8,<3.10'

    # To install multiple versions
    uv python install 3.9 3.10 3.11
    ```

- _Viewing available Python versions_ - 

    [viewing-available-python-versions](https://docs.astral.sh/uv/concepts/python-versions/#viewing-available-python-versions)

    [uv-python-list](https://docs.astral.sh/uv/reference/cli/#uv-python-list)

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

- Finding a Python executable

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

- Requiring or disabling managed Python versions

    By default, uv will attempt to use Python versions found on the system and only download managed Python versions when necessary. To ignore system Python versions, and only use managed Python versions, use the --managed-python flag.

    ```bash
    uv python list --managed-python
    ```

    Similarly, to ignore managed Python versions and only use system Python versions, use the --no-managed-python flag.

    ```bash
    uv python list --no-managed-python
    ```