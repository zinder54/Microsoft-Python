def collect_user_input():
    principle = input("please input principle amount:")
    interest = input("input the interest amount")
    frequency = input("input the frequency of interest")
    time = ("input the length of time for compounding")
    return principle,interest,frequency,time

def calculate_compound_interest(amount_first, rate, time, freq):
    amount = amount_first * (1 + rate / freq) ** (freq * time)
    return amount
    
def Return_compound_amount():
    collect_user_input()
    calculate_compound_interest(principle,)
collect_user_input()