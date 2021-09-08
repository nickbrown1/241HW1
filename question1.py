class HW1Q1:

    def timeConvert(input_second):
        days=0
        hours=0
        mins=0
        second=0
        x=0
        y=0
        if input_second>86400:
            days = int(input_second/86400)
            x = input_second - days * 86400
            hours = int(x/3600)
            y = x - hours * 3600
            mins = int(y / 60)
            second = y - mins * 60
            print(days,"day", hours, "hours", mins, "minutes", second,"seconds")
        elif input_second>=3600:
            hours = int(input_second/3600)
            y = input_second- hours * 3600
            mins = int(y / 60)
            second = y - mins * 60
            print(hours, "hours", mins, "minutes", second, "seconds")
        elif input_second>60:
            mins = int(input_second/60)
            second = input_second-mins*60
            print(mins, "minute", second, "seconds")

    w = input("input seconds?")
    timeConvert(int(w))
