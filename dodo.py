"""DoIt Script. Run all tasks with `poetry run doit` or single task with `poetry run doit run update_cl`."""

from pathlib import Path

from dash_dev.doit_base import DIG, debug_action, task_export_req  # noqa: F401
from dash_dev.doit_doc import (task_create_tag, task_document,  # noqa: F401
                               task_open_docs, task_remove_tag, task_update_cl)
from dash_dev.doit_lint import (task_auto_format, task_lint_pre_commit,  # noqa: F401
                                task_lint_project, task_radon_lint, task_set_lint_config)
from dash_dev.doit_test import (task_coverage, task_open_test_docs, task_ptw_current,  # noqa: F401
                                task_ptw_ff, task_ptw_marker, task_ptw_not_chrome, task_test,
                                task_test_all, task_test_keyword, task_test_marker)

# Configure Dash paths
DIG.set_paths(source_path=Path(__file__).resolve().parent)

# Create list of all tasks run with `poetry run doit`. Comment on/off as needed
DOIT_CONFIG = {
    'action_string_formatting': 'old',  # Required for keyword-based tasks
    'default_tasks': [
        'export_req', 'update_cl',
        'coverage',
        # 'open_test_docs',
        'set_lint_config',
        'auto_format',
        # 'lint_pre_commit',
        # 'type_checking',
        'document',
        # 'open_docs',
    ],
}
"""DoIt Configuration Settings. Run with `poetry run doit`."""


def task_write_puml():
    """Write updated PlantUML file(s) with `py2puml`."""
    pkg = DIG.pkg_name
    diagram_dir = DIG.source_path / '.diagrams'

    # TODO: pypi package wasn't working. Used local version
    run_py2puml = f'poetry run ../py-puml-tools/py2puml/py2puml.py --config {diagram_dir}/py2puml.ini'

    # # PLANNED: needs to be a bit more efficient...
    # > files = []
    # > for file_path in (DIG.source_path / pkg).glob('*.py'):
    # >     if any(line.startswith('class ') for line in file_path.read_text().split('\n')):
    # >         files.append(file_path.name)
    files = [
        'utils_app.py',
        'utils_app_modules.py',
        'utils_app_with_navigation.py',
        'utils_fig.py',
    ]
    return debug_action([
        f'{run_py2puml} -o {diagram_dir}/{pkg}.puml' + ''.join([f' {pkg}/{fn}' for fn in files]),
        f'plantuml {diagram_dir}/{pkg}.puml -tpng',
        # f'plantuml {diagram_dir}/{pkg}.puml -tsvg',

        # > f'{run_py2puml} -o {diagram_dir}/{pkg}-examples.puml ./tests/examples/*.py --root ./tests',
        # > f'plantuml {diagram_dir}/{pkg}-examples.puml -tsvg',
    ])
