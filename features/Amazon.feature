
Feature: Amazon
    Scenario: Check Amazon
        Given I navigate to "Amazon" login page "https://www.amazon.com/"
        Then I am taken to home page of "Amazon" with page title contains "Amazon.com"

    Scenario: Find Product
        Given I navigate to "Amazon" login page "https://www.amazon.com/"
        And I search for the product "Samsung Galaxy S8"
