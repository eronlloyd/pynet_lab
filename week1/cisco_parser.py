from ciscoconfparse import CiscoConfParse

cisco_config = CiscoConfParse('cisco_ipsec.txt')

# Crypto map entries and their children
print('1: Find all crypto map entries and their children')
print('-'* 80)
for config_line in cisco_config.find_objects(r"^crypto map CRYPTO"):
    print "{0}: {1}".format(config_line.text, config_line.children)

# Crypto map entries using PFS group2
print('\n2: Find all crypto map entries using PFS group2')
print('-'* 80)
for config_line in cisco_config.find_objects(r"^crypto map CRYPTO"):
    for child in config_line.children:
        # print("Checking '{0}'".format(child.text))
        if "set pfs group2" in child.text:
            print "{0} has matching child with text '{1}' on line {2}".format(
                config_line.text, child.text, child.linenum
            )

# Crypto map entries not using AES
print('\n3: Find all crypto map entries not using AES')
print('-'* 80)
for config_line in cisco_config.find_objects(r"^crypto map CRYPTO"):
    for child in config_line.children:
        # print("Checking '{0}'".format(child.text))
        if "set transform-set" in child.text and "AES" not in child.text:
            print "{0} has matching child with text '{1}' on line {2}".format(
                config_line.text, child.text, child.linenum
            )
