# cfdibills
[![PyPI Latest Release](https://img.shields.io/pypi/v/cfdibills.svg)](https://pypi.org/project/cfdibills/)
[![codecov](https://codecov.io/gh/peguerosdc/cfdibills/branch/main/graph/badge.svg?token=IE6CNFJJMQ)](https://codecov.io/gh/peguerosdc/cfdibills)

Utility to parse CFDI (Mexican invoice) versions 3.3 and 4.0 and validate their status against the SAT.

## Features

* Load a CFDI in XML format into a [pydantic](https://github.com/samuelcolvin/pydantic) object
  * CFDIs are validated against the XSD schema, but a thorough check (i.e. conditional values) is not performed.
* Query the status of a CFDI via SAT's web service
* **DOESN'T REQUIRE** additional dependencies to read the XML like libxml2-dev, libxslt-dev


## Installation

Run:

```sh
pip install cfdibills
```

## Examples

You can load and verify a bill directly from its XML:

````python
import cfdibills

cfdi = cfdibills.read_xml("path/to/bill.xml")
status = cfdibills.verify(cfdi)
````

Or you can verify it manually:

````python
import cfdibills

status = cfdibills.verify(uuid="folio fiscal", rfc_emisor="re", rfc_receptor="rr", total_facturado=150.00)
````

In both cases, `status`  would look something like this:

````python
SATConsultaResponse(
    codigo_estatus='S - Comprobante obtenido satisfactoriamente.',
    es_cancelable='Cancelable con aceptación',
    estado='Vigente',
    estatus_cancelacion=None,
    validacion_efos='200',
)
````


## Contributing

This repository uses [pre-commit](https://pre-commit.com/) to help developers perform almost the same validations as in
the CI pipeline but before having to wait for a Pull-Request. You can set it up using:

```sh
pip install -r requirements_dev.txt
pre-commit install
```

## License

Licensed under the [GNU LGPLv3 License](https://github.com/peguerosdc/cfdibilly/blob/master/LICENSE).
