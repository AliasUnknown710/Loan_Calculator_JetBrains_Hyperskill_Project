import math
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--principal")
    parser.add_argument("--payment")
    parser.add_argument("--periods")
    parser.add_argument("--interest")
    parser.add_argument("--type")

    args = parser.parse_args()

    t = args.type

    interest = float(args.interest) if args.interest else None
    P = float(args.principal) if args.principal else None
    A = float(args.payment) if args.payment else None
    n = int(args.periods) if args.periods else None

    invalid = False

    if t not in ("annuity", "diff"):
        invalid = True

    if interest is None:
        invalid = True

    for v in (P, A, n, interest):
        if v is not None and v < 0:
            invalid = True

    if t == "diff" and A is not None:
        invalid = True

    provided = [t, P, A, n, interest]
    if sum(v is not None for v in provided) < 4:
        invalid = True

    if invalid:
        print("Incorrect parameters")
        exit()

    i = interest / (12 * 100)

    if t == "diff":
        total = 0
        for m in range(1, n + 1):
            Dm = (P / n) + i * (P - (P * (m - 1) / n))
            payment = math.ceil(Dm)
            total += payment
            print(f"Month {m}: payment is {payment}")
        print()
        print(f"Overpayment = {int(total - P)}")
        exit()

    if t == "annuity":

        if n is None:
            n = math.ceil(math.log(A / (A - i * P), 1 + i))

            years = n // 12
            months = n % 12

            if years > 0 and months > 0:
                print(f"It will take {years} years and {months} months to repay this loan!")
            elif years > 0 and months == 0:
                print(f"It will take {years} years to repay this loan!")
            else:
                print(f"It will take {months} months to repay this loan!")

            print(f"Overpayment = {int(A * n - P)}")

        elif A is None:
            A = math.ceil(P * (i * (1 + i) ** n) / ((1 + i) ** n - 1))
            print(f"Your annuity payment = {A}!")
            print(f"Overpayment = {int(A * n - P)}")

        elif P is None:
            P = A / ((i * (1 + i) ** n) / ((1 + i) ** n - 1))
            P_int = int(P)
            print(f"Your loan principal = {P_int}!")
            print(f"Overpayment = {int(A * n - P_int)}")

        else:
            print("Incorrect parameters")