from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer

from ..models.dyna_ml import DnaXmlFormat, DnaXmlFormatType, DnaMeasurement, Type, DnaMeasurement, Gpsbaseline
 
observation = DnaXmlFormat(
    type_value=DnaXmlFormatType.MEASUREMENT_FILE,
    dna_measurement=[
        DnaMeasurement(
            type_value=[Type(value='GPS')],
            first='211300470',
            second='211300940',
            gpsbaseline=Gpsbaseline(
                x=-4675.9386,
                y=-1693.9255,
                z=2657.0815,
                sigma_xx=1.7012598619000e-05,
                sigma_xy=-1.0467927495000e-05,
                sigma_xz=1.4195195035000e-05,
                sigma_yy=9.4335882750000e-06,
                sigma_yz=-1.0196034054000e-05,
                sigma_zz=1.4284143617000e-05
            )
        ),
    ],
    referenceframe="ETRS89-NOR",
    epoch="1989.0",
    )

print(XmlSerializer().render(observation))

print("ferdig")
