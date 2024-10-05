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

    # regular purchase (1 /month), pays back at beginning of next month
    print("TEST CASE 1")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    print("Now owing:", amount_owed(31, 1))  # 80.0
    pay_bill(80, 1, 2)
    purchase(80, 1, 2, "Canada")
    print("Now owing:", amount_owed(29, 2))  # 80.0
    pay_bill(80, 1, 3)
    purchase(80, 1, 3, "Canada")
    print("Now owing:", amount_owed(31, 3))  # 80.0

    # regular purchase (1 /month), pays half at beginning of next month
    print("TEST CASE 2")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    print("Now owing:", amount_owed(31, 1))  # 80.0
    pay_bill(40, 1, 2)  # 40
    purchase(80, 1, 2, "Canada")  # 120 (40 + 80)
    print("Now owing:", amount_owed(29, 2))  # 120.0 (40 interest, 80 non-interest)
    print("Now owing:", amount_owed(1, 3))  # 122.0 (40*1.05+80 interest, 0 non-interest)
    pay_bill(40, 1, 3)  # 82.0 (82 interest, 0 non-interest)
    purchase(80, 1, 3, "Canada")  # 162.0 (82 interest, 80 non-interest)
    print("Now owing:", amount_owed(31, 3))  # 162.0 (82 interest, 80 non-interest)
    print("Now owing:", amount_owed(1, 4))  # 166.1 (86.1+80 interest, 0 non-interest)

    # regular purchase (2 /month), pays back at beginning of next month
    print("TEST CASE 3")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 2, 1, "Canada")
    print("Now owing:", amount_owed(31, 1))  # 80.0
    pay_bill(160, 1, 2)
    purchase(80, 1, 2, "Canada")
    purchase(80, 2, 2, "Canada")
    print("Now owing:", amount_owed(29, 2))  # 80.0
    pay_bill(160, 1, 3)
    purchase(80, 1, 3, "Canada")
    purchase(80, 2, 3, "Canada")
    print("Now owing:", amount_owed(31, 3))  # 80.0

    # regular purchase (2 /month), pays half at beginning of next month
    print("TEST CASE 4")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 2, 1, "Canada")
    print("Now owing:", amount_owed(31, 1))  # 160.0
    pay_bill(80, 1, 2)  # 80
    purchase(80, 1, 2, "Canada")  # 160 (80 + 80)
    purchase(80, 2, 2, "Canada")
    print("Now owing:", amount_owed(29, 2))  # 240.0 (80 interest, 160 non-interest)
    print("Now owing:", amount_owed(1, 3))  # 244.0 (244 interest, 0 non-interest)
    pay_bill(80, 1, 3)  # 164.0 (164 interest, 0 non-interest)
    purchase(80, 1, 3, "Canada")  # 244.0 (164 interest, 80 non-interest)
    purchase(80, 2, 3, "Canada")
    print("Now owing:", amount_owed(31, 3))  # 324.0 (164 interest, 160 non-interest)
    print("Now owing:", amount_owed(1, 4))  # 332.2 (332.2 interest, 0 non-interest)

    # buy once, pay in june in full, check in december
    print("TEST CASE 5")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    print("Now owing:", amount_owed(15, 6))  # 80->80->84->88.2->92.61->97.2405(in june)
    pay_bill(97.24050000000001, 15, 6)
    print("Now owing:", amount_owed(15, 6))
    print("Now owing:", amount_owed(31, 12))

    # buy once, pay in june in partial, check in december
    print("TEST CASE 6")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    print("Now owing:", amount_owed(15, 6))  # 80->80->84->88.2->92.61->97.2405(in june)
    pay_bill(10, 15, 6)  # 87.2405 remaining
    print("Now owing:", amount_owed(15, 6))  # 87.2405->91.602525(july)->96.18265125->100.9917838125->106.0413730031->
    print("Now owing:", amount_owed(31, 12))  # 111.3434416533 in november -> 116.9106137359 in december

    # buy once, buy again in early june, pay in june in full for jan debt+interest, check in december
    print("TEST CASE 7")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 1, 6, "Canada")
    print("Now owing:", amount_owed(15, 6))  # (80->80->84->88.2->92.61->97.2405(in june)) + 80 new debt => 177.2405
    pay_bill(97.2405, 15, 6)  # 80 new debt remaining
    print("Now owing:", amount_owed(15, 6))  # 80
    print("Now owing:", amount_owed(31, 12))  # 80->80->84->88.2->92.61->97.2405->102.102525

    # buy once, buy again in early june, pay in june (slightly more than jan debt+interest), check in december
    print("TEST CASE 8")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 1, 6, "Canada")
    print("Now owing:", amount_owed(15, 6))  # (80->80->84->88.2->92.61->97.2405(in june)) + 80 new debt => 177.2405
    pay_bill(100, 15, 6)  # 77.2405 (all new debt) remaining
    print("Now owing:", amount_owed(15, 6))
    print("Now owing:", amount_owed(31, 12))  # 77.2405->77.2405->81.102525->85.15765125
    # ->89.4155338125->93.8863105031->98.5806260283 (at dec)

    # buy once, buy again in early june, pay in june (slightly less than jan debt+interest), check in december
    print("TEST CASE 9")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 1, 6, "Canada")
    print("Now owing:", amount_owed(15, 6))  # (80->80->84->88.2->92.61->97.2405(in june)) + 80 new debt => 177.2405
    pay_bill(90, 15, 6)  # 87.2405 remaining (7.2405 old debt)
    print("Now owing:", amount_owed(15, 6))
    print("Now owing:", amount_owed(31, 12))  # 80+7.2405(june)->80+7.602525 (87.602525)->91.98265125->96.5817838125
    # ->101.4108730031->106.4814166533->111.805487486

    # buy once, forget about the card
    print("TEST CASE 10")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    print("Now owing:", amount_owed(31, 12))  # 80->80(feb)->(80*1.05^10)(dec)130.3115701422

    # buy once, pay back immediately forget about the card
    print("TEST CASE 11")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    pay_bill(80, 1, 1)
    print("Now owing:", amount_owed(31, 12))  # 0

    # TEST 4 but with alternating 2 countries
    print("TEST CASE 12")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 2, 1, "France")
    print("Now owing:", amount_owed(31, 1))  # 160.0
    pay_bill(80, 1, 2)  # 80
    purchase(80, 1, 2, "Canada")  # 160 (80 + 80)
    purchase(80, 2, 2, "France")
    print("Now owing:", amount_owed(29, 2))  # 240.0 (80 interest, 160 non-interest)
    print("Now owing:", amount_owed(1, 3))  # 244.0 (244 interest, 0 non-interest)
    pay_bill(80, 1, 3)  # 164.0 (164 interest, 0 non-interest)
    purchase(80, 1, 3, "Canada")  # 244.0 (164 interest, 80 non-interest)
    purchase(80, 2, 3, "France")
    print("Now owing:", amount_owed(31, 3))  # 324.0 (164 interest, 160 non-interest)
    print("Now owing:", amount_owed(1, 4))  # 332.2 (332.2 interest, 0 non-interest)

    # TEST 4 but with alternating 3 countries
    print("TEST CASE 13")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 2, 1, "France")
    print("Now owing:", amount_owed(31, 1))  # 160.0
    pay_bill(80, 1, 2)  # 80 interest building debt
    purchase(80, 1, 2, "China")  # FRAUD - ERROR, still 80
    purchase(80, 2, 2, "France")  # ALREADY FRAUD - ERROR, still 80
    print("Now owing:", amount_owed(29, 2))  # 80 (80 interest, 0 non-interest)
    print("Now owing:", amount_owed(1, 3))  # 84.0 (84 interest, 0 non-interest)
    pay_bill(80, 1, 3)  # 4.0 (4 interest, 0 non-interest)
    purchase(80, 1, 3, "Canada")  # ALREADY FRAUD - ERROR, still 4
    purchase(80, 2, 3, "France")  # ALREADY FRAUD - ERROR, still 4
    print("Now owing:", amount_owed(31, 3))  # 4.0 (4 interest, 160 non-interest)
    print("Now owing:", amount_owed(1, 4))  # 4.2 (4.2 interest, 0 non-interest)

    # TEST 4 but with same country -> then 2 other countries
    print("TEST CASE 14")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 2, 1, "Canada")
    print("Now owing:", amount_owed(31, 1))  # 160.0
    pay_bill(80, 1, 2)  # 80
    purchase(80, 1, 2, "Canada")  # 160 (80 + 80)
    purchase(80, 2, 2, "Canada")
    print("Now owing:", amount_owed(29, 2))  # 240.0 (80 interest, 160 non-interest)
    print("Now owing:", amount_owed(1, 3))  # 244.0 (244 interest, 0 non-interest)
    pay_bill(80, 1, 3)  # 164.0 (164 interest, 0 non-interest)
    purchase(80, 1, 3, "China")  # 244.0 (164 interest, 80 non-interest)
    purchase(80, 2, 3, "France")  # FRAUD, STILL 244 (164 interest, 80 non-interest)
    print("Now owing:", amount_owed(31, 3))  # 244 (164 interest, 80 non-interest)
    print("Now owing:", amount_owed(1, 4))  # 252.2 (164*1.05+80 interest, 0 non-interest)

    # TEST 4 but with 3 countries, but each country purchase twice
    print("TEST CASE 15")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(80, 2, 1, "Canada")
    print("Now owing:", amount_owed(31, 1))  # 160.0
    pay_bill(80, 1, 2)  # 80
    purchase(80, 1, 2, "France")  # 160 (80 + 80)
    purchase(80, 2, 2, "France")
    print("Now owing:", amount_owed(29, 2))  # 240.0 (80 interest, 160 non-interest)
    print("Now owing:", amount_owed(1, 3))  # 244.0 (244 interest, 0 non-interest)
    pay_bill(80, 1, 3)  # 164.0 (164 interest, 0 non-interest)
    purchase(80, 1, 3, "China")  # 244.0 (164 interest, 80 non-interest)
    purchase(80, 2, 3, "China")
    print("Now owing:", amount_owed(31, 3))  # 324.0 (164 interest, 160 non-interest)
    print("Now owing:", amount_owed(1, 4))  # 332.2 (332.2 interest, 0 non-interest)

    # Fraud early on, but don't pay back
    print("TEST CASE 16")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(50, 2, 1, "France")
    purchase(30, 2, 1, "Germany")
    purchase(30, 3, 1, "Germany")
    print("Now owing:", amount_owed(31, 1))  # 130.0
    print("Now owing:", amount_owed(31, 2))  # 130.0
    print("Now owing:", amount_owed(31, 3))  # 130*1.05
    print("Now owing:", amount_owed(31, 12))  # 130*1.05**10=211.7563014811

    # Fraud early on, but pay back
    print("TEST CASE 17")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(50, 2, 1, "France")
    purchase(30, 2, 1, "Germany")
    purchase(30, 3, 1, "Germany")
    pay_bill(130, 3, 1)
    print("Now owing:", amount_owed(31, 1))  # 0
    print("Now owing:", amount_owed(31, 2))  # 0
    print("Now owing:", amount_owed(31, 3))  # 0
    print("Now owing:", amount_owed(31, 12))  # 0

    # Fraud early on, but pay back
    print("TEST CASE 18")
    initialize()  # reset the code
    purchase(80, 1, 1, "Canada")
    purchase(50, 2, 2, "France")
    pay_bill(90, 3, 2)  # now owe 40 non interest
    purchase(30, 3, 3, "Germany")
    purchase(30, 4, 4, "Germany")
    print("Now owing:", amount_owed(31, 3))  # 40 interested money
    print("Now owing:", amount_owed(31, 12))  # 40*1.05**9
