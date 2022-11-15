import platform
import sys

import pytest

from cpymadtools._version import __version__, version_info


def test_version_info():
    info = version_info()
    assert isinstance(info, str)
    assert __version__ in info
    assert f"{sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}" in info
    assert platform.platform() in info
