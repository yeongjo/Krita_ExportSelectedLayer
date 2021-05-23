from PyQt5.QtWidgets import QWidget, QLabel, QMessageBox
from krita import Extension, DockWidget

directoryTextField = "H:\Pictures\Drawing\KraExportedLayers"

def mkdir(directory):
    target_directory = directory
    if (os.path.exists(target_directory)
            and os.path.isdir(target_directory)):
        return

    try:
        os.makedirs(target_directory)
    except OSError as e:
        raise e

#for action in Krita.instance().actions():
#    print(action.objectName() + " - " + action.text())

#Krita.instance().action("resizeimagetolayer").trigger()



def execute():
    documentName = Krita.instance().activeDocument().fileName()
    documentName = documentName if documentName else 'Untitled'
    fileName, extension = os.path.splitext(os.path.basename(documentName))


    # 파일의 폴더만들기
    newDir = os.path.join(directoryTextField, fileName)
    print("create folder: ", newDir)
    mkdir(newDir)

    layerName = Krita.instance().activeDocument().activeNode().name()
    layerFileName = '{0}/{1}.png'.format(newDir, layerName)

    bounds = QRect()

    print(layerFileName)
    width = Krita.instance().activeDocument().width()
    height = Krita.instance().activeDocument().height()
    Krita.instance().activeDocument().activeNode().save(
        layerFileName, width/72., height/72., krita.InfoObject(), bounds)

    QMessageBox.information(
        QWidget(),
        i18n("saved!"),
        i18n("save in %s") % layerFileName)

class ExportSelectedLayer(Extension):
    def __init__(self, parent):
        """
        Standard Krita Python extension constructor.
        Most of the initialization happens in :func:`setup`

        :param parent: Parent widget
        :type parent: :class:`QWidget` or None
        """
        super(HelloExtension, self).__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        """
        This is where most of the setup takes place!
        """
        action = window.createAction("export_selected_layer", i18n("Export Selected Layer"))
        action.triggered.connect(execute)