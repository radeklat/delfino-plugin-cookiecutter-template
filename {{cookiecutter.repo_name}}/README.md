<h1 align="center" style="border-bottom: none;"> 🔌&nbsp;&nbsp;{{cookiecutter.project_name}}&nbsp;&nbsp; 🔌</h1>
<h3 align="center">{{cookiecutter.project_short_description}}</h3>

<p align="center">
{%- if cookiecutter.circleci_enabled == "yes" %}
    <a href="https://app.circleci.com/pipelines/github/{{cookiecutter.github_repo_owner}}/{{cookiecutter.repo_name}}?branch=main">
        <img alt="CircleCI" src="https://img.shields.io/circleci/build/github/{{cookiecutter.github_repo_owner}}/{{cookiecutter.repo_name}}">
    </a>{% endif %}
{%- if cookiecutter.codecov_enabled == "yes" %}
    <a href="https://app.codecov.io/gh/{{cookiecutter.github_repo_owner}}/delfino-core/">
        <img alt="Codecov" src="https://img.shields.io/codecov/c/github/{{cookiecutter.github_repo_owner}}/{{cookiecutter.repo_name}}">
    </a>{% endif %}
    <a href="https://github.com/{{cookiecutter.github_repo_owner}}/delfino-core/tags">
        <img alt="GitHub tag (latest SemVer)" src="https://img.shields.io/github/tag/{{cookiecutter.github_repo_owner}}/{{cookiecutter.repo_name}}">
    </a>
    <img alt="Maintenance" src="https://img.shields.io/maintenance/yes/{% now 'local', '%Y' %}">
    <a href="https://github.com/{{cookiecutter.github_repo_owner}}/{{cookiecutter.repo_name}}/commits/main">
        <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/{{cookiecutter.github_repo_owner}}/{{cookiecutter.repo_name}}">
    </a>
{%- if cookiecutter.hosted_on_pypi == "yes" %}
    <a href="https://www.python.org/doc/versions/">
        <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/{{cookiecutter.repo_name}}">
    </a>
    <a href="https://pypistats.org/packages/{{cookiecutter.repo_name}}">
        <img alt="Downloads" src="https://img.shields.io/pypi/dm/{{cookiecutter.repo_name}}">
    </a>{% endif %}
</p>

# Commands
  
| Command               | Description             |
|-----------------------|-------------------------|
| demo                  | An example demo command |

# Installation

- pip: `pip install {{cookiecutter.repo_name}}`
- Poetry: `poetry add -D {{cookiecutter.repo_name}}`
- Pipenv: `pipenv install -d {{cookiecutter.repo_name}}`

<!-- PUT DEPENDENCIES OF INDIVIDUAL COMMANDS AS EXTRAS -->
<!--
## Optional dependencies

Each project may use different sub-set of [commands](#commands). Therefore, dependencies of all commands are optional and checked only when the command is executed.

Using `[all]` installs all the [optional dependencies](https://setuptools.pypa.io/en/latest/userguide/dependency_management.html#optional-dependencies) used by all the commands. If you want only a sub-set of those dependencies, there are finer-grained groups available:

- `demo`
-->

# Configuration

Delfino doesn't load any plugins by default. To enable this plugin, add the following config into `pyproject.toml`:

```toml
[tool.delfino.plugins.{{cookiecutter.repo_name}}]

```

<!-- PLUGIN MAY NEED CONFIGURATION -->
<!--
## Plugin configuration

This plugin has several options. All the values are optional and defaults are shown below: 

```toml
[tool.delfino.plugins.{{cookiecutter.repo_name}}]
# Config option description
config_option_name = "default value"
```
-->

<!-- INDIVIDUAL COMMANDS MAY NEED CONFIGURATION -->
<!--
## Commands configuration

Several commands have their own configuration as well:

```toml
[tool.delfino.plugins.{{cookiecutter.repo_name}}.demo]
# Config option description
config_option_name = "default value"
```
-->

# Usage

Run `delfino --help`.
