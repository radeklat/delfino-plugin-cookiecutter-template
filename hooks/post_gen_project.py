import shutil
from pathlib import Path
from subprocess import run

_FILEPATHS_TO_DELETE = {
    ".circleci": '{{cookiecutter.circleci_enabled}}' == 'no'
}

for filepath_str, should_be_deleted in _FILEPATHS_TO_DELETE.items():
    filepath = Path(filepath_str)

    if should_be_deleted:
        action = "Deleting"
        if filepath.is_file():
            filepath.unlink()
        elif filepath.is_dir():
            shutil.rmtree(filepath)
    else:
        action = "Not deleting"

    print(f"{action} {filepath_str}")

run(["poetry", "add", "delfino"])

if "{{cookiecutter.delfino_core_enabled}}" == "yes":
    run(["poetry", "add", "--group=dev", "delfino-core[verify-all]"])
