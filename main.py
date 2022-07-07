##################### Extra Hard Starting Project ######################
import random
import smtplib
import datetime
import pandas
from random import randint

my_email = "teessssssst1@gmail.com"
password = 7002340553

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
now = datetime.datetime.now()
year = now.year
month = now.month
day = now.weekday()

today = (month, day)

birth = pandas.read_csv("birthdays.csv")

birthdate = {(month, day): data_row for (index, data_row) in birth.iterrows()}

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

if today in birthdate:
    person = birthdate[today]
    path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(path) as file:
        content = file.read()
        content = content.replace("[NAME]", person["name"])

    # 4. Send the letter generated in step 3 to that person's email address.

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="To:teesssst2@yahoo.com\n",
                            msg=f"Happy Birthday \n\n{content}")
