import xml.etree.ElementTree as ET

from dynadjustplugin.models.dnaproj_parser import convert_dnaproj_to_xml


def test_convert_dnaproj_to_xml_preserves_settings_and_empty_values(tmp_path):
    project_file = tmp_path / "example.dnaproj"
    project_file.write_text(
        "# example project\n"
        "#general (35) VALUE\n"
        "------------------------------------------\n"
        "network-name                       etrs89\n"
        "input-folder                      C:\\\\data files\n"
        "geo-file\n"
        "#import (35) VALUE\n"
        "------------------------------------------\n"
        "reference-frame                   ETRS89-NOR\n",
        encoding="utf-8",
    )

    output_path = convert_dnaproj_to_xml(project_file)
    root = ET.parse(output_path).getroot()

    assert output_path.name == "example.project.xml"
    assert root.tag == "DnaProject"
    assert root.attrib["source"] == "example.dnaproj"
    settings = {
        setting.attrib["name"]: setting.text
        for setting in root.findall("./Section[@name='general']/Setting")
    }
    assert settings == {
        "network-name": "etrs89",
        "input-folder": "C:\\\\data files",
        "geo-file": None,
    }
    assert root.findtext("./Section[@name='import']/Setting[@name='reference-frame']") == (
        "ETRS89-NOR"
    )
