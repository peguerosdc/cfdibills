===============
Getting started
===============

Installation
------------

Run:

.. code-block:: bash

    pip install cfdibills


Usage
------------

You can load a verify a bill directly from its XML:

.. code-block:: python

    import cfdibills

    cfdi = cfdibills.read_xml("path/to/invoice.xml")
    status = cfdibills.verify(cfdi)


Or you can verify it manually:

.. code-block:: python

    import cfdibills

    cfdibills.verify(uuid="folio fiscal", rfc_emisor="re", rfc_receptor="rr", total_facturado=150.00)
