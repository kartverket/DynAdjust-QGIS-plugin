"""Model and serialize a DynaML Directions element."""

from copy import deepcopy
from typing import Sequence
from xml.etree import ElementTree


class Directions:
    """Represent and serialize a DynaML Directions element."""

    _REQUIRED_TAGS = ("Ignore", "Target", "Value", "StdDev")

    def __init__(self, children: Sequence[ElementTree.Element]) -> None:
        self.children = list(children)
        tags = tuple(child.tag for child in self.children)
        if tags not in (
            self._REQUIRED_TAGS,
            self._REQUIRED_TAGS + ("MeasurementID",),
        ):
            raise ValueError(
                "Directions must contain Ignore, Target, Value, StdDev, "
                "and optionally MeasurementID in order"
            )

    def to_element(self) -> ElementTree.Element:
        """Build the XML element tree for these directions."""
        root = ElementTree.Element("Directions")
        root.extend(deepcopy(child) for child in self.children)
        return root

    def to_xml(self) -> str:
        """Serialize these directions as an XML string."""
        return ElementTree.tostring(self.to_element(), encoding="unicode")
