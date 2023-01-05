# Description


This is a tool for converting text from UTF-8 to Edgecase Markup Language (EML).




# Sample commands


```bash

python cli.py

python cli.py --help

python cli.py --task hello

python cli.py --task hello --log-level=info

python cli.py --task hello --log-level=debug

python cli.py --task hello2

python cli.py --task get_python_version

python cli.py --task convert --input-file cli_input/input.txt

```




Tests:

```bash

# Run all tests, including submodule tests.
pytest

# Run all tests, excluding submodule tests.
pytest --ignore=text_converter/submodules

# Run all tests in a specific test file
pytest text_converter/test/test_hello.py

# Run tests with relatively little output
pytest --quiet text_converter/test/test_hello.py

# Run a single test
pytest text_converter/test/test_hello.py::test_hello

# Print log output in real-time during a single test
pytest --capture=no --log-cli-level=INFO text_converter/test/test_hello.py::test_hello

# Note: The --capture=no option will also cause print statements within the test code to produce output.

```



Code style:


```bash

pycodestyle text_converter/code/hello.py

pycodestyle --filename=*.py

pycodestyle --filename=*.py --statistics

pycodestyle --filename=*.py --exclude text_converter/submodules

```

Settings for pycodestyle are stored in the file `tox.ini`.








# Environment


Successfully run under the following environments:

1:  
- Ubuntu 16.04 on WSL (Windows Subsystem for Linux) on Windows 10  
- Python 3.6.15
- pytest 6.1.2  

Recommendation: Use `pyenv` to install these specific versions of `python` and `pytest`.








# Installation


Install & configure `pyenv`.  

https://github.com/pyenv/pyenv-installer

https://github.com/pyenv/pyenv

Result: When you change into the `text_converter_python3` directory, the versions of `python` and `pip` change appropriately.


```
git clone git@github.com/sj-piano/text_converter_python3.git

cd text_converter_python3

pyenv install 3.6.15

pyenv local 3.6.15




