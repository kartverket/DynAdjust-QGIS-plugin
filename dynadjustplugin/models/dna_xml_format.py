"""Serialize a DynaML document root."""

from copy import deepcopy
from typing import Sequence
from xml.etree import ElementTree


class DnaXmlFormat:
    """Represent and serialize the DnaXmlFormat XML element."""

    _VALID_TYPES = {"Measurement File", "Station File", "Combined File"}
    _VALID_CHILD_TAGS = {"DnaStation", "DnaMeasurement"}

    def __init__(
        self,
        file_type: str,
        children: Sequence[ElementTree.Element],
        reference_frame: str = "GDA2020",
        epoch: str = "01.01.2020",
    ) -> None:
        if file_type not in self._VALID_TYPES:
            raise ValueError("Invalid DnaXmlFormat type: {}".format(file_type))
        if not children:
            raise ValueError("DnaXmlFormat requires at least one child element")
        if any(child.tag not in self._VALID_CHILD_TAGS for child in children):
            raise ValueError(
                "DnaXmlFormat children must be DnaStation or DnaMeasurement elements"
            )

        self.file_type = file_type
        self.children = list(children)
        self.reference_frame = reference_frame
        self.epoch = epoch

    def to_element(self) -> ElementTree.Element:
        """Build the XML element tree for this document."""
        root = ElementTree.Element(
            "DnaXmlFormat",
            {
                "type": self.file_type,
                "referenceframe": self.reference_frame,
                "epoch": self.epoch,
            },
        )
        root.extend(deepcopy(child) for child in self.children)
        return root

    def to_xml(self) -> str:
        """Serialize this document as an XML string."""
        return ElementTree.tostring(self.to_element(), encoding="unicode")

