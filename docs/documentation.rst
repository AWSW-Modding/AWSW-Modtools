Documentation
=============

Documenting the code, especially the API, is critical to ensure that the modding tools isn't abandoned.

Style Guide
-----------

All the Python code must follow `PEP 8`_. The docstrings must follow `Google's style guide`_.

.. _PEP 8: https://www.python.org/dev/peps/pep-0008/
.. _Google's style guide: https://google.github.io/styleguide/pyguide.html#Comments

Building Documentation
----------------------

The documentation framework used is Sphinx. To build the documentation, switch the current branch to gh-pages.
After, execute ``sphinx-build . ..`` in the docs/ directory. This would cause all the documentation to be built.
The resulting files are now in the root project and can be viewed by Github pages.

*TODO: Make building documentation simpler*
