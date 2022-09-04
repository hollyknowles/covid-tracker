import requests


def edit_date_format(date):
    """ Inputs a string of any of these formats: DD/MM/YY, DD/MM/YYYY, DD-MM-YY, DD-MM-YY, DD.MM.YY, DD.MM.YYYY
        and outputs in the format: Month, Day, Year.
        e.g. '21/06/20' becomes 'Jan, 21 2020' """

    if "/" in date:
        split_list = date.split("/")
    elif "-" in date:
        split_list = date.split("-")
    elif "." in date:
        split_list = date.split(".")
    else:
        return  # input incorrectly formatted

    day = split_list[0]
    month = split_list[1]
    year = split_list[2]

    # App is about covid data so all years will be 20XX (ie no 19XX)
    if len(year) == 2:
        year = '20' + year
        split_list[2] = year

    # API accepts month as short name not number
    month = change_month_format(month)
    split_list[1] = month

    # Concatenate and add spaces/comma
    output_string = month + " " + day + ", " + year

    return output_string


def change_month_format(month):
    if month == "1" or month == "01":
        return "Jan"
    elif month == "2" or month == "02":
        return "Feb"
    elif month == "3" or month == "03":
        return "Mar"
    elif month == "4" or month == "04":
        return "Apr"
    elif month == "5" or month == "05":
        return "May"
    elif month == "6" or month == "06":
        return "Jun"
    elif month == "7" or month == "07":
        return "Jul"
    elif month == "8" or month == "08":
        return "Aug"
    elif month == "9" or month == "09":
        return "Sep"
    elif month == "10":
        return "Oct"
    elif month == "11":
        return "Nov"
    elif month == "12":
        return "Dec"


async def get_data(country, date):
    """ This function gets the covid case data from the Worldometer website """
    url = "https://worldometer-covid-19.p.rapidapi.com/GetCovidStats"

    querystring = {"countrycode": country, "date": date}

    headers = {
        "X-RapidAPI-Key": "4819b2c789mshbc8dc710537c61ep1313d1jsn2ecb830ed7ba",
        "X-RapidAPI-Host": "worldometer-covid-19.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring).json()
    print(response)
    return response


def get_date(response):
    return response["date"]


def get_country(response):
    return response["country"]


def get_new_cases(response):
    return response["new_cases"]


def get_total_cases(response):
    return response["total_cases"]


def get_new_deaths(response):
    return response["new_deaths"]


def get_total_active_cases(response):
    return response["total_active"]


def get_last_updated(response):
    return response["last_updated"]


def format_data():
    """ could format into a pretty infographic card or graph rather than the bot reply with just text"""
    pass

# example response when country = "us", date = "Aug 15, 2021"
# {
# "date": "Aug 15, 2021",
# "country": "USA",
# "newcases": "112206", "totalcases": "37996484",
# "newdeaths": "937", "totaldeaths": "647021",
# "totalactive": "2970753", "lastupdated": "September 04, 2022, 03:40 GMT"
# }
