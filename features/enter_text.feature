Feature: Enter Text in Text Boxes
  As a user
  I want to enter text in text boxes
  So that I can see submitted information is displayed in the output section

Background:
    Given the user navigates to the home page
    When the user clicks on Elements text
    When the user clicks on Text Box text
    
Scenario: the user navigates to the Text Box section
    Then the form text, textbox fields and submit button be visible
    Then the form text fields are empty

Scenario Outline: the user enters Full Name in the Full Name text box
    When the user enters "<fullName>" into Full Name textbox
    And the user clicks on Submit button
    Then the entered full name: "<fullName>" in textbox should be displayed in the name output

    Examples:
      | fullName          |
      | John Doe         |
      | Jane Smith       |
      | Alice Johnson    |