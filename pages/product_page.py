from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def check_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET).text
        assert product_name == product_in_basket, "В корзину добавлен не тот товар"

    def message_after_accept_allerts(self):
        message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text
        assert message == self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET).text + \
               " has been added to your basket.", "Сообщение некорректное."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
