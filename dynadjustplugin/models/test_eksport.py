from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

if __package__:
    from .dyna_ml import DnaXmlFormat, DnaXmlFormatType, DnaMeasurement, Type
else:
    from dyna_ml import DnaXmlFormat, DnaXmlFormatType, DnaMeasurement, Type

network = DnaXmlFormat(
    type_value=DnaXmlFormatType.MEASUREMENT_FILE,
    dna_measurement=[DnaMeasurement(type_value=[Type(value='GPS')])],
    referenceframe="ETRS89-NOR",
    epoch="1989.0",
)
print(XmlSerializer().render(network))

print("ferdig")
