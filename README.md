# cfdibills
[![PyPI Latest Release](https://img.shields.io/pypi/v/cfdibills.svg)](https://pypi.org/project/cfdibills/)

Utility to inspect and validate CFDI (Mexican invoice) versions 3.3 and 4.0

## Features

* Load a CFDI in XML format into a python object
* Gather the status of a CFDI from SAT
* **Doesn't require** additional dependencies to read XML like libxml2-dev, libxslt-dev

## Installation

Run:

```sh
pip install cfdibills
```

## Examples

You can load a verify a bill directly from its XML:

````python
import cfdibills

cfdi = cfdibills.read_xml("path/to/invoice.xml")
status = cfdibills.verify(cfdi)
````

Or you can verify it manually:

````python
import cfdibills

cfdibills.verify(uuid="folio fiscal", rfc_emisor="re", rfc_receptor="rr", total_facturado=150.00)
````

## License

Licensed under the [GNU LGPLv3 License](https://github.com/peguerosdc/cfdibilly/blob/master/LICENSE).