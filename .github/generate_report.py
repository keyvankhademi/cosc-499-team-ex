#!/usr/bin/env python

# Install with:
# pip install -U --no-cache-dir https://github.com/brandongk-ubco/gitstats/releases/download/v1.1.0/gitstats-1.1.0-py3-none-any.whl

import gitstats
import datetime
import os
import pytz
import pathlib

print("Running with gitstats version: {}".format(gitstats.__version__))

access_token = os.getenv("GIT_ACCESS_TOKEN")
repository = os.getenv("GIT_REPO_NAME")
group_name = os.getenv("GROUP_NAME")
is_two_week = os.getenv("IS_TWO_WEEK")

excluded_users = []

vancouver_tz = vancouver = pytz.timezone('America/Vancouver')
current_date = datetime.datetime.now(tz=vancouver_tz)

SATURDAY_DAY_OF_THE_WEEK = 5 
start_day = datetime.datetime(
    current_date.year,
    current_date.month,
    current_date.year
)

while start_day.weekday() != SATURDAY_DAY_OF_THE_WEEK:
    start_day = start_day - datetime.timedelta(days=1)

if is_two_week is not None:
    start_day = start_day - datetime.timedelta(days=7) 

start = datetime.datetime(
    start_day.year, start_day.month, start_day.day, 0, 0, 0
)
end = current_date

stats = gitstats.report(access_token,
                        group_name,
                        repository,
                        start=start,
                        end=end,
                        excluded_users=excluded_users)

dir_path = pathlib.Path(__file__).parents[0]
output_path = dir_path/"stats_results.md"

with open(output_path,"w+") as f:
    f.write("```\n")
    f.write(stats + "\n")
    f.write("```\n")

print("Done")
