from BaseApp import BasePage
from selenium.webdriver.common.by import By


class GoogleSearchLocators:
    LOCATOR_GOOGLE_SEARCH_FIELD = (By.CSS_SELECTOR, 'input[name="q"]')
    LOCATOR_GOOGLE_SEARCH_BUTTON = (By.CSS_SELECTOR, 'input[type="submit"]')
    LOCATOR_GOOGLE_RESULT_SEARCH = (By.CLASS_NAME, "g")
    LOCATOR_GOOGLE_MVIDEO_SEARCH = (By.TAG_NAME, "cite")


class SearchHelper(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(GoogleSearchLocators.LOCATOR_GOOGLE_SEARCH_BUTTON, time=2).click()

    def count_results(self):
        all_list = self.find_elements(GoogleSearchLocators.LOCATOR_GOOGLE_RESULT_SEARCH, time=2)
        return len(all_list)

    def mvideo_result(self):
        all_list = self.find_elements(GoogleSearchLocators.LOCATOR_GOOGLE_MVIDEO_SEARCH, time=2)
        mvideo_search = [x.text for x in all_list if len(x.text) > 0]
        for x in range(len(mvideo_search)):
            if 'mvideo.ru' in mvideo_search[x]:
                return mvideo_search[x]
        return None