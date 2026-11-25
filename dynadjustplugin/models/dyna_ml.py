from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


@dataclass(kw_only=True)
class ClusterId:
    class Meta:
        name = "ClusterID"

    value: str = field(default="")


@dataclass(kw_only=True)
class Constraints:
    value: str = field(default="")


@dataclass(kw_only=True)
class Coords:
    value: str = field(default="")


@dataclass(kw_only=True)
class Description:
    value: str = field(default="")


class DnaXmlFormatType(Enum):
    MEASUREMENT_FILE = "Measurement File"
    STATION_FILE = "Station File"
    COMBINED_FILE = "Combined File"


@dataclass(kw_only=True)
class Epoch:
    value: str = field(default="")


@dataclass(kw_only=True)
class EpochOfObservation:
    value: str = field(default="")


@dataclass(kw_only=True)
class First:
    value: str = field(default="")


@dataclass(kw_only=True)
class Height:
    value: str = field(default="")


@dataclass(kw_only=True)
class HemisphereZone:
    value: str = field(default="")


@dataclass(kw_only=True)
class Hscale:
    value: str = field(default="")


@dataclass(kw_only=True)
class Ignore:
    value: str = field(default="")


@dataclass(kw_only=True)
class InstHeight:
    value: str = field(default="")


@dataclass(kw_only=True)
class Lscale:
    value: str = field(default="")


@dataclass(kw_only=True)
class MeasurementId:
    class Meta:
        name = "MeasurementID"

    value: str = field(default="")


@dataclass(kw_only=True)
class Name:
    value: str = field(default="")


@dataclass(kw_only=True)
class Pscale:
    value: str = field(default="")


@dataclass(kw_only=True)
class ReferenceFrame:
    value: str = field(default="")


@dataclass(kw_only=True)
class Second:
    value: str = field(default="")


@dataclass(kw_only=True)
class SigmaXx:
    class Meta:
        name = "SigmaXX"

    value: str = field(default="")


@dataclass(kw_only=True)
class SigmaXy:
    class Meta:
        name = "SigmaXY"

    value: str = field(default="")


@dataclass(kw_only=True)
class SigmaXz:
    class Meta:
        name = "SigmaXZ"

    value: str = field(default="")


@dataclass(kw_only=True)
class SigmaYy:
    class Meta:
        name = "SigmaYY"

    value: str = field(default="")


@dataclass(kw_only=True)
class SigmaYz:
    class Meta:
        name = "SigmaYZ"

    value: str = field(default="")


@dataclass(kw_only=True)
class SigmaZz:
    class Meta:
        name = "SigmaZZ"

    value: str = field(default="")


@dataclass(kw_only=True)
class Source:
    value: str = field(default="")


@dataclass(kw_only=True)
class StdDev:
    value: str = field(default="")


@dataclass(kw_only=True)
class TargHeight:
    value: str = field(default="")


@dataclass(kw_only=True)
class Target:
    value: str = field(default="")


@dataclass(kw_only=True)
class Third:
    value: str = field(default="")


@dataclass(kw_only=True)
class Total:
    value: str = field(default="")


@dataclass(kw_only=True)
class Type:
    value: str = field(default="")


@dataclass(kw_only=True)
class Value:
    value: str = field(default="")


@dataclass(kw_only=True)
class Vscale:
    value: str = field(default="")


@dataclass(kw_only=True)
class X:
    value: str = field(default="")


@dataclass(kw_only=True)
class Xaxis:
    class Meta:
        name = "XAxis"

    value: str = field(default="")


@dataclass(kw_only=True)
class Y:
    value: str = field(default="")


@dataclass(kw_only=True)
class Yaxis:
    class Meta:
        name = "YAxis"

    value: str = field(default="")


@dataclass(kw_only=True)
class Z:
    value: str = field(default="")


@dataclass(kw_only=True)
class M11:
    class Meta:
        name = "m11"

    value: str = field(default="")


@dataclass(kw_only=True)
class M12:
    class Meta:
        name = "m12"

    value: str = field(default="")


@dataclass(kw_only=True)
class M13:
    class Meta:
        name = "m13"

    value: str = field(default="")


@dataclass(kw_only=True)
class M21:
    class Meta:
        name = "m21"

    value: str = field(default="")


@dataclass(kw_only=True)
class M22:
    class Meta:
        name = "m22"

    value: str = field(default="")


@dataclass(kw_only=True)
class M23:
    class Meta:
        name = "m23"

    value: str = field(default="")


@dataclass(kw_only=True)
class M31:
    class Meta:
        name = "m31"

    value: str = field(default="")


@dataclass(kw_only=True)
class M32:
    class Meta:
        name = "m32"

    value: str = field(default="")


@dataclass(kw_only=True)
class M33:
    class Meta:
        name = "m33"

    value: str = field(default="")


@dataclass(kw_only=True)
class Directions:
    ignore: Ignore = field(
        metadata={
            "name": "Ignore",
            "type": "Element",
        }
    )
    target: Target = field(
        metadata={
            "name": "Target",
            "type": "Element",
        }
    )
    value: Value = field(
        metadata={
            "name": "Value",
            "type": "Element",
        }
    )
    std_dev: StdDev = field(
        metadata={
            "name": "StdDev",
            "type": "Element",
        }
    )
    measurement_id: None | MeasurementId = field(
        default=None,
        metadata={
            "name": "MeasurementID",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Gpscovariance:
    class Meta:
        name = "GPSCovariance"

    m11: M11 = field(
        metadata={
            "type": "Element",
        }
    )
    m12: M12 = field(
        metadata={
            "type": "Element",
        }
    )
    m13: M13 = field(
        metadata={
            "type": "Element",
        }
    )
    m21: M21 = field(
        metadata={
            "type": "Element",
        }
    )
    m22: M22 = field(
        metadata={
            "type": "Element",
        }
    )
    m23: M23 = field(
        metadata={
            "type": "Element",
        }
    )
    m31: M31 = field(
        metadata={
            "type": "Element",
        }
    )
    m32: M32 = field(
        metadata={
            "type": "Element",
        }
    )
    m33: M33 = field(
        metadata={
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class PointCovariance:
    m11: M11 = field(
        metadata={
            "type": "Element",
        }
    )
    m12: M12 = field(
        metadata={
            "type": "Element",
        }
    )
    m13: M13 = field(
        metadata={
            "type": "Element",
        }
    )
    m21: M21 = field(
        metadata={
            "type": "Element",
        }
    )
    m22: M22 = field(
        metadata={
            "type": "Element",
        }
    )
    m23: M23 = field(
        metadata={
            "type": "Element",
        }
    )
    m31: M31 = field(
        metadata={
            "type": "Element",
        }
    )
    m32: M32 = field(
        metadata={
            "type": "Element",
        }
    )
    m33: M33 = field(
        metadata={
            "type": "Element",
        }
    )


@dataclass(kw_only=True)
class StationCoord:
    name: Name = field(
        metadata={
            "name": "Name",
            "type": "Element",
        }
    )
    xaxis: Xaxis = field(
        metadata={
            "name": "XAxis",
            "type": "Element",
        }
    )
    yaxis: Yaxis = field(
        metadata={
            "name": "YAxis",
            "type": "Element",
        }
    )
    height: Height = field(
        metadata={
            "name": "Height",
            "type": "Element",
        }
    )
    hemisphere_zone: None | HemisphereZone = field(
        default=None,
        metadata={
            "name": "HemisphereZone",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Clusterpoint:
    x: X = field(
        metadata={
            "name": "X",
            "type": "Element",
        }
    )
    y: Y = field(
        metadata={
            "name": "Y",
            "type": "Element",
        }
    )
    z: Z = field(
        metadata={
            "name": "Z",
            "type": "Element",
        }
    )
    measurement_id: None | MeasurementId = field(
        default=None,
        metadata={
            "name": "MeasurementID",
            "type": "Element",
        },
    )
    sigma_xx: SigmaXx = field(
        metadata={
            "name": "SigmaXX",
            "type": "Element",
        }
    )
    sigma_xy: SigmaXy = field(
        metadata={
            "name": "SigmaXY",
            "type": "Element",
        }
    )
    sigma_xz: SigmaXz = field(
        metadata={
            "name": "SigmaXZ",
            "type": "Element",
        }
    )
    sigma_yy: SigmaYy = field(
        metadata={
            "name": "SigmaYY",
            "type": "Element",
        }
    )
    sigma_yz: SigmaYz = field(
        metadata={
            "name": "SigmaYZ",
            "type": "Element",
        }
    )
    sigma_zz: SigmaZz = field(
        metadata={
            "name": "SigmaZZ",
            "type": "Element",
        }
    )
    point_covariance: list[PointCovariance] = field(
        default_factory=list,
        metadata={
            "name": "PointCovariance",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class DnaStation:
    name: Name = field(
        metadata={
            "name": "Name",
            "type": "Element",
        }
    )
    constraints: Constraints = field(
        metadata={
            "name": "Constraints",
            "type": "Element",
        }
    )
    type_value: Type = field(
        metadata={
            "name": "Type",
            "type": "Element",
        }
    )
    station_coord: StationCoord = field(
        metadata={
            "name": "StationCoord",
            "type": "Element",
        }
    )
    description: None | Description = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class Gpsbaseline:
    class Meta:
        name = "GPSBaseline"

    x: X = field(
        metadata={
            "name": "X",
            "type": "Element",
        }
    )
    y: Y = field(
        metadata={
            "name": "Y",
            "type": "Element",
        }
    )
    z: Z = field(
        metadata={
            "name": "Z",
            "type": "Element",
        }
    )
    measurement_id: None | MeasurementId = field(
        default=None,
        metadata={
            "name": "MeasurementID",
            "type": "Element",
        },
    )
    sigma_xx: SigmaXx = field(
        metadata={
            "name": "SigmaXX",
            "type": "Element",
        }
    )
    sigma_xy: SigmaXy = field(
        metadata={
            "name": "SigmaXY",
            "type": "Element",
        }
    )
    sigma_xz: SigmaXz = field(
        metadata={
            "name": "SigmaXZ",
            "type": "Element",
        }
    )
    sigma_yy: SigmaYy = field(
        metadata={
            "name": "SigmaYY",
            "type": "Element",
        }
    )
    sigma_yz: SigmaYz = field(
        metadata={
            "name": "SigmaYZ",
            "type": "Element",
        }
    )
    sigma_zz: SigmaZz = field(
        metadata={
            "name": "SigmaZZ",
            "type": "Element",
        }
    )
    gpscovariance: list[Gpscovariance] = field(
        default_factory=list,
        metadata={
            "name": "GPSCovariance",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class DnaMeasurement:
    type_value: list[Type] = field(
        default_factory=list,
        metadata={
            "name": "Type",
            "type": "Element",
        },
    )
    ignore: list[Ignore] = field(
        default_factory=list,
        metadata={
            "name": "Ignore",
            "type": "Element",
        },
    )
    reference_frame: list[ReferenceFrame] = field(
        default_factory=list,
        metadata={
            "name": "ReferenceFrame",
            "type": "Element",
        },
    )
    epoch: list[Epoch] = field(
        default_factory=list,
        metadata={
            "name": "Epoch",
            "type": "Element",
        },
    )
    epoch_of_observation: list[EpochOfObservation] = field(
        default_factory=list,
        metadata={
            "name": "EpochOfObservation",
            "type": "Element",
        },
    )
    first: list[First] = field(
        default_factory=list,
        metadata={
            "name": "First",
            "type": "Element",
        },
    )
    second: list[Second] = field(
        default_factory=list,
        metadata={
            "name": "Second",
            "type": "Element",
        },
    )
    third: list[Third] = field(
        default_factory=list,
        metadata={
            "name": "Third",
            "type": "Element",
        },
    )
    value: list[Value] = field(
        default_factory=list,
        metadata={
            "name": "Value",
            "type": "Element",
        },
    )
    std_dev: list[StdDev] = field(
        default_factory=list,
        metadata={
            "name": "StdDev",
            "type": "Element",
        },
    )
    inst_height: list[InstHeight] = field(
        default_factory=list,
        metadata={
            "name": "InstHeight",
            "type": "Element",
        },
    )
    targ_height: list[TargHeight] = field(
        default_factory=list,
        metadata={
            "name": "TargHeight",
            "type": "Element",
        },
    )
    total: list[Total] = field(
        default_factory=list,
        metadata={
            "name": "Total",
            "type": "Element",
        },
    )
    directions: list[Directions] = field(
        default_factory=list,
        metadata={
            "name": "Directions",
            "type": "Element",
        },
    )
    vscale: list[Vscale] = field(
        default_factory=list,
        metadata={
            "name": "Vscale",
            "type": "Element",
        },
    )
    gpsbaseline: list[Gpsbaseline] = field(
        default_factory=list,
        metadata={
            "name": "GPSBaseline",
            "type": "Element",
        },
    )
    hscale: list[Hscale] = field(
        default_factory=list,
        metadata={
            "name": "Hscale",
            "type": "Element",
        },
    )
    lscale: list[Lscale] = field(
        default_factory=list,
        metadata={
            "name": "Lscale",
            "type": "Element",
        },
    )
    pscale: list[Pscale] = field(
        default_factory=list,
        metadata={
            "name": "Pscale",
            "type": "Element",
        },
    )
    clusterpoint: list[Clusterpoint] = field(
        default_factory=list,
        metadata={
            "name": "Clusterpoint",
            "type": "Element",
        },
    )
    coords: list[Coords] = field(
        default_factory=list,
        metadata={
            "name": "Coords",
            "type": "Element",
        },
    )
    source: list[Source] = field(
        default_factory=list,
        metadata={
            "name": "Source",
            "type": "Element",
        },
    )
    measurement_id: list[MeasurementId] = field(
        default_factory=list,
        metadata={
            "name": "MeasurementID",
            "type": "Element",
        },
    )
    cluster_id: list[ClusterId] = field(
        default_factory=list,
        metadata={
            "name": "ClusterID",
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
class DnaXmlFormat:
    dna_station: list[DnaStation] = field(
        default_factory=list,
        metadata={
            "name": "DnaStation",
            "type": "Element",
        },
    )
    dna_measurement: list[DnaMeasurement] = field(
        default_factory=list,
        metadata={
            "name": "DnaMeasurement",
            "type": "Element",
        },
    )
    type_value: DnaXmlFormatType = field(
        metadata={
            "name": "type",
            "type": "Attribute",
        }
    )
    referenceframe: str = field(
        default="GDA2020",
        metadata={
            "type": "Attribute",
        },
    )
    epoch: str = field(
        default="01.01.2020",
        metadata={
            "type": "Attribute",
        },
    )
