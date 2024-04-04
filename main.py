import sys, os
from PySide6 import QtWidgets
from PySide6.QtGui import QCloseEvent, QIcon
from PySide6.QtCore import QSize
from mainui import Ui_MainWindow
if sys.platform == "win32":
    import winshell
    from win32com.client import Dispatch

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.setFixedSize(QSize(393, 383))

        self.browsersavail = {}
        if sys.platform == "win32":
            self.shell = Dispatch('WScript.Shell')
            chromepath = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
            bravepath = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe'
            firefoxpath = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            edgepath = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
            self.ffprofile = f"{winshell.application_data()}\\Mozilla\\Firefox\\Profiles\\webapp-profile"
        elif sys.platform == "linux":
            chromepath = r'/usr/bin/google-chrome-stable'
            bravepath = r'/usr/bin/brave'
            firefoxpath = r'/usr/bin/firefox'
            edgepath = r'/usr/bin/microsoft-edge-stable'
            self.ffprofile = f"{os.environ['HOME']}/.mozilla/firefox/webapp-profile"

        if os.path.exists(chromepath):
            self.browsersavail["Chrome"] = chromepath
        if os.path.exists(bravepath):
            self.browsersavail["Brave"] = bravepath
        if os.path.exists(firefoxpath):
            self.browsersavail["Firefox"] = firefoxpath
            if not os.path.exists(self.ffprofile):
                os.mkdir(self.ffprofile)
                if sys.platform == "win32":
                    os.mkdir(f"{self.ffprofile}\\chrome")
                    with open(f"{self.ffprofile}\\user.js", "w") as file:
                        file.write(r'user_pref("toolkit.legacyUserProfileCustomizations.stylesheets", true);')
                    with open(f"{self.ffprofile}\\chrome\\userChrome.css", "w") as file:
                        file.write(r'#nav-bar, #tabbrowser-tabs {visibility: collapse !important;}')
                elif sys.platform == "linux":
                    os.mkdir(f"{self.ffprofile}/chrome")
                    with open(f"{self.ffprofile}/user.js", "w") as file:
                        file.write(r'user_pref("toolkit.legacyUserProfileCustomizations.stylesheets", true);')
                    with open(f"{self.ffprofile}/chrome/userChrome.css", "w") as file:
                        file.write(r'#nav-bar, #tabbrowser-tabs {visibility: collapse !important;}')
        if os.path.exists(edgepath):
            self.browsersavail["Edge"] = edgepath
        if len(self.browsersavail) == 0:
            self.displaydialog("Error", "No supported browsers available")
        
        self.browsernameip.addItems(self.browsersavail.keys())
        self.browsermodeip.addItems(["Normal", "Incognito"])
            
        self.chooseiconbtn.clicked.connect(self.geticon)
        self.createwa.clicked.connect(self.createwafunc)

    def displaydialog(self, title, text):
        box = QtWidgets.QMessageBox(self)
        box.setWindowTitle(title)
        box.setText(text)
        box.exec()

    def createwafunc(self):
        name = self.nameip.text()
        url = self.urlip.text()
        browser = self.browsernameip.currentText()
        mode = self.browsermodeip.currentText()
        icon = self.iconpathip.text()
        app = self.appmode.isChecked()
        if (name == "" or url == "" or icon == ""):
            self.displaydialog("Error", "Some or all entries are empty")
        else:
            if url.find("https") == -1 and url.find("http") == -1:
                url = f"https://{url}"
            if browser == "Chrome" or browser == "Brave" or browser == "Edge":
                if app:
                    cmd = f" --app={url}"
                else:
                    cmd = f" --new-window {url}"
                if mode == "Incognito":
                    if browser != "Edge":
                        cmd += " --incognito"
                    else:
                        cmd += " --inprivate"
            elif browser == "Firefox":
                cmd = " --new-window"
                if mode == "Incognito":
                    cmd = " --private-window"
                cmd += f" {url}"
                if app:
                    cmd += f" --profile {self.ffprofile}"
            if sys.platform == "win32":
                shortcut = self.shell.CreateShortcut(winshell.desktop() + "\\" + name + ".lnk")
                shortcut.Targetpath = self.browsersavail[browser]
                shortcut.Arguments = cmd
                shortcut.IconLocation = icon
                shortcut.save()
                self.clearinput()
            elif sys.platform == "linux":
                path = os.path.join(os.environ['HOME'], f".local/share/applications/{name}.desktop")
                execline = f"{self.browsersavail[browser]} {cmd}"
                with open(path, "w") as file:
                    file.write("[Desktop Entry]\n")
                    file.write("Type=Application\n")
                    file.write("Encoding=UTF-8\n")
                    file.write("Name=")
                    file.write(name + '\n')
                    file.write("Comment=A Web App\n")
                    file.write("Exec=")
                    file.write(execline + '\n')
                    file.write("Icon=")
                    file.write(icon + '\n')
                self.clearinput()

    def geticon(self):
        dialog = QtWidgets.QFileDialog(self)
        dialog.setFileMode(QtWidgets.QFileDialog.AnyFile)
        if sys.platform == "win32":
            dialog.setNameFilter("Files (*.ico)")
        else:
            dialog.setNameFilter("Files (*.png *.ico *.jpeg *.jpg)")
        dialog.setViewMode(QtWidgets.QFileDialog.List)
        icon = ""
        if dialog.exec():
            icon = dialog.selectedFiles()[0]
        if icon!="":
            self.iconpathip.setText(icon)
            self.chooseiconbtn.setIcon(QIcon(icon))
            self.chooseiconbtn.setIconSize(QSize(65,65))
            self.chooseiconbtn.setText("")

    def clearinput(self):
        self.nameip.clear()
        self.urlip.clear()
        self.iconpathip.clear()
        self.browsernameip.setCurrentIndex(0)
        self.browsermodeip.setCurrentIndex(0)
        self.chooseiconbtn.setIcon(QIcon())
        self.chooseiconbtn.setText("Select an icon")
        self.appmode.setChecked(False)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    window = MainWindow()
    window.show()
    app.exec()