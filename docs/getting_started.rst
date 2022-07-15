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

    cfdi = cfdibills.read_xml("path/to/bill.xml")
    status = cfdibills.verify(cfdi)


Or you can verify it manually:

.. code-block:: python

    import cfdibills

    cfdibills.verify(uuid="folio fiscal", rfc_emisor="re", rfc_receptor="rr", total_facturado=150.00)

In both cases, `status`  would look something like this:

.. code-block:: python

    SATConsultaResponse(
        codigo_estatus='S - Comprobante obtenido satisfactoriamente.',
        es_cancelable='Cancelable con aceptación',
        estado='Vigente',
        estatus_cancelacion=None,
        validacion_efos='200',
    )
