# Run ONLY Login feature with below command
# behave -n 'Login'

Feature: MCUX

    Scenario: Login Archive
        Given I navigate to "Archive" login page "http://newsmam"
        When I enter "name" as "user_mname" "password" as "xxxxxx"
        And I click on "input" "id" "loginButton"
        Then I am taken to home page of "MCUX" with page title contains "MediaCentral"

    Scenario: Login WG05
        Given I navigate to "WG05" login page
        When I enter "name" as "user_name" "password" as "xxxxxxx"
        And I click on "input" "id" "loginButton"
        Then I am taken to home page of "MCUX" with page title contains "WG05"

    Scenario: Index Search
        Given I navigate to "Archive" login page
        When I enter "name" as "user_name" "password" as "xxxxxxx"
        And I click on "input" "id" "loginButton"
        Then I am taken to home page of "MCUX" with page title contains "MediaCentral"
        And I can Index search word "Obama"
