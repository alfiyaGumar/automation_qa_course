import time
from pages.elements_page import TextBoxPage


class TestElements:
    def test_test(self, driver):
        text_box_page = TextBoxPage(driver, "https://demoqa.com/")
        text_box_page.open()
        input_data = text_box_page.fill_all_field()
        output_data = text_box_page.check_filled_form()
        assert input_data == output_data
        # full_name, email, current_address, permanent_address = text_box_page.fill_all_field()
        # output_name, output_email, output_current_address, output_permanent_address = text_box_page.fill_all_field()
        # assert full_name == output_name, "the full name does not math"
        # assert email == output_email, "the email does not math"
        # assert current_address == output_current_address, "the current_address does not math"
        # assert permanent_address == output_permanent_address, "the permanent_address does not math"


        time.sleep(5)

