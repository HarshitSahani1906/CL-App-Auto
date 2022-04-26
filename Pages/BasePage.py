import logging

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Utilities import configReader
from Utilities.generatingLogs import Logging

log = Logging(__name__, logging.INFO)


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        # print("1"+str(self.driver))
        # print("2"+str(self.wait))

    def click(self, locator, key):
        # self.driver.wait(6)
        if str(key).startswith("Xpath_"):

            # print("locator and xpath is :"+str(configReader.readConfig(locator, key)))

            log.logger.info("Clicking on element :" + str(key))
            try:
                self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, configReader.readConfig(locator, key))))
            except TimeoutException as e:
                log.logger.exception("Either Element is not clickable or it is not Loaded " + str(e))
                assert False, "Either Element is not clickable or it is not Loaded" + str(e)
            try:
                self.driver.find_element(AppiumBy.XPATH, configReader.readConfig(locator, key)).click()
            except Exception as e:
                log.logger.exception("click didn't occur" + str(e))
                assert False, "click didn't occur" + str(e)
        elif str(key).startswith("AccessID_"):
            log.logger.info("Clicking on element :" + str(key))
            try:
                self.wait.until(
                    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, configReader.readConfig(locator, key))))

            except TimeoutException as e:
                log.logger.exception("Either Element is not clickable or it is not Loaded :" + str(e))
                assert False, "Either Element is not clickable or it is not Loaded :"+ str(e)

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig(locator, key)).click()
            except Exception as e:
                log.logger.exception("click didn't occur" + str(e))
                assert False, "click didn't occur"+ str(e)

        elif str(key).startswith("ID_"):
            log.logger.info("Clicking on element :" + str(key))
            try:
                self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, configReader.readConfig(locator, key))))
            except TimeoutException as e:
                log.logger.exception("Either Element is not clickable or it is not Loaded " + str(e))
                assert False, "Either Element is not clickable or it is not Loaded "+ str(e)

            try:
                self.driver.find_element(AppiumBy.ID, configReader.readConfig(locator, key)).click()
            except Exception as e:
                log.logger.exception("click didn't occur" + str(e))
                assert False, "click didn't occur :"+ str(e)

        log.logger.info("Clicked on above element :")

    def clickIndex(self, locator, key, index):
        if str(key).startswith("XPath_"):
            log.logger.info("Clicking on element :" + str(key) + " with index value:" + str(index))
            try:
                self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, configReader.readConfig(locator, key))))
            except TimeoutException as e:
                log.logger.exception("Either Element is not clickable or it is not Loaded " + str(e))
                assert False, "Either Element is not clickable or it is not Loaded :"+ str(e)
            try:
                self.driver.find_elements(AppiumBy.XPATH, configReader.readConfig(locator, key))[index].click()
            except Exception as e:
                log.logger.exception("click didn't occur"  + str(e))
                assert False, "click didn't occur : "+ str(e)

        elif str(key).startswith("AccessID_"):
            log.logger.info("Clicking on element :" + str(key) + " with index value:" + str(index))
            try:
                self.wait.until(
                    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, configReader.readConfig(locator, key))))

            except TimeoutException as e:
                log.logger.exception("Either Element is not clickable or it is not Loaded " + str(e))
                assert False, "Either Element is not clickable or it is not Loaded"+ str(e)

            try:
                self.driver.find_elements(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig(locator, key))[
                    index].click()
            except Exception as e:
                log.logger.exception("click didn't occur" + str(e))
                assert False, "click didn't occur : " + str(e)

        elif str(key).startswith("ID_"):
            log.logger.info("Clicking on element :" + str(key) + " with index value:" + str(index))
            try:
                self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, configReader.readConfig(locator, key))))
            except TimeoutException as e:
                log.logger.exception("Either Element is not clickable or it is not Loaded " + str(e))
                assert False, "Either Element is not clickable or it is not Loaded " + str(e)

            try:
                self.driver.find_elements(AppiumBy.ID, configReader.readConfig(locator, key))[index].click()
            except Exception as e:
                log.logger.exception("click didn't occur" + str(e))
                assert False, "click didn't occur : " + str(e)

        log.logger.info("Clicked on above element :")

    def type(self, locator, key, value):
        if str(key).startswith("Xpath_"):
            log.logger.info("Typing  int  element :" + str(key) + " Entering value :" + str(value))
            try:
                self.wait.until(EC.element_to_be_clickable((AppiumBy.XPATH, configReader.readConfig(locator, key))))

            except TimeoutException as e:
                log.logger.exception("Either Element is not clickable or it is not Loaded " + str(e))
                assert False, "Either Element is not clickable or it is not Loaded "+ str(e)

            try:
                self.driver.find_element(AppiumBy.XPATH, configReader.readConfig(locator, key)).send_keys(value)
            except Exception as e:
                log.logger.exception("Not able to send Value : "+ str(e))
                assert False, "Not able to send Value : " + str(e)

        elif str(key).startswith("AcessID_"):
            log.logger.info("Typing  int  element :" + str(key) + " Entering value :" + str(value))
            try:
                self.wait.until(
                    EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, configReader.readConfig(locator, key))))
            except TimeoutException as e:
                log.logger.exception("Either Element is not clickable or it is not Loaded " + str(e))
                assert False, "Either Element is not clickable or it is not Loaded "+ str(e)

            try:
                self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig(locator, key)).send_keys(
                    value)
            except Exception as e:
                log.logger.exception("Not able to send Value : " + str(e))
                assert False, "Not able to send Value : "+ str(e)

        elif str(key).startswith("ID_"):
            log.logger.info("Typing  int  element :" + str(key) + " Entering value :" + str(value))
            try:
                self.wait.until(EC.element_to_be_clickable((AppiumBy.ID, configReader.readConfig(locator, key))))
            except TimeoutException as e:
                log.logger.exception("Either Element is not clickable or it is not Loaded " + str(e))
                assert False, "Either Element is not clickable or it is not Loaded "+ str(e)

            try:
                self.driver.find_element(AppiumBy.ID, configReader.readConfig(locator, key)).send_keys(value)
            except Exception as e:
                log.logger.exception("Not able to send Value : " + str(e))
                assert False, "Not able to send Value : " + str(e)
        log.logger.info("Typed on above element")

    def text(self, locator, key):
        if str(key).startswith("Xpath_"):
            log.logger.info("Getting  text of element :" + str(key))
            try:
                self.wait.until(
                    EC.visibility_of_element_located((AppiumBy.XPATH, configReader.readConfig(locator, key))))
            except TimeoutException as e:
                log.logger.exception("Either Element is not clickable or it is not Loaded " + str(e))
                assert False, "Either Element is not clickable or it is not Loaded "+ str(e)

            try:
                text = self.driver.find_element(AppiumBy.XPATH, configReader.readConfig(locator, key)).text
            except Exception as e:
                log.logger.exception("Not able to get Value : " + str(e))
                assert False, "Not able to get Value : " + str(e)

        elif str(key).startswith("AccessID_"):
            log.logger.info("Getting  text of element :" + str(key))
            try:
                self.wait.until(EC.visibility_of_element_located(
                    (AppiumBy.ACCESSIBILITY_ID, configReader.readConfig(locator, key))))
            except TimeoutException as e:
                log.logger.exception("Either Element is not clickable or it is not Loaded " + str(e))
                assert False, "Either Element is not clickable or it is not Loaded "+ str(e)

            try:
                text = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig(locator, key)).text
            except Exception as e:
                log.logger.exception("Not able to get Value : " + str(e))
                assert False, "Not able to get Value : " + str(e)

        elif str(key).startswith("ID_"):
            log.logger.info("Getting  text of element :" + str(key))
            try:
                self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, configReader.readConfig(locator, key))))
            except TimeoutException as e:
                log.logger.exception("Either Element is not clickable or it is not Loaded " + str(e))
                assert False, "Either Element is not clickable or it is not Loaded "+ str(e)

            try:
                text = self.driver.find_element(AppiumBy.ID, configReader.readConfig(locator, key)).text
            except Exception as e:
                log.logger.exception("Not able to get Value : " + str(e))
                assert False, "Not able to get Value : " + str(e)


        else:
            log.logger.info("Getting  text of element :" + str(key))


        return text

    def clear(self, locator, key):
        if str(key).startswith("Xpath_"):
            log.logger.info("Getting  text of element :" + str(key))
            self.wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, configReader.readConfig(locator, key))))
            clear = self.driver.find_element(AppiumBy.XPATH, configReader.readConfig(locator, key)).clear()
        elif str(key).startswith("AccessID_"):
            log.logger.info("Getting  text of element :" + str(key))
            self.wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, configReader.readConfig(locator, key))))
            clear = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig(locator, key)).clear()
        elif str(key).startswith("ID_"):
            log.logger.info("Getting  text of element :" + str(key))
            self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, configReader.readConfig(locator, key))))
            clear = self.driver.find_element(AppiumBy.ID, configReader.readConfig(locator, key)).clear()
        else:
            log.logger.info("Getting  text of element :" + str(key))

        return clear

    def is_enable(self, locator, key):
        if str(key).startswith("Xpath_"):
            log.logger.info("Getting  text of element :" + str(key))
            self.wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, configReader.readConfig(locator, key))))
            isEnable = self.driver.find_element(AppiumBy.XPATH, configReader.readConfig(locator, key)).getAttribute("enabled")
        elif str(key).startswith("AccessID_"):
            log.logger.info("Getting  text of element :" + str(key))
            self.wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, configReader.readConfig(locator, key))))
            isEnable = self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, configReader.readConfig(locator, key)).getAttribute("enabled")
        elif str(key).startswith("ID_"):
            log.logger.info("Getting  text of element :" + str(key))
            self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, configReader.readConfig(locator, key))))
            isEnable = self.driver.find_element(AppiumBy.ID, configReader.readConfig(locator, key)).getAttribute("enabled")
        else:
            log.logger.info("Getting  text of element :" + str(key))

        return isEnable

    def is_visible(self, locator, key):
        if str(key).startswith("Xpath_"):
            log.logger.info("Getting  text of element :" + str(key))
            # self.wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, configReader.readConfig(locator, key))))
            isVisible=EC.visibility_of_element_located((AppiumBy.XPATH, configReader.readConfig(locator, key)))
            # isVisible = self.driver.find_element(AppiumBy.XPATH, configReader.readConfig(locator, key))
            print(isVisible)
        elif str(key).startswith("AccessID_"):
            log.logger.info("Getting  text of element :" + str(key))
            self.wait.until(EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, configReader.readConfig(locator, key))))
            isVisible = self.driver.find_element(AppiumBy.XPATH, configReader.readConfig(locator, key))
        elif str(key).startswith("ID_"):
            log.logger.info("Getting  text of element :" + str(key))
            self.wait.until(EC.visibility_of_element_located((AppiumBy.ID, configReader.readConfig(locator, key))))
            isVisible = self.driver.find_element(AppiumBy.XPATH, configReader.readConfig(locator, key))
        else:
            log.logger.info("Getting  text of element :" + str(key))

        return isVisible
