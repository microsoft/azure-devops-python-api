Visual Studio Team Services API
=======================================================

This project provides access to Visual Studio Team Services APIs.

Contribute Code
===============

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

Packaging
=========

The released packages for this code can be found here https://pypi.python.org/pypi/vsts-python-api. 
Use the standard PYPI packaging flow to push a new release. Make sure to increment the version number appropriately.

*Example*
::
    python setup.py sdist
    python -m twine upload dist/*
::
