# pycfdi
Utility to inspect and validate CFDI (Mexican invoice) versions 3.3 and 4.0

## Features

* Check if an XML file is a valid CFDI
* Load a CFDI into a dictionary for manipulation
* Verify with SAT if a CFDI is valid

## Examples

You can load a verify an invoice directly from its XML:

````python
import pycfdi

file = "invoice.xml"
if pycfdi.is_cfdi(file):
    cfdi = pycfdi.read_xml(file)
    status = pycfdi.verify(cfdi)
````

Or you can verify an invoice manually:

````python
import pycfdi

pycfdi.verify(uuid="folio fiscal", rfc_emisor="re", rfc_receptor="rr", total_facturado=150.00)
````

## License

Licensed under the [GNU LGPLv3 License](https://github.com/peguerosdc/pycfdi/blob/master/LICENSE).