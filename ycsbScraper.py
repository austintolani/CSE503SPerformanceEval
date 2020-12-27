import re
import sys
# Get file name and open file
file = open(sys.argv[1],'r')
text = file.read()

# Parse Values
throughput = re.findall(", Throughput\(ops/sec\), (\d*\.\d*)",text)

# Print Values
print("Throughput Values For Inserts:", list(map(float, throughput[0:][::2])))
print("Throughput Values For Updates/Writes:", list(map(float, throughput[1:][::2])))
# Close file
file.close()


