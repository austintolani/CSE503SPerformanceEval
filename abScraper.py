import re
import sys
# Get file name and open file
file = open(sys.argv[1],'r')
text = file.read()

# Parse Values
timeTaken = re.findall("(\d\.\d*)\sseconds",text)
transferRate = re.findall("(\d*\.\d*)\s\[Kbytes/sec\]",text)
prcntServW66 = re.findall("66%\s*(\d*)",text)
requestsPerSecond = re.findall("(\d*\.\d*)\s\[#/sec\]",text)
meanTimePerRequest = re.findall("(\d*\.\d*)\s\[ms\]\s\(mean\)",text)
meanTimePerConcurrentRequest = re.findall("(\d*\.\d*)\s\[ms\]\s\(mean,",text)
# Print Values
# print("Transfer Rate: ",list(map(float, transferRate)))
# print("Time Taken For Tests: ",list(map(float, timeTaken)))
print("80 percent of requests served within: ",list(map(int, prcntServW66)))
# print("Requests per second: ",list(map(float, requestsPerSecond)))
# print("Time per request (mean): ",list(map(float, meanTimePerRequest)))
# print("Time per request (mean, across all concurrent requests): ",list(map(float, meanTimePerConcurrentRequest)))
# Close file
file.close()


