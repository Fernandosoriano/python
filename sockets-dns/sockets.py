# 1.-Find Domain Name From DNS Pointer (PTR)
# Records Using IP Address
# Write a function that takes an IP address and returns the domain
# name using PTR DNS records.
# LINK = https://edabit.com/challenge/MtktG9Dz7z9vBCFYM

def get_domain(ip_address:str) -> str:
    import socket
    """function that receives the ip as a string,
    and returns the name asociated to this ip, the DNS
    (Domain name system)

    Args:
        ip_address (str): The ip string to be searched

    Returns:
        str: the name asociated to the ip
    """   
    name = socket.gethostbyaddr(ip_address)
    return name[0]

# print(get_domain("8.8.8.8"))
# print(get_domain("8.8.4.4"))