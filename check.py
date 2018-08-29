import sys
from PyQt4 import QtCore, QtGui, uic
import requests
import re
from lxml import etree

qtCreatorFile = "GP_Online_Check.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.check_button.clicked.connect(self.check)

    def check(self):
        pkg = self.input_box.toPlainText()
        headers = {
            'Referer': 'https://play.google.com/store/apps',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, '
                          'like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
        }

        pkg_list = re.findall(r"[a-zA-Z0-9._]+", pkg)
        online_list = []

        for p in pkg_list:
            print('Checking %s' % p)
            response = requests.get('https://play.google.com/store/apps/details?id=' + p, headers=headers)
            html = etree.HTML(response.text)
            title = html.xpath('//head/title/text()')
            if title[0] == 'Not Found':
                pass
            else:
                online_list.append(p)

        online_list_str = '\r\n'.join(online_list)
        self.result_box.setText(online_list_str)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
