import os
import requests

with open('domains.txt', 'r') as f:
    domains = [line.strip() for line in f]

with open('results.txt', 'w') as f:
    for domain in domains:
        url = f"http://{domain}"
        response = requests.get(url)
        if response.status_code == 200:
            path = os.path.join(domain, ".svn")
            if os.path.exists(path):
                f.write(f"{domain}/.svn/\n")
                print(f"{domain}/.svn/ directory found.")
            else:
                print(f"{domain}/.svn/ directory not found.")
        else:
            print(f"{domain} returned {response.status_code} status code.")

exit()
