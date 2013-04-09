from __future__ import absolute_import, division
# vim: set fileencoding=utf-8 :
import sys
from nose_pyversion import PyVersion


def test_version_match():
    """Test that PyVersion returns None on matching filenames and False on
    non-matching filenames"""

    print 'testing'

    separator = '-'

    pyversion = PyVersion()
    pyversion.separator = separator

    assert pyversion.wantFile('file.py'.format(*sys.version_info
                                                     )) is None
    assert pyversion.wantFile('file-py{0}.py'.format(*sys.version_info
                                                     )) is None
    assert pyversion.wantFile('file-py{0}{1}.py'.format(*sys.version_info
                                                        )) is None
    assert pyversion.wantFile('file-py{0}{1}{2}.py'.format(*sys.version_info
                                                           )) is None

    # Cannot test this any other way, if minor and micro version is the same
    # this cannot be tested.
    if sys.version_info.micro is not sys.version_info.minor:
        assert pyversion.wantFile('file-py{0}{2}.py'.format(*sys.version_info)) is False

    major, minor, micro = sys.version_info[0:3]
    assert pyversion.wantFile('file-py{0}{1}.py'.format(
        major + 1,
        minor
    )) is False
    assert pyversion.wantFile('file-py{0}{1}.py'.format(
        major,
        minor - 1 if minor > 0 else minor + 1
    )) is False
    assert pyversion.wantFile('file-py{0}{1}{2}.py'.format(
        major,
        minor - 1 if minor > 0 else minor + 1,
        micro
    )) is False
    assert pyversion.wantFile('file-py{0}{1}{2}.py'.format(
        major,
        minor,
        micro - 1 if micro > 0 else micro + 1
    )) is False
