from pathlib import Path
from lxml import etree
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from ..models.dyna_ml import DnaXmlFormat

def validate_xml(xml_file):

    schema_path = Path('models/DynaML.xsd')
    schema = etree.XMLSchema(etree.parse(str(schema_path)))

    file_path = Path(xml_file)
    if file_path.is_file():
        schema.assertValid(etree.parse(str(file_path)))
        print('{}: valid'.format(file_path.name))
    else:
        print('{}: missing'.format(file_path.name))
        raise FileNotFoundError("XML input file not found: {}".format(file_path.name))

    validate_xml(file_path)
    print("Parsing XML file:", xml_file)

    parser = XmlParser()

    network = parser.parse(
        str(file_path),
        DnaXmlFormat
    )

    print("Parsed XML successfully:", network)

def parse_and_serialize(xml_file):
    file_path = Path(xml_file)
    if not file_path.is_file():
        raise FileNotFoundError("XML input file not found: {}".format(file_path))

    print("Parsing XML file:", xml_file)

    parser = XmlParser()

    network = parser.parse(
        str(file_path),
        DnaXmlFormat
    )

    serializer = XmlSerializer()

    xml = serializer.render(network)

    print(xml)

parse_and_serialize("C:\\Users\\himsve\\source\\repos\\DynAdjust\\sampleData\\etrs89.xml")

parse_and_serialize("C:\\Users\\himsve\\source\\repos\\DynAdjust\\sampleData\\etrs89.simult.adj.msr.xml")

parse_and_serialize("C:\\Users\\himsve\\source\\repos\\DynAdjust\\sampleData\\etrs89.simult.adj.stn.xml")
