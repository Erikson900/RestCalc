import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pytest



@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8080")
    yield driver
    driver.quit()

def test_addition(setup):
    driver = setup
    rendomNUm1 = float(random.randint(0,100))
    rendomNUm2 = float(random.randint(0,100))
    sum = rendomNUm1 + rendomNUm2
    driver.find_element(By.ID, "num1").send_keys(str(rendomNUm1))
    driver.find_element(By.ID, "num2").send_keys(str(rendomNUm2))
    driver.find_element(By.XPATH, "//button[text()='Add']").click()
    result = driver.find_element(By.ID, "result").text
    assert result == f"Result: {sum}"

def test_subtraction(setup):
    driver = setup
    count = 0
    for i in range(3):
        rendomNUm1 = float(random.randint(0, 100))
        rendomNUm2 = float(random.randint(0, 100))
        sub = rendomNUm1 - rendomNUm2
        driver.find_element(By.ID, "num1").send_keys(str(rendomNUm1))
        driver.find_element(By.ID, "num2").send_keys(str(rendomNUm2))
        driver.find_element(By.XPATH, "//button[text()='Subtract']").click()
        result = driver.find_element(By.ID, "result").text
        driver.find_element(By.ID, "num1").clear()
        driver.find_element(By.ID, "num2").clear()
        if result == f"Result: {sub}":
            count += 1
    assert 3 == count


def test_FirstFieldAisEmpty(setup):
    driver = setup
    driver.find_element(By.ID, "num2").send_keys("3")
    driver.find_element(By.XPATH, "//button[text()='Subtract']").click()
    result = driver.find_element(By.ID, "result").text
    assert result == "Please enter both numbers."

def test_SecondFieldAisEmpty(setup):
    driver = setup
    driver.find_element(By.ID, "num1").send_keys("3")
    driver.find_element(By.XPATH, "//button[text()='Subtract']").click()
    result = driver.find_element(By.ID, "result").text
    assert result == "Please enter both numbers."

def test_BothFieldsAreEmpty(setup):
    driver = setup
    driver.find_element(By.XPATH, "//button[text()='Subtract']").click()
    result = driver.find_element(By.ID, "result").text
    assert result == "Please enter both numbers."