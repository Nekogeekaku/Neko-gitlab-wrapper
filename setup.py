from setuptools import setup, find_packages

setup(
    name='nekogitlabwrapper',
    version='0.1',
    description='A simple Python library to facilitate gitlab request.',
    author='Thierry CARRICABURU',
    packages=find_packages(include=['nekogitlabwrapper']),
    install_requires=['requests'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)