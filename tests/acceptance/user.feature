Feature: Testing user account functionalities
  Scenario: User can log in to the store
    Given User is on the login page
    When User types in login and password
    And User clicks log in button
    Then "My Account" page is displayed

  Scenario: User tries to log in using incorrect credentials
    Given User is on the login page
    When User types in wrong login and password
    And User clicks log in button
    Then Login error page is displayed