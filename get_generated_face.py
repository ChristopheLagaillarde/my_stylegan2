# Program : get_generated_face
# Description : Get the face from thispersondoesnotexist.com
# Date : 28/05/22
# Author : Christophe Lagaillarde
# Version : 1.0

from selenium import webdriver


def get_generated_face(driver: webdriver) -> None:

    # Variable
    image_path: str = "images/generated_face.jpg"
    website_url: str = 'https://this-person-does-not-exist.com/fr'

    driver.get(website_url)

    src: str = driver.find_element_by_id('avatar').get_attribute('src')
    driver.get(src)

    with open(image_path, 'wb') as file:
        file.write(driver.find_element_by_xpath('/html/body/img').screenshot_as_png)

    return None
