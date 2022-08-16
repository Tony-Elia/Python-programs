while True:
    def converter(list, type):
        if type == int:
            x = 0
            for x in range(len(list)):
                list[x] = int(list[x])
        elif type == str:
            x = 0
            for x in range(len(list)):
                list[x] = str(list[x])
            
    def print_result(list):    
        converter(list, str)
        print(list[0] + "/" + list[1] + "/" + list[2])

    def limit_upgrader(year, month):
        if year % 4 == 0 and month == 2:
            month_limit = 29
        elif month == 2:
            month_limit = 28
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            month_limit = 31
        else:
            month_limit = 30
        return month_limit

    def add_days():
        year = date[2]
        month = date[1]
        day = date[0]

        try:
            input_days = int(input("Write the days you want to add to the date above: "))
        except:
            print("Invalid input")
            exit()

        if input_days == 0:
            print_result(date)
            exit()
        elif input_days > 0:
            month_limit = 31
            while input_days > 0:
                month_limit = limit_upgrader(year, month)
                day = input_days + day
                if day > month_limit:
                    input_days = day - month_limit - 1
                    day = 1
                    month += 1
                    if month > 12:
                        month = 1
                        year += 1
                else:
                    input_days = 0

            date[2] = year
            date[1] = month
            date[0] = day
        else:
            month_limit = 31
            while input_days < 0:
                month_limit = limit_upgrader(year, month)
                day += input_days
                if day <= 0:
                    input_days = day*-1
                    month -= 1
                    if month < 1:
                        month = 12
                        year -= 1
                    month_limit = limit_upgrader(year, month)
                    day = month_limit
                else:
                    input_days = 0

            date[2] = year
            date[1] = month
            date[0] = day



        print_result(date)

    def count_days():
        end_date = input("Write the end date in form of dd/mm/yyyy: ")
        end_date = end_date.split("/")
        converter(end_date, int)

        year = date[2]
        month = date[1]
        day = date[0]

        end_year = end_date[2]
        end_month = end_date[1]
        end_day = end_date[0]
        
        count = 0
        day_count = 0
        month_count = 0
        year_count = 0
        while day != end_day or month != end_month or year != end_year:
            month_limit = limit_upgrader(year, month)
            day += 1
            count += 1
            day_count += 1

            if day_count > month_limit:
                day_count = 1
                month_count += 1
                if month_count > 12:
                    month_count = 1
                    year_count += 1

            if day > month_limit:
                day = 1
                month += 1
                if month > 12:
                    month = 1
                    year += 1

        print(str(count) + " Day(s) between them")
        print("Or", str(year_count), "Year(s)", str(month_count), "Month(s)", str(day_count), "Day(s) including the start date")
            



    date = input("Write the start date in form of dd/mm/yyyy: ")
    date  = date.split("/")
    i = 0
    converter(date, int)

    response = input("1 => add days for the start date\n2 => count the days between two dates\n")
    if response == "1":
        add_days()
    elif response == "2":
        count_days()
    else:
        print("Invalid input. Write 1 or 2 ONLY")