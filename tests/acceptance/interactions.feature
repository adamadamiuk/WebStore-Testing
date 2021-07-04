Feature: Interaction with page elements
  Scenario: User can close GDPR promp
    Given User is on the home page
    And GDPR prompt informing about cookies is visible
    When User clicks "agree"
    Then The GDPR prompt disappears

  Scenario: User can filter the results by price
    Given User is on the "Man's watches" page
    When "Show filters" is selected
    And Price range 370 - 420 is selected
    Then The list of products in correct range is displayed

  Scenario: Searching, adding to the basket and removing an item
    Given User is on the home page
    And Searching for "Smartwatch" in the catalogue of products
    When The list of retrieved products includes smartwatches
    Then User adds a product to the basket
    And The item counter in the basket is 1
    When User removes an item from the basket
    Then The item counter in the basket is 0
