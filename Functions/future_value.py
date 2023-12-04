# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 08:38:48 2023

@author: arun.rameshbabu
"""



def future_value_fn(month_invest, yearly_int, time_yr=20):
    """
    This function calculates and returns a future value for a given
    monthly investment, yearly interest and term.

    Parameters
    ----------
    month_invest : int / float
        Amount that is invested monthly.
    yearly_int : int / float
        Yearly interest rate.
    time_yr : int / float
        Number of years for which the recurring investment is made.

    Returns
    -------
    f_value : int / float
        The investment value at the end of the term specified.

    """
    m_time = time_yr *12
    m_int_rt = yearly_int / 12
    f_value = 0
    for i in range(m_time):
        f_value = month_invest + f_value
        f_value += (f_value * m_int_rt)/100
    return f_value

if __name__ == "__main__":
    print(future_value_fn(150, 10, 5))
    
    # continue_loop='y'
    # while continue_loop.lower() == 'y':
    #     mon_invest = float(input("Enter monthly investment:\t\t"))
    #     y_int_rt = int(input("Enter yearly interest rate:\t\t"))
    #     y_time = int(input("Enter number of years:\t\t"))
    #     future_val = future_value(mon_invest, y_int_rt, y_time)
    #     print("Future value:\t\t\t\t{}".format(future_val))
    #    continue_loop = input("\nContinue? (y/n): ")