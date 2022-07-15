Welcome to cfdibills's documentation!
=====================================

Utility to parse CFDI (Mexican invoice) versions 3.3 and 4.0 and validate their status against the SAT.

**Features**

* Load a CFDI in XML format into a `pydantic <https://github.com/samuelcolvin/pydantic>`_ object

  * CFDIs are validated against the XSD schema, but a thorough check (i.e. conditional values) is not performed.

* Query the status of a CFDI via SAT's web service
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
