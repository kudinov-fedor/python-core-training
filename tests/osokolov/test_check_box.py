from selenium.webdriver.common.by import By

HOST = 'https://demoqa.com'


def test_text_box(browser):
    path = '/checkbox'
    browser.get(f'{HOST}{path}')

    expand_all_button = browser.find_element(By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-expand-all"]')
    collapse_all_button = browser.find_element(By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-collapse-all"]')
    expand_all_button.click()

    documents_folder = browser.find_element(By.CSS_SELECTOR, 'label[for="tree-node-documents"]')
    documents_folder.click()

    documents_folder_checkbox = documents_folder.find_element(By.CSS_SELECTOR, 'input[id="tree-node-documents"]')

    assert documents_folder_checkbox.is_selected()
