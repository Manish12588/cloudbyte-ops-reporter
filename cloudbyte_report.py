#!/usr/bin/env python3
"""CloudByte Ops Reporter: summarise CloudByte's activity from the command line."""

def get_user(record):
    return record.split()[1]

def get_hours(record):
    return record.split()[0][11:13]

def get_action(record):
    return record.split()[2]

def main():
   
   # 1. Way to read the files
   # with open("cloudbyte_access.log") as files:
   #    records = files.readlines()
   
   #2. Way to read the file
   # records = []
   # with open("cloudbyte_access.log") as f:
   #      for line in f:
   #          records.append(line)
  
   #3. Way to read the files with comprehension
   with open("cloudbyte_access.log") as f:
       records = [line for line in f]
   #records = [ line for line in open("cloudbyte_access.log") ] 
   #print(records)

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
   #Busiest Hours
   print()
   hour_pairs = count_and_rank(records, get_hours)
   print("Busiest hours")
   for count, hour in hour_pairs:
      print(f"{hour}:00  {count} events")

   #Activity By Type
   print()
   user_actions = count_and_rank(records,get_action)
   print("Activity by type")
   for rank, (count, action) in enumerate(user_actions, start=1):
        print(f"  {rank}. {action}: {count} events")

   #Task 2: Most active logins
   print()
   print("Most active logins")
   logins = [ record for record in records if get_action(record) == "login"]
   most_active_login = count_and_rank(logins,get_user)
   #print(most_active_login)
   for rank, (count, user) in enumerate(most_active_login,start=1):
       print(f"{rank}. {user}: {count} events")


   #Task 3: Activity for one user
   print()
   all_actions_records = [ record for record in records if get_user(record) == "alice"]
   action = count_and_rank(all_actions_records,get_action)

   print(f"Activity for {all_actions_records[0].split()[1]}")
   for rank, (count, action) in enumerate(action, start=1):
      print(f"{rank}. {action}: {count} events")

   

def count_and_rank(records,get_key):
   counts = {}
   for record in records:
        key = get_key(record)
        counts[key] = counts.get(key, 0) + 1

   pairs = [ (count, key) for key, count in counts.items()]
   pairs.sort(key=by_count_then_name)
   return pairs

def by_count_then_name(pair):
    """Sort key: busiest first, ties broken A-to-Z by name."""
    count, name = pair          # "name" is whatever was ranked: a username or an hour
    return (-count, name)       # busiest first (negated count), ties A->Z by name

if __name__ == "__main__":
    main() 