from PyQt5.QtDesigner import QPyDesignerCustomWidgetPlugin
from PyQt5.QtGui import QIcon
from simple_adjust import QSimpleAdjust

class QSimpleAdjustPlugin(QPyDesignerCustomWidgetPlugin):
  def __init__(self, parent = None):
    QPyDesignerCustomWidgetPlugin.__init__(self)
    self.initialized = False
  
  def initialize(self, core):
    if self.initialized:
      return
    self.initialized = True

  def isInitialized(self):
    return self.initialized

  def createWidget(self, parent):
    return QSimpleAdjust(parent)

  def name(self):
    return "QSimpleAdjust"

  def group(self):
    return "PyQt Custom Widgets"

  def toolTip(self):
    return ""

  def whatsThis(self):
    return ""

  def isContainer(self):
    return False
    
  def icon(self):
    return QIcon()

  def domXml(self):
    return (
               '<widget class="QSimpleAdjust" name=\"QSimpleAdjust\">\n'
               " <property name=\"toolTip\" >\n"
               "  <string></string>\n"
               " </property>\n"
               " <property name=\"whatsThis\" >\n"
               "  <string></string>\n"
               " </property>\n"
               "</widget>\n"
               )

  def includeFile(self):
    return "simple_adjust"