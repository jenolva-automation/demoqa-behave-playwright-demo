Feature: Enter Text in Text Boxes
  As a user
  I want to enter text in text boxes
  So that I can see submitted information is displayed in the output section

Background:
    Given the user navigates to the home page
    When the user clicks on Elements text
    And the user clicks on Text Box text
    
Scenario: the user navigates to the Text Box section
    Then the form text, textbox fields and submit button be visible
    Then the form text fields are empty

Scenario Outline: the user enters Full Name in the Full Name text box
    Then the Text Box text is visible
    When the user enters "<fullName>" into Full Name textbox
    And the user clicks on Submit button
    Then the entered full name: "<fullName>" in textbox should be displayed in the name output

    Examples:
      | fullName          |
      | John Doe         |
      | Jane Smith       |
      | Alice Johnson    |

Scenario Outline: the user enters Email in the Email text box
    Then the Text Box text is visible
    When the user enters "<email>" into Email textbox
    And the user clicks on Submit button
    Then the entered email: "<email>" in textbox should be displayed in the email output

    Examples:
      | email                  |
      | john.Doe@email.com     |
      | jane.Smith@email.com   |
      | alice.Johnson@email.com|

Scenario Outline: the user enters Current Address in the Current Address text box
    Then the Text Box text is visible
    When the user enters "<currentAddress>" into Current Address textbox
    And the user clicks on Submit button
    Then the entered current address: "<currentAddress>" in textbox should be displayed in the output

    Examples:
      | currentAddress               |
      | 123 Main St, Springfield     |
      | 456 Elm St, Shelbyville      |
      | 789 Oak St, Capital City     |

Scenario Outline: the user enters Permanent Address in the Permanent Address text box
    Then the Text Box text is visible
    When the user enters "<permanentAddress>" into Permanent Address textbox
    And the user clicks on Submit button
    Then the entered permanent address: "<permanentAddress>" in textbox should be displayed in the output

    Examples:
      | permanentAddress            |
      | 1230 Main St, Springfield     |
      | 4560 Elm St, Shelbyville      |
      | 7890 Oak St, Capital City     |