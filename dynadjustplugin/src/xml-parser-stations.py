from qgis.core import *
from PyQt6.QtCore import QVariant
import xml.etree.ElementTree as ET

xml_file = r"C:\Users\himsve\source\repos\DynAdjust\sampleData\etrs89.xml"

tree = ET.parse(xml_file)
root = tree.getroot()

layer = QgsVectorLayer("Point?crs=EPSG:10875", "Stations", "memory")
provider = layer.dataProvider()

provider.addAttributes([
    QgsField("name", QVariant.String)
])

layer.updateFields()

features = []

for station in root.findall(".//StationCoord"):
    name = station.findtext("Name")
    
    east = float(station.findtext("XAxis"))
    north = float(station.findtext("YAxis"))

    feat = QgsFeature()
    feat.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(east, north)))
    feat.setAttributes([name])

    features.append(feat)

provider.addFeatures(features)

QgsProject.instance().addMapLayer(layer)

