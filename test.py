import time
from selenium.webdriver.common.keys import Keys
from GooglePages import SearchHelper


def test_string_find(browser):
    google_page = SearchHelper(browser)
    google_page.go_to_site()
    text = google_page.enter_word("купить кофемашину bork c804")
    text.send_keys(Keys.ENTER)

    count_result = google_page.count_results()
    assert 10 <= count_result, f'Ошибка количество строк поиска  {count_result}'

    mvideo_result = google_page.mvideo_result()
    assert 'mvideo.ru' in mvideo_result, f'mvideo.ru нет в поиске'







