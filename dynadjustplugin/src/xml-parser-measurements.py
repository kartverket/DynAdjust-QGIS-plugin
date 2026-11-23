from qgis.core import *
from PyQt6.QtCore import QVariant
import xml.etree.ElementTree as ET

xml_file = r"C:\Users\himsve\source\repos\DynAdjust\sampleData\etrs89.xml"

tree = ET.parse(xml_file)
root = tree.getroot()

stations = {}


for stn in root.findall(".//StationCoord"):
    name = stn.findtext("Name")
    east = float(stn.findtext("XAxis"))
    north = float(stn.findtext("YAxis"))

    stations[name] = (east, north)

# Measurement layer
line_layer = QgsVectorLayer(
    "LineString?crs=EPSG:10875",
    "Measurements",
    "memory"
)

provider = line_layer.dataProvider()

provider.addAttributes([
    QgsField("from_stn", QVariant.String),
    QgsField("to_stn", QVariant.String),
    QgsField("type", QVariant.String)
])

line_layer.updateFields()

features = []

for msr in root.findall(".//DnaMeasurement"):
    from_stn = msr.findtext("First")
    to_stn = msr.findtext("Second")
    msr_type = msr.findtext("Type")

    if from_stn not in stations or to_stn not in stations:
        continue

    x1, y1 = stations[from_stn]
    x2, y2 = stations[to_stn]

    feat = QgsFeature()

    feat.setGeometry(
        QgsGeometry.fromPolylineXY([
            QgsPointXY(x1, y1),
            QgsPointXY(x2, y2)
        ])
    )

    feat.setAttributes([
        from_stn,
        to_stn,
        msr_type
    ])

    features.append(feat)

provider.addFeatures(features)

QgsProject.instance().addMapLayer(line_layer)
