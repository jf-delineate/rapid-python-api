Feature: Tests Successful Search

Scenario: successful
  Given with path /company/03638404
  When method GET
  Then status 200
