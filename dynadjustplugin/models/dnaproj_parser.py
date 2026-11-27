"""Convert DynAdjust project settings files to XML."""

import argparse
import re
import xml.etree.ElementTree as ET
from pathlib import Path

_SECTION_HEADER = re.compile(r"^#([A-Za-z][A-Za-z0-9_-]*)\s+\(\d+\)")


def parse_dnaproj(project_file: str | Path) -> dict[str, dict[str, str]]:
    """Parse sections and key/value settings from a DynAdjust project file."""
    project_path = Path(project_file)
    if not project_path.is_file():
        raise FileNotFoundError("Project file not found: {}".format(project_path))

    sections: dict[str, dict[str, str]] = {}
    current_section = None

    with project_path.open(encoding="utf-8-sig") as source:
        for line_number, line in enumerate(source, start=1):
            stripped = line.strip()
            if not stripped:
                continue

            section_match = _SECTION_HEADER.match(stripped)
            if section_match:
                current_section = section_match.group(1)
                if current_section in sections:
                    raise ValueError(
                        "Duplicate section {!r} on line {}".format(
                            current_section, line_number
                        )
                    )
                sections[current_section] = {}
                continue

            if stripped.startswith("#") or re.fullmatch(r"[-\s]+", stripped):
                continue

            if current_section is None:
                raise ValueError(
                    "Setting found outside a section on line {}".format(line_number)
                )

            parts = stripped.split(None, 1)
            key = parts[0]
            value = parts[1] if len(parts) == 2 else ""
            if key in sections[current_section]:
                raise ValueError(
                    "Duplicate setting {!r} in section {!r} on line {}".format(
                        key, current_section, line_number
                    )
                )
            sections[current_section][key] = value

    if not sections:
        raise ValueError("No project sections found in {}".format(project_path))

    return sections


def convert_dnaproj_to_xml(
    project_file: str | Path, output_file: str | Path | None = None
) -> Path:
    """Write project settings as XML and return the output path."""
    project_path = Path(project_file)
    sections = parse_dnaproj(project_path)
    output_path = (
        Path(output_file)
        if output_file is not None
        else project_path.with_name("{}.project.xml".format(project_path.stem))
    )

    root = ET.Element("DnaProject", source=project_path.name)
    for section_name, settings in sections.items():
        section = ET.SubElement(root, "Section", name=section_name)
        for key, value in settings.items():
            setting = ET.SubElement(section, "Setting", name=key)
            setting.text = value or None

    tree = ET.ElementTree(root)
    ET.indent(tree, space="  ")
    tree.write(output_path, encoding="utf-8", xml_declaration=True)
    return output_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert a DynAdjust .dnaproj settings file to XML."
    )
    parser.add_argument("project_file", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    args = parser.parse_args()

    output_path = convert_dnaproj_to_xml(args.project_file, args.output)
    print("Wrote {}".format(output_path))


if __name__ == "__main__":
    main()
