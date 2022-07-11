# cfdibills
[![PyPI Latest Release](https://img.shields.io/pypi/v/cfdibills.svg)](https://pypi.org/project/cfdibills/)
[![codecov](https://codecov.io/gh/peguerosdc/cfdibills/branch/main/graph/badge.svg?token=IE6CNFJJMQ)](https://codecov.io/gh/peguerosdc/cfdibills)

Utility to inspect and verify CFDI (Mexican invoice) versions 3.3 and 4.0

## Features

* Load a CFDI in XML format into a [pydantic](https://github.com/samuelcolvin/pydantic) object
* Query the status of a CFDI via SAT's web service
* Only presence of required fields is validated, but this package doesn't perform a thorough validation of the CFDI
standard.
* **DOESN'T REQUIRE** additional dependencies to read the XML like libxml2-dev, libxslt-dev


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

## Contributing

This repository uses [pre-commit](https://pre-commit.com/) to help developers perform almost the same validations as in
the CI pipeline but before having to wait for a Pull-Request. You can set it up using:

```sh
pip install -r requirements_dev.txt
pre-commit install
```

## License

Licensed under the [GNU LGPLv3 License](https://github.com/peguerosdc/cfdibilly/blob/master/LICENSE).
