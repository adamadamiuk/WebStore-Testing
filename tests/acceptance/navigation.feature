Feature: Testing navigation within the web store
  Scenario: User goes from homepage to login page
    Given User is on the home page
    When User clicks "My Account"
    Then User is on the login page

  Scenario: User can go from home page to the catalogue of products
    Given User is on the home page
    When User hovers over "Men's watches" button
    And "Zagarki meskie na pasku" category is selected
    Then User is on the catalogue page