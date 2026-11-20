#!/usr/bin/env python3
"""CloudByte Ops Reporter: summarise CloudByte's activity from the command line."""

def main():
    print("CloudByte Access Report")
    with open("cloudbyte_access.log") as files:
        totalLogs = files.readlines()  #Gives me the total lines from log file
        firstLog_time = totalLogs[0].split()[0].split("T")
        lastLog_time = totalLogs[-1].split()[0].split("T")
        print(f"{len(totalLogs)} events from {firstLog_time[0]} {firstLog_time[1]} to {lastLog_time[0]} {lastLog_time[1]} \n")
        for log in totalLogs:
            fields = log.split()
            date = fields[0][:10]
            time = fields[0][11:]
            print(f"{date} {time}  {fields[1]} {fields[2]}")       

        
# I created this function to achieve the result in different way
def other_way_to_achieve():
    total_logs =[]
    #Storing the each lines into list
    with open("cloudbyte_access.log") as files:
        for log in files:
            total_logs.append(log)

    first_timestamp = total_logs[0].split()[0]
    last_timestamp = total_logs[-1].split()[0] 

    print("CloudByte Access Report")
    print(f"{len(total_logs)} events from {first_timestamp[:10]} {first_timestamp[11:]} to {last_timestamp[:10]} {last_timestamp[11:]}")
    
    for log in total_logs:
        fields = log.split()
        date = fields[0][:10]
        time = fields[0][11:]
        print(f"{date} {time}  {fields[1]} {fields[2]}")


if __name__ == "__main__":
    main()
    #other_way_to_achieve()
