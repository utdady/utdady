from datetime import date
import calendar


def isprime(n):
    step = 0
    for i in range(2, n + 1):
        if n % i == 0:
            step += 1
    if step == 1:
        return True
    else:
        return False


def main():
    ddate = date.today()
    print("\n\t\t\tBirthDays that are prime!\n")
    print("Select your range (Press enter for DEFAULT values)\n")

    try:
        lo = int(input("Enter lower bound [Year]: "))
    except ValueError:
        lo = 1
    try:
        hi = int(input("Enter upper bound [Year]: "))
    except ValueError:
        hi = ddate.year

    obj = calendar.Calendar()
    done = False

    while not done:
        dob = []
        for year in range(lo, hi+1):
            if isprime(year):
                for month in range(1, 13):
                    if isprime(month):
                        for day in obj.itermonthdays(year, month):
                            if isprime(day):
                                temp = [day,month,year]
                                if len(temp) > 0:
                                    dob.append(temp)
        print(f"\nNumber of birthdays that are prime from year {lo} to {hi}: {len(dob)}")
        io = input("\nDo you want to see the birthdays? [Yes/No]: ")
        if io.upper() in ('YES', 'Y', 'YE', 'YEAH'):
            print(dob)
        oi = input("\nDo you want to check again? [Yes/No]: ")
        if oi.upper() in ('YES', 'Y', 'YE', 'YEAH'):
            done = False
        else:
            done = True
    
                

main()
