"""Model and serialize a DynaML PointCovariance element."""

from copy import deepcopy
from typing import Sequence
from xml.etree import ElementTree


class PointCovariance:
    """Represent and serialize a DynaML PointCovariance element."""

    _MATRIX_TAGS = (
        "m11",
        "m12",
        "m13",
        "m21",
        "m22",
        "m23",
        "m31",
        "m32",
        "m33",
    )

    def __init__(self, children: Sequence[ElementTree.Element]) -> None:
        self.children = list(children)
        if tuple(child.tag for child in self.children) != self._MATRIX_TAGS:
            raise ValueError(
                "PointCovariance must contain m11 through m33 in row-major order"
            )

    def to_element(self) -> ElementTree.Element:
        """Build the XML element tree for this covariance matrix."""
        root = ElementTree.Element("PointCovariance")
        root.extend(deepcopy(child) for child in self.children)
        return root

    def to_xml(self) -> str:
        """Serialize this covariance matrix as an XML string."""
        return ElementTree.tostring(self.to_element(), encoding="unicode")
