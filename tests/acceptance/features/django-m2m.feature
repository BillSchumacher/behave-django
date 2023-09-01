# Created by billschumacher at 9/1/23
Feature: Querying a many-to-many relationship

  Scenario: Querying groups and permissions on User
    Given A user exists
    When I query the user groups and permissions
    Then No error is raised