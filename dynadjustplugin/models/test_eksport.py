from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

if __package__:
    from .dyna_ml import DnaXmlFormat, DnaXmlFormatType, DnaMeasurement, Type
else:
    from dyna_ml import DnaXmlFormat, DnaXmlFormatType, DnaMeasurement, Type

parser = XmlParser()

xml_file = "C:\\Users\\himsve\\source\\repos\\DynAdjust\\sampleData\\etrs89.xml"

print("Parsing XML file:", xml_file)

network = parser.parse(
    xml_file,
    DnaXmlFormat
)

serializer = XmlSerializer()

xml = serializer.render(network)

print(xml)

network = DnaXmlFormat(
    type_value=DnaXmlFormatType.MEASUREMENT_FILE,
    dna_measurement=[DnaMeasurement(type_value=[Type(value='GPS')])],
)
print(XmlSerializer().render(network))

print("ferdig")
