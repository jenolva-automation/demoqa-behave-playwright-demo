Feature: Click Checkboxes
  As a user
  I want to click Checkboxes
  So that I can see the selected checkbox values are displayed in the output section

Background:
    Given the user navigates to the home page
    When the user clicks on Elements text
    And the user clicks Check Box text

    Scenario: the user navigates to the Check Box section
    Then the Check Box text and fields will be visible

    Scenario: click the Home checkbox from unchecked state
    When the user clicks the Home checkbox from unchecked state
    Then all labels should be displayed in the output section
    
    