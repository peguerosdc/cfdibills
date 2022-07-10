import cfdibills

file = "./data/AAAD.19172.XML"

cfdi = cfdibills.read_xml(file)
status = cfdibills.verify(cfdi)

cfdibills.verify(
    uuid="A9C13105-714C-43BE-A9A8-65DE90A9014B",
    rfc_emisor="CCR201029739",
    rfc_receptor="SCO920618N7A",
    total_facturado=1427.00,
)
