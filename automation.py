import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize the WebDriver (provide the path to your WebDriver executable)
driver = webdriver.Chrome()

# Navigate to localhost:5000
driver.get("http://localhost:5000")

# Find the file input field and send the path to the image you want to upload
image_filename = 'test.png'  # Change this to your image filename
image_path = os.path.abspath(image_filename)
file_input = driver.find_element(By.NAME, "image")
file_input.send_keys(image_path)

# Find and click the submit button
submit_button = driver.find_element(By.XPATH, "/html/body/form/input[2]")
submit_button.click()

# Give some time for the image to upload and the response to come back
time.sleep(5)

# Get the result (image path) from the page
result = driver.find_element(By.TAG_NAME, "body").text
print("Uploaded image path:", result)

# Close the WebDriver
driver.quit()
