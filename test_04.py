from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time
import win32gui
import win32con
import os
from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Reconciliation():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https:localhost/main/#/v5/waybillAnalyze/contrast")
        print("打开网页")

        #关闭弹窗
        # while True:
        #     self.driver.implicitly_wait(30)
        #     # if self.driver.find_element_by_class_name("ant-modal-close-x"):
        #     #     x_btn = self.driver.find_element_by_class_name("ant-modal-close-x")
        #     #     self.driver.execute_script("arguments[0].click();",x_btn)
        #     x_root = (By.CLASS_NAME, "ant-modal-root")
        #     # 二十秒内每五秒找一次
        #     if WebDriverWait(self.driver,20,0.5).until(EC.presence_of_element_located(x_root)):
        #         x_btn = self.driver.find_element_by_class_name("ant-modal-close-x")
        #         self.driver.execute_script("arguments[0].click();",x_btn)
        #         print("11111")
        #     else:
        #         self.driver.refresh()
        #         print("2222222222222")
        #         break





        self.path_flie = os.getcwd()


    def upload_excel(self):
        self.driver.implicitly_wait(20)
        upload_btn = self.driver.find_element_by_class_name("select_file")

        upload_btn.click()
        time.sleep(1)
        dialog = win32gui.FindWindow("#32770", u"打开")
        time.sleep(1)
        ComboBoxEx32 = win32gui.FindWindowEx(dialog, None, 'ComboBoxEx32', None)
        ComboBox = win32gui.FindWindowEx(ComboBoxEx32,None, "ComboBox",None)
        edit = win32gui.FindWindowEx(ComboBox, None, "Edit", None)
        button = win32gui.FindWindowEx(dialog, None, "Button", u"打开(&O)")
        time.sleep(1)


        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, self.path_flie+'\对账记录20211108.xls')
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
        time.sleep(5)

        up_btn = self.driver.find_element_by_class_name("upload_submit_btn")
        up_btn.click()



if __name__ == '__main__':
    a = Reconciliation()
    a.upload_excel()