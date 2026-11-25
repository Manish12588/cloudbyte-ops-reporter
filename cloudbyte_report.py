#!/usr/bin/env python3
"""CloudByte Ops Reporter: summarise CloudByte's activity from the command line."""

def get_user(record):
    return record.split()[1]

def get_hours(record):
    return record.split()[0][11:13]

def get_action(record):
    return record.split()[2]

def main():
   
   # Read the log file once
   with open("cloudbyte_access.log") as files:
      records = files.readlines()

   print("CloudByte Access Report")
   firstLog_time = records[0].split()[0].split("T")
   lastLog_time = records[-1].split()[0].split("T")
   print(f"{len(records)} events from {firstLog_time[0]} {firstLog_time[1]} to {lastLog_time[0]} {lastLog_time[1]} \n")

   for record in records:
        fields = record.split()
        date = fields[0][:10]
        time = fields[0][11:]
        print(f"{date} {time}  {fields[1]} {fields[2]}")

   #03 From Listing to Counting
   print()
   user_counts = {}
   for record in records:
      user = record.split()[1]
      user_counts[user] = user_counts.get(user, 0) + 1
 
   user_pairs = count_and_rank(records, get_user)
   print("Most active users")
   for rank, (count, name) in enumerate(user_pairs, start=1):
        print(f"{rank}. {name}: {count} events")

   #04 - Section
   print()
   hour_pairs = count_and_rank(records, get_hours)
   print("Busiest hours")
   for count, hour in hour_pairs:
      print(f"{hour}:00  {count} events")

   print()
   user_actions = count_and_rank(records,get_action)
   print("Activity by type")
   for rank, (count, action) in enumerate(user_actions, start=1):
        print(f"  {rank}. {action}: {count} events")
   



def count_and_rank(records,get_key):
   counts = {}
   for record in records:
        key = get_key(record)
        counts[key] = counts.get(key, 0) + 1
   pairs = []
   for key, count in counts.items():
        pairs.append((count, key))
   #pairs.sort(reverse=True)
   pairs.sort(key=by_count_then_name)
   return pairs

def by_count_then_name(pair):
    """Sort key: busiest first, ties broken A-to-Z by name."""
    count, name = pair          # "name" is whatever was ranked: a username or an hour
    return (-count, name)       # busiest first (negated count), ties A->Z by name

if __name__ == "__main__":
    main() 