Feature: Tests Failed Search

Scenario: failed
  Given with path /company/036384
  When method GET
  Then status 404
