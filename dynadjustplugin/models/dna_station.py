"""Model and serialize a DynaML DnaStation element."""

from copy import deepcopy
from typing import Sequence
from xml.etree import ElementTree


class DnaStation:
    """Represent and serialize a DynaML DnaStation element."""

    _REQUIRED_TAGS = ("Name", "Constraints", "Type", "StationCoord")

    def __init__(self, children: Sequence[ElementTree.Element]) -> None:
        self.children = list(children)
        tags = tuple(child.tag for child in self.children)
        if tags not in (
            self._REQUIRED_TAGS,
            self._REQUIRED_TAGS + ("Description",),
        ):
            raise ValueError(
                "DnaStation must contain Name, Constraints, Type, StationCoord, "
                "and optionally Description in order"
            )

    def to_element(self) -> ElementTree.Element:
        """Build the XML element tree for this station."""
        root = ElementTree.Element("DnaStation")
        root.extend(deepcopy(child) for child in self.children)
        return root

    def to_xml(self) -> str:
        """Serialize this station as an XML string."""
        return ElementTree.tostring(self.to_element(), encoding="unicode")
