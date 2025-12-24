# 1. "pytest.ini" File:
# It allows you to define settings that customize how pytest runs your tests,
# so, you don’t have to specify them manually every time.
# The pytest.ini file takes precedence over other files, even when it is empty.

# What can you configure in pytest.ini?
# - Minimum pytest version (minversion)
# - Additional command-line options (addopts)
# As we did when we added the "--strict-markers" flag
# - Test paths (testpaths)
# - Custom markers for organizing tests
# - Logging settings

# pytest.ini example
# [pytest]
# minversion = 6.0
# addopts = --strict-markers --disable-warnings  ; adding different flags
#                                                ; options

# testpaths =           ; This tells pytest to look for tests in the tests and
#     tests             ; integration directories, instead of scanning the
#     integration       ; entire project.

# log_cli = true        ; Enables logging output in the console.
# log_level = INFO      ; Sets the logging level to INFO.

# ; Registering marks:
# markers =
#     slow: marks tests as slow
#     database: marks tests that interact with the database
