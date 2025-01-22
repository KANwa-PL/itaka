Feature: Itaka login feature

  Scenario: Successful login
    Given I am on the login page
    And I fill in the username with "default.test.user100@gmail.com"
    And I fill in the password with "DefaultTestPa$$w0rd"
    When I press the login button
    Then I am taken to client area and should see welcome message