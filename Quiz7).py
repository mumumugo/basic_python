#Quiz) one report per week. The format as below:
#Format:
#- X week) Weekly Report
#Department:
#Name:
#Summary:

#write a code that can make 1 week to 50 week's report file.
# file name: '1w.txt', '2w.txt','3w.txt',...

for week in range(1,3):
    with open(str(week) + "weekly_report.txt","w", encoding="utf8") as report_file:
        report_file.write("-----{0} week) Weekly Report----". format(week))
        report_file.write("\nDepartment:")
        report_file.write("\nName:")
        report_file.write("\nSummary:")