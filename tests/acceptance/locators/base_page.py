from selenium.webdriver.common.by import By


class BasePageLocators:
    TITLE = By.TAG_NAME, 'strong'
    NAV_LINKS =  By.ID, 'navigation'
    DROPDOWN = By.ID, 'trigger'
    DROPDOWN_LINKS = By.ID, 'dropdown_link'
    PAGE = By.ID, 'page-index'
    CLEAR_BUTTON = By.ID, 'clear'
    DOWNLOAD_BUTTON = By.ID, 'download'
    PREDICT_BUTTON = By.ID, 'predict'
    RESULT = By.ID, 'predict'

