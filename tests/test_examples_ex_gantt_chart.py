"""Test the file examples/ex_gantt_chart.py."""

import pytest

from .configuration import no_log_errors
from .examples import ex_gantt_chart


@pytest.mark.CHROME
def test_smoke_test_ex_gantt_chart(dash_duo):
    dash_duo.start_server(ex_gantt_chart.app.app)

    import time
    time.sleep(1)

    assert no_log_errors(dash_duo)
