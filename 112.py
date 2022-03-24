from scapy.all import *
import regex

# This will take a hex string and convert to readable ascii

# packets = rdpcap(r"D:///Projecten/EmergencyCalls/112.pcapng")

r = r"(?<=3131322d4d454c44494e47).*?(?=a4)"

test_str = "3131322d4d454c44494e473a20426a6f726e204d634b656e6e61202831333229202d2049732065722065656e20646f6b746572202f20616d62756c616e63696572206265736368696b6261617220696e20686574207a69656b656e687569733fa4"[:-2]

a = regex.findall(r,test_str)

try:
    test = bytes.fromhex(test_str).decode('utf-8')
    print(test)
except:
    print('This will not work')