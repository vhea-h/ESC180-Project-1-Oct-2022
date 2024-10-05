#Take 3 strings 'c1', 'c2' and 'c3'
#Return True if and only if the values of all three strings are different from each other
def all_three_different(c1, c2, c3):
    if c1 != c2 and c2 != c3 and c1 != c3:
        return True
    else:
        return False

#TESTING HELPER FUNCTION
#Take a string "test_name", an expected value "expected_value" and an actual value "actual_value" (usually from testing a function's output) 
# Print a test has been "passed" if actual_value is equal to expected_value. Print the test has "failed" otherwise. Include test names in results. 
def print_test_results(test_name, expected_value, actual_value):
    if actual_value == expected_value:
        print (test_name, "= Passed")
    else:
        print (test_name, "= Failed")

if __name__ == "__main__":
    #Printing title for testing segment
    print("------------------------------------------------------")
    print("TEST CASES FOR STRING COMPARISON [all_three_different()]") 
    print("------------------------------------------------------")

    #TEST CASES FOR STRING COMPARISON [all_three_different()]:
        #Testing all 3 same | Expected: False
    print_test_results("All 3 same test", False, all_three_different("cat", "cat", "cat"))

        #Testing first 2 same | Expected: False
    print_test_results("First 2 same test", False, all_three_different("cat", "cat", "dog"))

        #Testing last 2 same | Expected: False
    print_test_results("Last 2 same test", False, all_three_different("dog", "cat", "cat"))

        #Testing first and last same | Expected: False
    print_test_results("First and last same test", False, all_three_different("cat", "dog", "cat"))

        #Testing different | Expected: True
    print_test_results("All 3 different test", True, all_three_different("cat", "dog", "cat"))