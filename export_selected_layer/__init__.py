from krita import Krita, DockWidgetFactory, DockWidgetFactoryBase
from .exportSelectedLayer import ExportSelectedLayer


# Initialize and add the extension
Scripter.addExtension(ExportSelectedLayer(Krita.instance()))
