"""Model and serialize a DynaML DnaMeasurement element."""

from copy import deepcopy
from typing import Sequence
from xml.etree import ElementTree


class DnaMeasurement:
    """Represent and serialize a DynaML DnaMeasurement element."""

    _CHILD_TAGS = {
        "Type",
        "Ignore",
        "ReferenceFrame",
        "Epoch",
        "EpochOfObservation",
        "First",
        "Second",
        "Third",
        "Value",
        "StdDev",
        "InstHeight",
        "TargHeight",
        "Total",
        "Directions",
        "Vscale",
        "GPSBaseline",
        "Hscale",
        "Lscale",
        "Pscale",
        "Clusterpoint",
        "Coords",
        "Source",
        "MeasurementID",
        "ClusterID",
    }

    def __init__(self, children: Sequence[ElementTree.Element]) -> None:
        self.children = list(children)
        if not self.children:
            raise ValueError("DnaMeasurement requires at least one child element")
        if any(child.tag not in self._CHILD_TAGS for child in self.children):
            raise ValueError(
                "DnaMeasurement contains an element not allowed by the DynaML schema"
            )

    def to_element(self) -> ElementTree.Element:
        """Build the XML element tree for this measurement."""
        root = ElementTree.Element("DnaMeasurement")
        root.extend(deepcopy(child) for child in self.children)
        return root

    def to_xml(self) -> str:
        """Serialize this measurement as an XML string."""
        return ElementTree.tostring(self.to_element(), encoding="unicode")
