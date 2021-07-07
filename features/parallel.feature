Feature: parallel test
    Scenario Outline: parallel run
        Given Executing <feature> <scenario>

        Examples: test 1
            | feature           | scenario  |
            | test-1.feature    | test 1    |
        
        Examples: test 2
            | feature           | scenario  |
            | test-2.feature    | test 2    |
        
        Examples: test 3
            | feature           | scenario  |
            | test-3.feature    | test 3    |
        
        Examples: test 4
            | feature           | scenario  |
            | test-4.feature    | test 4    |
        
        Examples: test 5
            | feature           | scenario  |
            | test-5.feature    | test 5    |
    