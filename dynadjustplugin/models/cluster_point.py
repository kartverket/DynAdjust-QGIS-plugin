"""Serialize a DynaML document root."""
from copy import deepcopy
from typing import Sequence
from xml.etree import ElementTree

class Clusterpoint:
    """Represent and serialize a DynaML Clusterpoint element."""

    _SIGMA_TAGS = (
        "SigmaXX",
        "SigmaXY",
        "SigmaXZ",
        "SigmaYY",
        "SigmaYZ",
        "SigmaZZ",
    )

    def __init__(self, children: Sequence[ElementTree.Element]) -> None:
        self.children = list(children)
        tags = [child.tag for child in self.children]

        if tags[:3] != ["X", "Y", "Z"]:
            raise ValueError("Clusterpoint must begin with X, Y, and Z elements")

        sigma_start = 3
        if len(tags) > sigma_start and tags[sigma_start] == "MeasurementID":
            sigma_start += 1
        sigma_end = sigma_start + len(self._SIGMA_TAGS)
        if tuple(tags[sigma_start:sigma_end]) != self._SIGMA_TAGS:
            raise ValueError("Clusterpoint must contain all six Sigma elements in order")
        if any(tag != "PointCovariance" for tag in tags[sigma_end:]):
            raise ValueError(
                "Clusterpoint may only contain PointCovariance elements after SigmaZZ"
            )

    def to_element(self) -> ElementTree.Element:
        """Build the XML element tree for this cluster point."""
        root = ElementTree.Element("Clusterpoint")
        root.extend(deepcopy(child) for child in self.children)
        return root

    def to_xml(self) -> str:
        """Serialize this cluster point as an XML string."""
        return ElementTree.tostring(self.to_element(), encoding="unicode")
