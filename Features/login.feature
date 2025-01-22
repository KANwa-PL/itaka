Feature: Itaka login feature

  Scenario: Successful login
    Given I am on the login page
    And I fill in the username
    And I fill in the password
    When I press the login button
    Then I am taken to client area and should see welcome message