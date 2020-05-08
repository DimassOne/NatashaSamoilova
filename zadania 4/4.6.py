ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
word = ospf_route.split(' ')
wor = """Protocol:        {:10}
Prefix:       {:10}
AD/Metric:       {:10}
Next-Hop:       {:10}
Last update:       {:10}
Outbound Interface: {:10}
"""
print(wor.format(*word))
