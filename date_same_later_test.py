#Take two dates, (day1, month1) and (day2, month2)
#Return true if (day1, month1) is the same or comes later than (day2, month2)
#Assume dates are valid in the year 2020
def date_same_or_later(day1, month1, day2, month2):
    if (month1 == month2):
        if (day1 >= day2):
            return True
        elif (day1 < day2):
            return False
        else:
            print ("UNEXPECTED DAY COMPARISON ERROR")

    elif(month1 > month2):
        return True

    elif(month1 < month2):
        return False
        
    else:
        print ("UNEXPECTED MONTH COMPARISON ERROR")

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
    print("TEST CASES FOR DAY COMPARISON [date_same_or_later()]") 
    print("------------------------------------------------------")

    #TEST CASES FOR DAY COMPARISON [date_same_or_later()]:
        #Testing same month later day | Mar.23, vs. Mar.3 | Expected: True
    print_test_results("Same month later day test", True, date_same_or_later(23, 3, 12, 3))

        #Testing same month earlier day | Feb.3, vs. Feb.13 | Expected: False
    print_test_results("Same month earlier day test", False, date_same_or_later(3, 2, 13, 2))

        #Testing same month same day | Feb.3, vs. Feb.3 | Expected: True
    print_test_results("Same month same day test", True, date_same_or_later(3, 2, 3, 2))

        #Testing later month later day | Mar.23, vs. Feb.13 | Expected: True
    print_test_results("Later month later day test", True, date_same_or_later(23, 3, 13, 2))

        #Testing later month same day | Mar.13, vs. Feb.13 | Expected: True
    print_test_results("Later month same day test", True, date_same_or_later(13, 3, 13, 2))

        #Testing later month earlier day | Mar.3, vs. Feb.13 | Expected: True
    print_test_results("Later month earlier day test", True, date_same_or_later(3, 3, 13, 2))

        #Testing earlier month same day | Oct.3, vs. Nov.3 | Expected: False
    print_test_results("Earlier month same day test", False, date_same_or_later(3, 10, 3, 11))

        #Testing earlier month later day | Oct.31, vs. Dec.13 | Expected: False
    print_test_results("Earlier month later day test", False, date_same_or_later(31, 10, 13, 12))

        #Testing earlier month earlier day | Oct.3, vs. Dec.13 | Expected: False
    print_test_results("Earlier month earlier day test", False, date_same_or_later(3, 10, 13, 12))

"""
Test Cases for Date Comparison (with expected values):

Testing same month later day: True

Testing same month earlier day: False

Testing same month same day: True

Testing later month later day: True

Testing later month same day: True

Testing later month earlier day: True

Testing earlier month same day: False

Testing earlier month later day: False

Testing earlier month earlier day: False

"""