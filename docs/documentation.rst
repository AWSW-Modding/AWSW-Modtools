Documentation
=============

Documenting the code, especially the API, is critical to ensure that the modding tools isn't abandoned.

Style Guide
-----------

All the Python code must follow `PEP 8`_. The docstrings must follow Napoleon, Google's docstring style. You can find more information in `Google's style guide`_ and `Sphinx documentation`_
Before merging into any major branch, ensure that pylint returns no problems.

To execute pylint under a Unix environment:

* Install normally through Python 2's pip
* Enter the game/ folder in the installation directory
* Run ``pylint modloader``

To run pylint for mods, run ``pylint mods/modname`` where modname is the mod's name.

.. _PEP 8: https://www.python.org/dev/peps/pep-0008/
.. _Google's style guide: https://google.github.io/styleguide/pyguide.html#Comments
.. _Sphinx documentation: http://www.sphinx-doc.org/en/stable/ext/napoleon.html

Building Documentation
----------------------

The documentation framework used is Sphinx. To build the documentation, switch the current branch to gh-pages and merge documentation into gh-pages.
After, execute ``sphinx-build . ..`` in the docs/ directory. This would cause all the documentation to be built.
The resulting files are now in the root project and can be viewed by Github pages.

*TODO: Make building documentation simpler*
