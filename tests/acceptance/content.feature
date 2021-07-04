Feature: Page has correct content
Inspecting the content of the page

  Scenario: Testing that the Home Page has correct content
    Given User is on the home page
    And Menu bar is visible
    And "My account" button is visible
    And GDPR prompt informing about cookies is visible

   Scenario: There is zero items in the basket
    Given User is on the home page
    And User can see the basket
    Then The item counter in the basket is 0

