import datetime
from datetime import datetime as dt
from dateutil.relativedelta import relativedelta, TH
import calendar

def lastthurs(months, years):
    # todayte = datetime.datetime.now().date()
    todayte = datetime.date(year = int(years), month = int(months), day = 1)
    cmon = todayte.month
    # cmon = month
    for i in range(1, 6):
        t = todayte + relativedelta(weekday=TH(i))
        if t.month != cmon:
            # since t is exceeded we need last one  which we can get by subtracting -2 since it is already a Thursday.
            t = t + relativedelta(weekday=TH(-2))
            break
    return t.strftime("%d")

def conversion(tokens):
    # input_string = "NFO:NIFTY23SEP19000PE"
    output = []
    for input_string in tokens:

        # Step 1: Remove "NFO:" from the beginning
        input_string = input_string.replace("NFO:", "")

        # Step 2: Check the first letter and extract accordingly
        if input_string[0] == 'N':
            extracted_string_1 = input_string[:5]
            input_string = input_string[5:]
        elif input_string[0] == 'B':
            extracted_string_1 = input_string[:9]
            input_string = input_string[9:]

        # Step 3: Extract the last 2 letters
        extracted_string_2 = input_string[-2:]
        input_string = input_string[:-2]

        # Step 4: Extract the last 5 letters
        extracted_string_3 = input_string[-5:]
        input_string = input_string[:-5]

        # Step 5: Extract the first 2 letters
        extracted_string_4 = input_string[:2]
        input_string = input_string[2:]

        # Step 6: Store the remaining string
        remaining_string = input_string

        # Step 7: Check the length of the remaining string
        if len(remaining_string) == 4:
            extracted_string_5 = remaining_string[:2]
            extracted_string_6 = remaining_string[2:]
            extracted_string_5 = calendar.month_abbr[int(extracted_string_5)]
        elif len(remaining_string) == 3:
            if remaining_string[0].isdigit():
                extracted_string_5 = remaining_string[0]
                extracted_string_6 = remaining_string[1:]
                extracted_string_5 = calendar.month_abbr[int(extracted_string_5)]
            else:
                extracted_string_5 = remaining_string
                extracted_string_6 = lastthurs(dt.strptime(extracted_string_5, '%b').month, extracted_string_4)
        else:
            extracted_string_5 = ""
            extracted_string_6 = remaining_string

        # Printing the extracted strings and the remaining string
        # print("Token name:", extracted_string_1)
        # print("Put/Call:", extracted_string_2)
        # print("Strike Price:", extracted_string_3)
        # print("Year:", extracted_string_4)
        # print("Remaining String:", remaining_string)
        # print("Month:", extracted_string_5)
        # print("Date:", extracted_string_6)
        # print("Last thursday: ", lastthurs())

        if extracted_string_2 == 'PE':
            putcall = "P"
        elif extracted_string_2 == 'CE':
            putcall = "C"

        tokenname = extracted_string_1
        strike = extracted_string_3
        year = extracted_string_4
        month = extracted_string_5
        dates = extracted_string_6

        finalstring = tokenname + dates + str.upper(month) + year + putcall + strike
        output.append(finalstring)

    return output

# print(conversion((["NFO:BANKNIFTY23SEP45100PE", "NFO:NIFTY23SEP19000CE"])))
