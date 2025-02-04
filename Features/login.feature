Feature: Itaka login feature

  @regression
  Scenario: Successful login
    Given I am on the login page
    And I fill in the username
    And I fill in the password
    When I press the login button
    Then I am taken to client area and should see welcome message

  @regression
  Scenario: Successful logout
    When I press the logout button
    Then I should see the login page

  @regression
  Scenario: Empty credentials login
    When I press the login button
    Then I should see error messages