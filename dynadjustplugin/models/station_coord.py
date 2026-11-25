"""Model and serialize a DynaML StationCoord element."""

from copy import deepcopy
from typing import Sequence
from xml.etree import ElementTree


class StationCoord:
    """Represent and serialize a DynaML StationCoord element."""

    _REQUIRED_TAGS = ("Name", "XAxis", "YAxis", "Height")

    def __init__(self, children: Sequence[ElementTree.Element]) -> None:
        self.children = list(children)
        tags = tuple(child.tag for child in self.children)
        if tags not in (
            self._REQUIRED_TAGS,
            self._REQUIRED_TAGS + ("HemisphereZone",),
        ):
            raise ValueError(
                "StationCoord must contain Name, XAxis, YAxis, Height, "
                "and optionally HemisphereZone in order"
            )

    def to_element(self) -> ElementTree.Element:
        """Build the XML element tree for this station coordinate."""
        root = ElementTree.Element("StationCoord")
        root.extend(deepcopy(child) for child in self.children)
        return root

    def to_xml(self) -> str:
        """Serialize this station coordinate as an XML string."""
        return ElementTree.tostring(self.to_element(), encoding="unicode")
