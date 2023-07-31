# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import pytest
from group import Group
from application import Application

class AppDynamicsJob(unittest.TestCase):
    def setUp(self):
        # AppDynamics will automatically override this web driver
        # as documented in https://docs.appdynamics.com/display/PRO44/Write+Your+First+Script
        self.app = Application()

    def test_add_group(self):
        wd = self.wd
        self.app.login(username="admin", password="secret")
        self.app.open_groups_page(wd)
        self.app.create_group(wd, Group(name="ddd", header="ffff", footer="fff"))
        self.app.logout()

    def test_add_empty_group(self):
        wd = self.wd
        self.app.login(username="admin", password="secret")
        self.app.open_groups_page()
        self.app.create_group(wd, Group(name="", header="", footer=""))
        self.app.logout()


    def tearDown(self):
        self.app.destroy()
        # To know more about the difference between verify and assert,
        # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results


if __name__ == "__main__":
    unittest.main()
