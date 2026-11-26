# DynAdjust-QGIS-plugin
QGIS plugin - Least squares adjustment software

## Importing the DynaML models

Install the checkout in editable mode from the repository root:

```shell
python -m pip install -e .
```

Then import the generated model classes from any Python project using that
environment:

```python
from dynadjustplugin.models import DnaMeasurement, DnaXmlFormat
```

Install the XML extra (`python -m pip install ".[xml]"`) to use xsdata's XML
parser and serializer.
