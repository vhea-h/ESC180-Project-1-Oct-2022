"""
Author of Starter Code: Michael Guerzhoy.  Last modified: Oct. 3, 2022

STUDENT INFO:
--------------
Modifications done by: Vhea He
UTORid: hevhea
Student Number: 1009525202
"""

#Initialize all global variables and constants 
def initialize():
    global cur_balance_owing_intst, cur_balance_owing_recent
    global last_update_day, last_update_month
    global last_country, last_country2
    global disabled
    global MONTHLY_INTEREST_RATE
    
    cur_balance_owing_intst = 0
    cur_balance_owing_recent = 0
    
    last_update_day, last_update_month = -1, -1
    
    last_country = None
    last_country2 = None   

    disabled = False 
    
    MONTHLY_INTEREST_RATE = 0.05

#Take two dates, (day1, month1) and (day2, month2), both integers
#Return true if (day1, month1) is the same or comes later than (day2, month2)
#Assume dates are valid in the year 2020
def date_same_or_later(day1, month1, day2, month2):

    #If dates are in same month, then compare days
    if (month1 == month2):
        if (day1 >= day2):
            return True
        elif(day1 < day2):
            return False
        else:
            print ("UNEXPECTED DAY COMPARISON ERROR")
    
    #If months different, no need to compare days. Only compare months
    elif(month1 > month2):
        return True

    elif(month1 < month2):
        return False
        
    else:
        print ("UNEXPECTED MONTH COMPARISON ERROR")
    
#Take 3 strings 'c1', 'c2' and 'c3'
#Return True if and only if the values of all three strings are different from each other
def all_three_different(c1, c2, c3):
    if c1 != c2 and c2 != c3 and c1 != c3:
        return True
    else:
        return False

#HELPER FUNCTION
#Take integer 'month'
#Determine whether any months have passed since last operation. If yes, perform all nessecary monthly tasks.
def monthly_update(month):
    global cur_balance_owing_intst, cur_balance_owing_recent
    global last_update_day, last_update_month
    
    #If the month has changed, find how many months have passed, move recent owed amounts to accuire interest 
    #   accordingly, and clear recent balance variable for the new month
    if month > last_update_month:
        #Find number of months since last update
        num_months_passed = month - last_update_month

        #Allow appropriate amounts to acquire after amount has been moved
        for i in range(num_months_passed):
            cur_balance_owing_intst += cur_balance_owing_intst * MONTHLY_INTEREST_RATE
        
        #Allow amounts outside to acquire interest for fewer months
        for i in range(num_months_passed - 1):
            cur_balance_owing_recent += cur_balance_owing_recent * MONTHLY_INTEREST_RATE
        
        #Add appropriate amount to interest acquiring balance from recent balance
        cur_balance_owing_intst += cur_balance_owing_recent
        
        #Reset recent balance for the new month
        cur_balance_owing_recent = 0

#HELPER FUNCTION
#Take two integers 'day' and 'month'
#Updates date of last update to date denoted by 'day' and 'month'
def update_date(day, month):
    global last_update_day, last_update_month
    last_update_day = day
    last_update_month = month

#Take float 'amount' and two integers 'day' and 'month'
#Perform a purchase of 'amount' on date denoted by 'day' and 'month'
def purchase(amount, day, month, country):
    global cur_balance_owing_intst, cur_balance_owing_recent 
    global last_update_day, last_update_month
    global last_country, last_country2
    global disabled

    #First check if card is disabled
    if disabled == False:
    
    #Check for possible problem scenarios
        #Current day is earlier than date of last operation
        if date_same_or_later(day, month, last_update_day, last_update_month) == False:
            return "error"

        #Suspected fraud: three different countries in a row
        if all_three_different(last_country, last_country2, country):
            disabled = True
            return "error"

        #If no faulty condition is found, check for monthly updates and continue with purchase process
        monthly_update(month) 
        cur_balance_owing_recent += amount

        #Update the date of last update
        update_date(day, month)

        #Update countries of purchase
        if last_country == last_country2 and last_country2 == None:
            last_country = country
            last_country2 = country
        last_country = last_country2
        last_country2 = country

    else:
        return "error"

#Take float two integers 'day' and 'month'
#Return amount owed on date denoted by 'day' and 'month'   
def amount_owed(day, month):
    global cur_balance_owing_intst, cur_balance_owing_recent 
    global last_update_day, last_update_month
   
  
    #First, check to see if date is valid (bad if current day is earlier than date of last operation)
    if date_same_or_later(day, month, last_update_day, last_update_month) == False:
            return "error"

    # Next, perform monthly updates in case much time has passed since last operation
    monthly_update(month)

    #Update the date of last update
    update_date(day, month)
    
    #Return amount owed
    return cur_balance_owing_intst + cur_balance_owing_recent

#Take float 'amount' and two integers 'day' and 'month'
#Pays off 'amount' in the amount owed on date denoted by 'day' and 'month'   
def pay_bill(amount, day, month):
    global cur_balance_owing_intst, cur_balance_owing_recent 
    global last_update_day, last_update_month
    global disabled

    #Check to see if date is valid (bad if current day is earlier than date of last operation)
    if date_same_or_later(day, month, last_update_day, last_update_month) == False:
        return "error"
    
    monthly_update(month)

    #Pay off amount owed (in interest acquiring balance first)
    if amount < cur_balance_owing_intst:
        cur_balance_owing_intst -= amount
    else:
        difference = amount - cur_balance_owing_intst
        cur_balance_owing_intst = 0

        #Pay off recent amount owed if others already payed out
        if difference < cur_balance_owing_recent:
            cur_balance_owing_recent -= difference
        else:
            cur_balance_owing_recent = 0

    #Update the date of last update
    update_date(day, month)

#TESTING HELPER FUNCTION
#Take a string "test_name", an expected value "expected_value" and an actual value "actual_value" (usually from testing a function's output) 
# Print a test has been "passed" if actual_value is equal to expected_value. Print the test has "failed" otherwise. Include test names in results. 
def print_test_results(test_name, expected_value, actual_value):
    if actual_value == expected_value:
        print (test_name, "= Passed")
    else:
        print (test_name, "= Failed")

# Initialize all global variables outside the main block.
initialize()		
    
if __name__ == '__main__':

    #Printing title for sample simulation segment
    print("------------------------------------------------------")
    print("SAMPLE SIMULATION [Given in starter code]") 
    print("------------------------------------------------------")

    initialize()
    purchase(80, 8, 1, "Canada")
    print("Now owing:", amount_owed(8, 1))      # 80.0                              (Test1)
    pay_bill(50, 2, 2)
    print("Now owing:", amount_owed(2, 2))      # 30.0     (=80-50)                 (Test2)
    print("Now owing:", amount_owed(6, 3))      # 31.5     (=30*1.05)               (Test3)
    purchase(40, 6, 3, "Canada")
    print("Now owing:", amount_owed(6, 3))      # 71.5     (=31.5+40)               (Test4)
    pay_bill(30, 7, 3)
    print("Now owing:", amount_owed(7, 3))      # 41.5     (=71.5-30)               (Test5)
    print("Now owing:", amount_owed(1, 5))      # 43.65375 (=1.5*1.05*1.05+40*1.05) (Test6)
    purchase(40, 2, 5, "France")
    print("Now owing:", amount_owed(2, 5))      # 83.65375                          (Test7)
    print(purchase(50, 3, 5, "United States"))  # error    (3 diff. countries in    (Test8)
                                                #          a row)
                                                
    print("Now owing:", amount_owed(3, 5))      # 83.65375 (no change, purchase     (Test9)
                                                #           declined)
    print(purchase(150, 3, 5, "Canada"))        # error    (card disabled)          (Test10)
    print("Now owing:", amount_owed(1, 6))      # 85.8364375                        (Test11)
                                                # (43.65375*1.05+40)
 
    #TESTING STRATEGY
    #Testing for parts a) and b) use a custom testing function defined above to match chosen test cases to their expected values
    #   The test cases are fed to the print_test_results() function, which determines whether the function being tested is outputting correct values
    #   Each test case is listed and described below

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

        #Testing all 3 different | Expected: True
    print_test_results("All 3 different test", True, all_three_different("cat", "dog", "mouse"))
