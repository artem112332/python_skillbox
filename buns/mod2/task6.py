site_name = input()
domain = ''
while True:
    if len(site_name) > 0:
        char = site_name[0]
        if char != '.':
            domain += char
            site_name = site_name[1::]
        else:
            print(domain)
            site_name = site_name[1::]
            domain = ''
    else:
        print(domain)
        break
