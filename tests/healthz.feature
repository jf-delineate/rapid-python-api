Feature: Tests Healthz

Scenario: health
  Given with path /healthz
  When method GET
  Then status 200
