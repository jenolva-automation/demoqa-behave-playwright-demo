Feature: Enter Text in Text Boxes
  As a user
  I want to enter text in text boxes
  So that I can see submitted information is displayed in the output section

Background:
    Given the user navigates to the home page

Scenario: the user navigates to the Text Box section
    When the user clicks on Elements text
    When the user clicks on Text Box text
    Then the form text, textbox fields and submit button be visible
    Then the form text fields are empty
     