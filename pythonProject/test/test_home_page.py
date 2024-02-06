import pytest
from PageObject.careers_page import CareersPage
from PageObject.home_page import HomePage
from PageObject.quality_assurance_page import QualityAssurancePage


class TestHomePage:

    def test_homepage(self, driver):
        home_page = HomePage(driver)
        home_page.open()

        assert home_page.expected_url == "https://useinsider.com/", "URL is incorrect"

    def test_careers_page(self, driver):
        home_page = HomePage(driver)
        home_page.open()
        careers_page = CareersPage(driver)
        careers_page.open_tab()

        assert careers_page.is_block_our_locations_displayed(), "'Our Locations' block is not displayed"
        assert careers_page.is_button_see_all_teams_displayed(), "'See all teams' button is not displayed"
        assert careers_page.is_life_at_insider_displayed(), "'Life at Insider' block is not displayed"

    def test_quality_assurance_page(self, driver):
        quality_assurance_page = QualityAssurancePage(driver)
        quality_assurance_page.open()
        quality_assurance_page.open_tab()
        quality_assurance_page.apply_filters('Istanbul, Turkey', 'Quality Assurance')

        assert quality_assurance_page.get_list_of_positions() == ['Senior Software Quality Assurance Engineer',
                                                                  'Software QA Tester- Insider Testinium Tech Hub (Remote)',
                                                                  'Software Quality Assurance Engineer']

    def test_quality_assurance_page_role(self, driver):
        quality_assurance_page = QualityAssurancePage(driver)
        quality_assurance_page.open()
        quality_assurance_page.open_tab()
        quality_assurance_page.apply_filters('Istanbul, Turkey', 'Quality Assurance')

        assert quality_assurance_page.is_all_quality_assurance(), "Not all are Quality Assurance"
        assert quality_assurance_page.is_all_location_istanbul(), "Not all location contains Istanbul, Turkey"

    def test_view_role_redirect(self, driver):
        quality_assurance_page = QualityAssurancePage(driver)
        quality_assurance_page.open()
        quality_assurance_page.open_tab()
        quality_assurance_page.apply_filters('Istanbul, Turkey', 'Quality Assurance')
        quality_assurance_page.open_view_role()
        assert quality_assurance_page.verify_new_url() == 'https://jobs.lever.co/useinsider/78ddbec0-16bf-4eab-b5a6-04facb993ddc', \
            "URL is incorrect"
