<h1 align="center" style="border-bottom: none;"> 🔌&nbsp;&nbsp;Delfino Plugin Cookiecutter Template&nbsp;&nbsp; 🔌</h1>
<h3 align="center">A <a href="https://cookiecutter.readthedocs.io">Cookiecutter</a> template for a <a href="https://github.com/radeklat/delfino">Delfino</a> plugin.</h3>

<p align="center">
    <img alt="Maintenance" src="https://img.shields.io/maintenance/yes/2022">
    <a href="https://github.com/radeklat/delfino-plugin-cookiecutter-template/commits/main">
        <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/radeklat/delfino-plugin-cookiecutter-template">
    </a>
</p>

# Creating project from this template

1. Install cookiecutter and required plugins:
   ```shell
   pip install cookiecutter jinja2-time
   ```
2. Create a new project using the Cookiecutter template:
   ```shell
   cookiecutter gh:radeklat/delfino-plugin-cookiecutter-template
   ```
3. Change into the new folder with `cd`
4. Initialize it as a git repository:
   ```shell
   git init
   git add .
   git commit -m "Initial commit"
   git tag initial
   ```
5. Create a Github repository with the same name as the resulting folder at https://github.com/new
6. Follow the instructions for _…or push an existing repository from the command line_
7. Push also the newly created initial tag:
   ```shell
   git push --tags
   ```
