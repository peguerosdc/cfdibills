Welcome to cfdibills's documentation!
=====================================

Utility to inspect and validate CFDI (Mexican invoice) versions 3.3 and 4.0

**Features**

* Load a CFDI in XML format into a `pydantic <https://github.com/samuelcolvin/pydantic>`_ object
* Query the status of a CFDI via SAT's web service
* Only presence of required fields is validated, but this package doesn't perform a thorough validation of the CFDI standard.
* **DOESN'T REQUIRE** additional dependencies to read the XML like libxml2-dev, libxslt-dev


.. toctree::
   :caption: Contents:
   :maxdepth: 2

   getting_started
   api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
