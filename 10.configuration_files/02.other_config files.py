# 2. "conftest.py" File:
# This is a local config file in pytest, where we can write hook functions
# and fixtures, as mentioned before, you can add multiple conftest.py files
# in the test main folder and subfolders.

# 3. "tox.ini" File
# It is a configuration file of the tox project, similar to the pytest.ini
# file.

# 4. "pyproject.toml" File:
# It can be used to configure pytest settings as an alternative to pytest.ini,
# but the [tool.pytest.ini_options] section is used instead of [pytest] in
# pytest.ini file, as shown below:

# [tool.pytest.ini_options]
# minversion = "6.0"
# addopts = "-ra -q"
# testpaths = ["tests", "integration"]
# log_cli = true
# log_level = "INFO"

# 5. "setup.cfg" File:
# It is a general-purpose configuration file originally used for packaging
# but can hold pytest settings if a [tool:pytest] section is added.

# [tool:pytest]
# minversion = 6.0
# addopts = -ra -q
# testpaths =
#     tests
#     integration

# Using setup.cfg is not recommended unless it is used for simple cases.

# For more information about the Configuration in pytest, check:
# https://docs.pytest.org/en/7.1.x/reference/customize.html#configuration
