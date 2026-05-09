from fixtures.browsers_fixtures import browser,page, wikipedia
import pytest
from pathlib import Path
from datetime import datetime
from reporter import reporter


def pytest_runtest_setup(item):
    reporter.start(item.nodeid)

def pytest_addoption(parser):
    parser.addoption(
        "--browser-type",
        action="store",
        default="chromium",
        choices=["chromium", "firefox","webkit"],
        help="which browser to use"
    )   

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    setattr(item, f"rep_{call.when}", report)

    if call.when == "call":
        status = "PASS" if report.passed else "FAIL" if report.failed else "SKIP"
        reporter.end(status)

def pytest_sessionfinish(session, exitstatus):
    if not hasattr(session.config, "workerinput"):
        reporter.summary()