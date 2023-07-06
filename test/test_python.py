import pytest
from rpmlint.checks.PythonCheck import PythonCheck
from rpmlint.filter import Filter

from Testing import CONFIG, get_tested_mock_package, get_tested_package


@pytest.fixture(scope='function', autouse=True)
def pythoncheck():
    CONFIG.info = True
    output = Filter(CONFIG)
    test = PythonCheck(CONFIG, output)
    return output, test


@pytest.mark.parametrize('package', [get_tested_mock_package(
    files={
        '/usr/lib/python2.7/site-packages/python-mypackage/doc': {'content': ''},
        '/usr/lib/python2.7/site-packages/python-mypackage/docs': {'content': ''},
        '/usr/lib/python3.10/site-packages/python-mypackage/doc': {'content': ''},
        '/usr/lib/python3.10/site-packages/python-mypackage/docs': {'content': ''},
        '/usr/lib64/python2.7/site-packages/python-mypackage/doc': {'content': ''},
        '/usr/lib64/python2.7/site-packages/python-mypackage/docs': {'content': ''},
        '/usr/lib64/python3.10/site-packages/python-mypackage/doc': {'content': ''},
        '/usr/lib64/python3.10/site-packages/python-mypackage/docs': {'content': ''}
    }
)])
def test_python_doc_in_package(package, pythoncheck):
    output, test = pythoncheck
    test.check(package)
    out = output.print_results(output.results)
    assert 'W: python-doc-in-package /usr/lib/python2.7/site-packages/python-mypackage/doc' in out
    assert 'W: python-doc-in-package /usr/lib/python2.7/site-packages/python-mypackage/docs' in out
    assert 'W: python-doc-in-package /usr/lib/python3.10/site-packages/python-mypackage/doc' in out
    assert 'W: python-doc-in-package /usr/lib/python3.10/site-packages/python-mypackage/docs' in out
    assert 'W: python-doc-in-package /usr/lib64/python2.7/site-packages/python-mypackage/doc' in out
    assert 'W: python-doc-in-package /usr/lib64/python2.7/site-packages/python-mypackage/docs' in out
    assert 'W: python-doc-in-package /usr/lib64/python3.10/site-packages/python-mypackage/doc' in out
    assert 'W: python-doc-in-package /usr/lib64/python3.10/site-packages/python-mypackage/docs' in out


@pytest.mark.parametrize('package', [get_tested_mock_package(
    files={
        '/usr/lib/python2.7/site-packages/python-mypackage/doc/__init__.py': {'content': '', 'create_dirs': True, 'include_dirs': 2},
        '/usr/lib/python2.7/site-packages/python-mypackage/docs/__init__.py': {'content': '', 'create_dirs': True, 'include_dirs': 1},
        '/usr/lib64/python2.7/site-packages/python-mypackage/doc/__init__.py': {'content': '', 'create_dirs': True, 'include_dirs': 2},
        '/usr/lib64/python2.7/site-packages/python-mypackage/docs/__init__.py': {'content': '', 'create_dirs': True, 'include_dirs': 1},
        '/usr/lib/python3.10/site-packages/python-mypackage/doc/__init__.py': {'content': '', 'create_dirs': True, 'include_dirs': 2},
        '/usr/lib/python3.10/site-packages/python-mypackage/docs/__init__.py': {'content': '', 'create_dirs': True, 'include_dirs': 1},
        '/usr/lib64/python3.10/site-packages/python-mypackage/doc/__init__.py': {'content': '', 'create_dirs': True, 'include_dirs': 2},
        '/usr/lib64/python3.10/site-packages/python-mypackage/docs/__init__.py': {'content': '', 'create_dirs': True, 'include_dirs': 1}
    }
)])
def test_python_doc_module_in_package(package, pythoncheck):
    output, test = pythoncheck
    test.check(package)
    out = output.print_results(output.results)
    assert 'W: python-doc-in-package /usr/lib/python2.7/site-packages/python-mypackage/doc' not in out
    assert 'W: python-doc-in-package /usr/lib/python2.7/site-packages/python-mypackage/docs' not in out
    assert 'W: python-doc-in-package /usr/lib/python3.10/site-packages/python-mypackage/doc' not in out
    assert 'W: python-doc-in-package /usr/lib/python3.10/site-packages/python-mypackage/docs' not in out
    assert 'W: python-doc-in-package /usr/lib64/python2.7/site-packages/python-mypackage/doc' not in out
    assert 'W: python-doc-in-package /usr/lib64/python2.7/site-packages/python-mypackage/docs' not in out
    assert 'W: python-doc-in-package /usr/lib64/python3.10/site-packages/python-mypackage/doc' not in out
    assert 'W: python-doc-in-package /usr/lib64/python3.10/site-packages/python-mypackage/docs' not in out


@pytest.mark.parametrize('package', [get_tested_mock_package(
    files={
        '/usr/lib/python2.7/site-packages/mydistutilspackage.egg-info': {'content': 'Metadata-Version: 2.1\nName: pythoncheck', 'create_dirs': False},
        '/usr/lib/python3.10/site-packages/mydistutilspackage.egg-info': {'content': 'Metadata-Version: 2.1\nName: pythoncheck', 'create_dirs': False},
        '/usr/lib64/python2.7/site-packages/mydistutilspackage.egg-info': {'content': 'Metadata-Version: 2.1\nName: pythoncheck', 'create_dirs': False},
        '/usr/lib64/python3.10/site-packages/mydistutilspackage.egg-info': {'content': 'Metadata-Version: 2.1\nName: pythoncheck', 'create_dirs': False}
    },
    real_files=True
)])
def test_python_distutils_egg_info(package, pythoncheck):
    output, test = pythoncheck
    test.check(package)
    out = output.print_results(output.results)
    assert 'E: python-egg-info-distutils-style /usr/lib/python2.7/site-packages/mydistutilspackage.egg-info' in out
    assert 'E: python-egg-info-distutils-style /usr/lib/python3.10/site-packages/mydistutilspackage.egg-info' in out
    assert 'E: python-egg-info-distutils-style /usr/lib64/python2.7/site-packages/mydistutilspackage.egg-info' in out
    assert 'E: python-egg-info-distutils-style /usr/lib64/python3.10/site-packages/mydistutilspackage.egg-info' in out


@pytest.mark.parametrize('package', [get_tested_mock_package(
    files={
        '/usr/lib/python2.7/site-packages/doc': {'content': '', 'create_dirs': False},
        '/usr/lib/python2.7/site-packages/docs': {'content': '', 'create_dirs': False},
        '/usr/lib/python3.10/site-packages/doc': {'content': '', 'create_dirs': False},
        '/usr/lib/python3.10/site-packages/docs': {'content': '', 'create_dirs': False},
        '/usr/lib64/python2.7/site-packages/doc': {'content': '', 'create_dirs': False},
        '/usr/lib64/python2.7/site-packages/docs': {'content': '', 'create_dirs': False},
        '/usr/lib64/python3.10/site-packages/doc': {'content': '', 'create_dirs': False},
        '/usr/lib64/python3.10/site-packages/docs': {'content': '', 'create_dirs': False}
    }
)])
def test_python_doc_in_site_packages(package, pythoncheck):
    output, test = pythoncheck
    test.check(package)
    out = output.print_results(output.results)
    assert 'E: python-doc-in-site-packages /usr/lib/python2.7/site-packages/doc' in out
    assert 'E: python-doc-in-site-packages /usr/lib/python2.7/site-packages/docs' in out
    assert 'E: python-doc-in-site-packages /usr/lib/python3.10/site-packages/doc' in out
    assert 'E: python-doc-in-site-packages /usr/lib/python3.10/site-packages/docs' in out
    assert 'E: python-doc-in-site-packages /usr/lib64/python2.7/site-packages/doc' in out
    assert 'E: python-doc-in-site-packages /usr/lib64/python2.7/site-packages/docs' in out
    assert 'E: python-doc-in-site-packages /usr/lib64/python3.10/site-packages/doc' in out
    assert 'E: python-doc-in-site-packages /usr/lib64/python3.10/site-packages/docs' in out


@pytest.mark.parametrize('package', [get_tested_mock_package(
    files={
        '/usr/lib/python2.7/site-packages/src': {'content': '', 'create_dirs': False},
        '/usr/lib/python3.10/site-packages/src': {'content': '', 'create_dirs': False},
        '/usr/lib64/python2.7/site-packages/src': {'content': '', 'create_dirs': False},
        '/usr/lib64/python3.10/site-packages/src': {'content': '', 'create_dirs': False}
    }
)])
def test_python_src_in_site_packages(package, pythoncheck):
    output, test = pythoncheck
    test.check(package)
    out = output.print_results(output.results)
    assert 'E: python-src-in-site-packages /usr/lib/python2.7/site-packages/src' in out
    assert 'E: python-src-in-site-packages /usr/lib/python3.10/site-packages/src' in out
    assert 'E: python-src-in-site-packages /usr/lib64/python2.7/site-packages/src' in out
    assert 'E: python-src-in-site-packages /usr/lib64/python3.10/site-packages/src' in out


@pytest.mark.parametrize('package', [get_tested_mock_package(
    files={
        '/usr/lib/python2.7/site-packages/test': {'content': '', 'create_dirs': False},
        '/usr/lib/python2.7/site-packages/tests': {'content': '', 'create_dirs': False},
        '/usr/lib/python3.10/site-packages/test': {'content': '', 'create_dirs': False},
        '/usr/lib/python3.10/site-packages/tests': {'content': '', 'create_dirs': False},
        '/usr/lib64/python2.7/site-packages/test': {'content': '', 'create_dirs': False},
        '/usr/lib64/python2.7/site-packages/tests': {'content': '', 'create_dirs': False},
        '/usr/lib64/python3.10/site-packages/test': {'content': '', 'create_dirs': False},
        '/usr/lib64/python3.10/site-packages/tests': {'content': '', 'create_dirs': False}
    }
)])
def test_python_tests_in_site_packages(package, pythoncheck):
    output, test = pythoncheck
    test.check(package)
    out = output.print_results(output.results)
    assert 'E: python-tests-in-site-packages /usr/lib/python2.7/site-packages/test' in out
    assert 'E: python-tests-in-site-packages /usr/lib/python2.7/site-packages/tests' in out
    assert 'E: python-tests-in-site-packages /usr/lib/python3.10/site-packages/test' in out
    assert 'E: python-tests-in-site-packages /usr/lib/python3.10/site-packages/tests' in out
    assert 'E: python-tests-in-site-packages /usr/lib64/python2.7/site-packages/test' in out
    assert 'E: python-tests-in-site-packages /usr/lib64/python2.7/site-packages/tests' in out
    assert 'E: python-tests-in-site-packages /usr/lib64/python3.10/site-packages/test' in out
    assert 'E: python-tests-in-site-packages /usr/lib64/python3.10/site-packages/tests' in out


@pytest.mark.parametrize('package', [
    'binary/python310-scikit-build-0.17.2',
    'binary/python310-jupyter-events-0.6.3',
])
def test_python_dependencies(tmp_path, package, pythoncheck):
    output, test = pythoncheck
    test.check(get_tested_package(package, tmp_path))
    out = output.print_results(output.results)
    assert 'W: python-missing-require' not in out
    assert 'W: python-leftover-require' not in out


@pytest.mark.parametrize('package', [get_tested_mock_package(
    files={
        '/usr/lib/python3.10/site-packages/flit-3.8.0.dist-info/METADATA': {
            'content': """
Requires-Dist: flit_core >=3.8.0
Requires-Dist: requests
Requires-Dist: docutils
Requires-Dist: tomli-w
Requires-Dist: sphinx ; extra == "doc"
""",
            'create_dirs': True
        },
    },
    real_files=True,
    header={
        'requires': [
            'python-flit_core',
            'python-requests',
            'python-tomli-w',
            'python310-docutils',
        ],
    },
)])
def test_python_dependencies_metadata(package, pythoncheck):
    output, test = pythoncheck
    test.check(package)
    out = output.print_results(output.results)
    assert 'W: python-missing-require' not in out
    assert 'W: python-leftover-require' not in out


@pytest.mark.parametrize('package', [get_tested_mock_package(
    files={
        '/usr/lib/python3.10/site-packages/icecream-2.1.3-py3.10.egg-info/requires.txt': {
            'content': """
asttokens>=2.0.1
colorama>=0.3.9
executing>=0.3.1
pygments>=2.2.0
""",
            'create_dirs': True
        },
    },
    real_files=True,
    header={
        'requires': [
            'asttokens>=2.0.1',
            'colorama>=0.3.9',
            'executing>=0.3.1',
            'pygments>=2.2.0',
        ],
    },
)])
def test_python_dependencies_requires(package, pythoncheck):
    output, test = pythoncheck
    test.check(package)
    out = output.print_results(output.results)
    assert 'W: python-missing-require' not in out
    assert 'W: python-leftover-require' not in out


@pytest.mark.parametrize('package', [get_tested_mock_package(
    files={
        '/usr/lib/python3.10/site-packages/jupyter_server_fileid-0.9.0.dist-info/METADATA': {
            'content': """
Requires-Python: >=3.7
Requires-Dist: jupyter-events>=0.5.0
Requires-Dist: jupyter-server<3,>=1.15
Requires-Dist: click; extra == 'cli'
Requires-Dist: jupyter-server[test]<3,>=1.15; extra == 'test'
Requires-Dist: pytest; extra == 'test'
Requires-Dist: pytest-cov; extra == 'test'
""",
            'create_dirs': True
        },
    },
    real_files=True,
    header={
        'requires': [
            'python-jupyter-events',
            'python-jupyter-server',
            'python-click',
            'python-jupyter-server',
            'python-pytest',
            'python-pytest-cov',
        ],
    },
)])
def test_python_dependencies_metadata2(package, pythoncheck):
    output, test = pythoncheck
    test.check(package)
    out = output.print_results(output.results)
    assert 'W: python-missing-require' not in out
    assert 'W: python-leftover-require' not in out


@pytest.mark.parametrize('package', [
    'binary/python3-icecream-missingdeps',
    'binary/python3-flit-missingdeps',
])
def test_python_dependencies_missing(tmp_path, package, pythoncheck):
    output, test = pythoncheck
    test.check(get_tested_package(package, tmp_path))
    out = output.print_results(output.results)
    assert 'W: python-missing-require' in out


@pytest.mark.parametrize('package', [
    'binary/python3-icecream-leftovers',
    'binary/python3-flit-leftovers',
])
def test_python_dependencies_leftover(tmp_path, package, pythoncheck):
    output, test = pythoncheck
    test.check(get_tested_package(package, tmp_path))
    out = output.print_results(output.results)
    assert 'W: python-leftover-require' in out
