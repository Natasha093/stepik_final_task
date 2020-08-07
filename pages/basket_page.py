from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items is presented, but should not be"

    def should_be_message_in_basket(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE).text
        assert message == "Your basket is empty. Continue shopping", \
            "Basket message is not presented, but should be"