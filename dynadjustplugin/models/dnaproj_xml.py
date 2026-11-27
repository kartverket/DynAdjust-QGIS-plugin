"""XML-serializable models for DynAdjust project-settings XML."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class DnaProjectSetting:
    class Meta:
        name = "Setting"

    name: str = field(metadata={"type": "Attribute"})
    value: str | None = field(default=None, metadata={"type": "Text"})


@dataclass(kw_only=True)
class DnaProjectSection:
    class Meta:
        name = "Section"

    name: str = field(metadata={"type": "Attribute"})
    setting: list[DnaProjectSetting] = field(
        default_factory=list,
        metadata={
            "name": "Setting",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class DnaProject:
    source: str = field(metadata={"type": "Attribute"})
    section: list[DnaProjectSection] = field(
        default_factory=list,
        metadata={
            "name": "Section",
            "type": "Element",
        },
    )
