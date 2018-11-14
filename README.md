# DevToTests

## Description

This is a small framework of tests made with the idea to practice the automation concepts I've learned using Python instead of Java,
covering the very basics of automation and Page-Object-Model, using Selenium and Pytest among other dependencies.


## Requirements

To run these tests, you'll need:

An IDE: I use [PyCharm](https://www.jetbrains.com/pycharm/), but any Python-capable IDE should work.

[venv](https://docs.python.org/3/library/venv.html): This module provides support for creating lightweight “virtual environments” with their own site directories, optionally isolated from system site directories. Each virtual environment has its own Python binary (which matches the version of the binary that was used to create this environment) and can have its own independent set of installed Python packages in its site directories.

[pytest](https://docs.pytest.org/en/latest/contents.html): pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries. You can install it by using ``pip install -U pytest``.

[pytest-selenium](https://pytest-selenium.readthedocs.io/en/latest/user_guide.html): pytest-selenium is a plugin for pytest that provides support for running Selenium based tests. You can install it using ``pip intall pytest_selenium``.

[ChromeDriver](http://chromedriver.chromium.org/): If you are using the latest version of Chrome, you will need the latest ChromeDriver. There's a dependency called Chromedriver_binary which allows you to reference the Chromedriver path without much hassle, and it also installs the Chromedriver with it. You can install it using `` pip install chromedriver_binary``.

[Pytruth](https://github.com/google/pytruth): It's an assertion library translated from the Java implementation of Google Truth which allows you to make assertions in a fluent style. I recommend it. Unfortunately, as far as I know, there is not a pip package of this dependency, so you'll have to clone the repo and move it to the project folder.

## Running the tests

To run the tests, you'll have to activate the virtual environment running the ``activate.bat`` file, and then type in the terminal ``pytest --driver Chrome``
