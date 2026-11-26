from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

if __package__:
    from .dyna_ml import DnaXmlFormat
else:
    from dyna_ml import DnaXmlFormat

parser = XmlParser()

xml_file = "C:\\Users\\himsve\\source\\repos\\DynAdjust\\sampleData\\etrs89.xml"

print("Parsing XML file:", xml_file)

network = parser.parse(
    xml_file,
    DnaXmlFormat
)

print("hei")
