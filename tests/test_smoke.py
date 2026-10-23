"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import scribegen


def test_version_is_set() -> None:
    assert scribegen.__version__
