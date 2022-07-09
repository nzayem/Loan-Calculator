import math
import argparse


def loan_principal(annual_pay, periods, interest):
    nominal_rate = interest / 1200

    loan_p = int(float(annual_pay / (nominal_rate * math.pow(1 + nominal_rate, periods)
                                     / (math.pow(1 + nominal_rate, periods) - 1))))
    return loan_p


def period_calculation(loan_p, monthly_pay, interest):

    nominal_rate = interest / 1200

    number_months = math.log(monthly_pay / (monthly_pay - nominal_rate * loan_p), 1 + nominal_rate)

    months = math.ceil(number_months)

    years = months // 12

    remain_months = months - 12 * years

    if months < 12:
        print(f"It will take {months} months to repay this loan!")

    elif months < 2:
        print(f"It will take {months} month to repay this loan!")

    elif years > 1 and remain_months > 1:
        print(f"It will take {years} years and {remain_months} months to repay this loan!")

    elif years == 1:
        print(f"It will take {years} years and {remain_months} months to repay this loan!")

    elif remain_months == 0:
        print(f"It will take {years} years to repay this loan!")

    return months


def annuity_calculation(loan, periods, interest):
    nominal_rate = interest / 1200

    annuity = math.ceil(float(loan * (nominal_rate * math.pow(1 + nominal_rate, periods))
                              / (math.pow(1 + nominal_rate, periods) - 1)))

    return annuity


def differentiate_pay(loan, periods, interest):

    i = interest / 1200

    total_differentiated = 0

    for m in range(1, periods + 1):
        differentiated = float(loan / periods + i * (loan - (loan * (m - 1)) / periods))

        print(f"Month {m}: payment is {math.ceil(differentiated)}")

        total_differentiated += math.ceil(differentiated)

    print(f"\nOverpayment = {total_differentiated - loan}")


parser = argparse.ArgumentParser(exit_on_error=False)

parser.add_argument('--type', choices=['annuity', 'diff'])
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=int)

args = parser.parse_args()

if args.type is None:
    print('Incorrect parameters')

elif args.type == 'diff' and args.interest is None:
    print('Incorrect parameters')

elif args.type == 'diff' and args.payment is not None:
    print('Incorrect parameters')

elif args.type == 'annuity' and args.interest is None:
    print('Incorrect parameters')

elif args.type == 'annuity':

    if args.principal and args.periods and args.interest:

        annuity_amount = annuity_calculation(args.principal, args.periods, args.interest)

        print(f"Your annuity payment = {annuity_amount}!")

        print(f"Overpayment = {annuity_amount * args.periods - args.principal}")

    elif args.payment and args.periods and args.interest:

        p = loan_principal(args.payment, args.periods, args.interest)
        print(f"Your loan principal = {p}!")
        print(f"Overpayment = {args.payment * args.periods - p}")

    elif args.principal and args.payment and args.interest:

        duration = period_calculation(args.principal, args.payment, args.interest)

        print(f"Overpayment = {args.payment * duration - args.principal}")

elif args.type == 'diff':

    if args.principal is not None and (args.principal < 0 or args.interest < 0 or args.periods < 0):
        print('Incorrect parameters')
        exit()
    differentiate_pay(args.principal, args.periods, args.interest)
