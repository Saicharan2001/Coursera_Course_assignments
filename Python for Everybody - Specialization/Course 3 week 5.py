from urllib.request import urlopen
import xml.etree.ElementTree as ET

url = input("Enter location: ")
print("Retrieving " + url)

xml = urlopen(url).read()

tree = ET.fromstring(xml)

counts =  tree.findall('.//count')
print("Count: " + str(len(counts)))

accumulator = 0

for count in counts:
    accumulator = accumulator + int(count.text)

print("Sum:" + str(accumulator))