# Unit Testing in Python
Learning how to use the *unittest* module. Unittest is in the standard library, so there is no need to install.

    import unittest
    import [module being tested]

This section of the repository will feature various simple functions, with examples on the best practise and methods for unit testing.

Effectively, unit testing makes sures that each function performs as it is meant to, and allows the developer to identify the problematic functions rather than manually going through all the code. Major timesaver, will make you friends.

### Why do We Unit Test?
Code needs to be thoroughly tested. Automated testing (as opposed to manual testing) saves enormous amounts of time. Automated testing allows us to see what code breaks and where (because all code inevitably breaks), which means we can quickly identify a problem that may be negatively affecting the entire program.

### Good Practice
- Syntax to name test modules: *"test_[ function ].py"* (e.g *test_calc.py*) - This is how the program knows it is a test. The test will be skipped if you fail this naming convention.
- Run within the conditional in order to make the terminal command shorter.
    if __name__ == '__main__':
    unittest.main()
- Include **good** tests and edge cases, quality not quantity.
- Tests should be isolated, don't rely on other tests.
- Some people use test-driven development. Creating the tests before the program. 
- **D-R-Y** - *Don't Repeat Yourself*. Contain any repetitive code (e.g. test variables) within the *setUp* class to keep your code clean.
- Test for the *success* **and** *failure* of functions.