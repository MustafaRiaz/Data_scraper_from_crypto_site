import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtCore import QThread, pyqtSignal
from GUI import Ui_MainWindow  # Import the generated UI class
from CloudflareBypasser import CloudflareBypasser
from DrissionPage import ChromiumPage, ChromiumOptions
import time
import re
import pandas as pd

class ScraperThread(QThread):
    scraping_started = pyqtSignal()
    error_occurred = pyqtSignal(str)
    scraping_finished = pyqtSignal()

    def __init__(self, link, save_directory, browser_path):
        super().__init__()
        self.link = link
        self.save_directory = save_directory
        self.browser_path = browser_path

    def run(self):
        try:
            options = ChromiumOptions()
            options.set_paths(browser_path=self.browser_path)

            arguments = [
                "--no-first-run",
                "--force-color-profile=srgb",
                "--metrics-recording-only",
                "--password-store=basic",
                "--use-mock-keychain",
                "--export-tagged-pdf",
                "--no-default-browser-check",
                "--disable-background-mode",
                "--enable-features=NetworkService,NetworkServiceInProcess,LoadCryptoTokenExtension,PermuteTLSExtensions",
                "--disable-features=FlashDeprecationWarning,EnablePasswordsAccountStorage",
                "--deny-permission-prompts",
                "--disable-gpu",
                "--accept-lang=en-US",
            ]

            for argument in arguments:
                options.set_argument(argument)

            driver = ChromiumPage(addr_or_opts=options)
            if self.link:
                driver.get(self.link)

            cf_bypasser = CloudflareBypasser(driver)
            cf_bypasser.bypass()

            time.sleep(5)

            try:
                element = driver("text=Top Traders")
                if element:
                    element.click()
                else:
                    self.error_occurred.emit("Element not found.")
                    return
            except Exception as e:
                self.error_occurred.emit(f"An error occurred: {e}")
                return

            links = []
            try:
                id = driver.eles('.chakra-link chakra-button custom-1hhf88o')
                bought = driver.eles('.custom-1o79wax')
                pnl = driver.eles('.custom-1e9y0rl')
                unRealized = driver.eles('.custom-1hd7h4r')
                balance = driver.eles('.custom-1cicvqe')

                boughtList = []
                UNREALIZEd = []
                boughts = []
                sold = []
                BALANCe = []
                for b in balance:
                    BALANCe.append(b.text)
                for u in unRealized:
                    UNREALIZEd.append(u.text)
                for b in bought:
                    boughtList.append(b.text)
                count = 0
                for b in boughtList:
                    if count % 2 == 0:
                        boughts.append(b)
                    else:
                        sold.append(b)
                    count = count + 1

                PNl = []
                for p in pnl:
                    PNl.append(p.text)

                pattern = re.compile(r"href='(https?://[^']+)'")

                for html_content in id:
                    html_content = str(html_content)
                    match = pattern.search(html_content)
                    if match:
                        links.append(match.group(1))
                makers = []
                for link in links:
                    required_text = link.split("/")[-1]
                    makers.append(required_text)
            except Exception as e:
                self.error_occurred.emit(f"An error occurred: {e}")
                return

            data = {
                'MAKER': makers,
                'BOUGHT': boughts,
                'SOLD': sold,
                'PNL': PNl,
                'UNREALIZED': UNREALIZEd,
                'BALANCE': BALANCe
            }

            columns = ['MAKER', 'BOUGHT', 'SOLD', 'PNL', 'UNREALIZED', 'BALANCE']
            df = pd.DataFrame(data, columns=columns)
            csv_file = os.path.join(self.save_directory, 'output_data.csv')

            df.to_csv(csv_file, index=False)
        except Exception as e:
            self.error_occurred.emit(f"Failed to start the browser: {e}")
        finally:
            self.scraping_finished.emit()

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.save_directory = ""

        # Please change the chrome address from here
        # Select the correct chrome address from your computer and then paste it here
        self.browser_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

        self.ui.pushButton_2.clicked.connect(self.start_scraper)
        self.ui.changeDirectoryButton.clicked.connect(self.select_directory)

    def start_scraper(self):
        link = self.ui.URLInput.text()
        if not link:
            self.show_message_box("Please enter the link")
        elif not self.save_directory:
            self.show_message_box("Please select a directory to save the file")
        elif not os.path.exists(self.browser_path):
            self.show_message_box("Please set the chrome address first")
            return
        else:
            self.ui.MessageLabel.setText("Please wait while scraping is in progress...")
            self.thread = ScraperThread(link, self.save_directory, self.browser_path)
            self.thread.scraping_started.connect(lambda: self.show_message_box("Scraping started."))
            self.thread.error_occurred.connect(self.show_message_box)
            self.thread.scraping_finished.connect(lambda: self.ui.MessageLabel.setText("Hurrah! Scraping is finished."))
            self.thread.start()

    def select_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        if directory:
            self.save_directory = directory
            self.ui.fileSaveLocation.setText(directory)

    def show_message_box(self, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Information")
        msg_box.setText(message)
        msg_box.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MyApp()
    mainWindow.show()
    sys.exit(app.exec_())
