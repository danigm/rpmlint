import pytest
from rpmlint.checks.BuildRootAndDateCheck import BuildRootAndDateCheck
from rpmlint.filter import Filter

from Testing import CONFIG, get_tested_mock_package


@pytest.fixture(scope='function', autouse=True)
def buildrootcheck():
    CONFIG.info = True
    output = Filter(CONFIG)
    test = BuildRootAndDateCheck(CONFIG, output)
    return output, test


@pytest.mark.parametrize('package', [get_tested_mock_package(
files={
'/bin/trace': {'content': '/home/marxin/rpmbuild/BUILDROOT/buildroot-0-0.x86_64'}
}
)])
def test_build_root(package, buildrootcheck):
    output, test = buildrootcheck
    test.prepare_regex('/home/marxin/rpmbuild/BUILDROOT/%{NAME}-%{VERSION}-%{RELEASE}.x86_64')
    test.check(package)
    out = output.print_results(output.results)
    assert 'E: file-contains-buildroot /bin/trace' in out
