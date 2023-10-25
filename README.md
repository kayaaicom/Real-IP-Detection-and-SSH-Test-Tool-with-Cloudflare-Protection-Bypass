main functions of the script:

find_real_ips function: Attempts to find the real IP address for a given subdomain.<br>
ssh_test function: Attempts to establish an SSH connection to the found IP address.<br>
main function: Gets the target domain from the user and tries to find the real IP addresses for a large number of possible subdomains.<br>


<h1>Cloudflare Bypass Scripts</h1>
This script is used to detect the real IP addresses of websites behind Cloudflare protection. Cloudflare is a popular tool for protecting websites from various threats, but using this script the real IP addresses of some subdomains can be detected.

<h3>How does it work?</h3>
1- The script tries to find real IP addresses by making DNS queries on common subdomains.<br>
2- Once an IP address is found, it tries to establish an SSH connection to that IP address.<br>
3- If the connection is successful, it is assumed that this IP address may belong to the real server.<br>

<h3>Usage:</h3><br>

      python script_name.py
You will then be asked to enter the target domain. For example: example.com

Note: Since the intended use could be bad, the code has been fixed and some restrictions have been introduced. Please use the tools in good faith for pentesting and hope to become a white hat hacker!<br><br>
Please use this script only for good purposes and do not create any illegal activity. This script is designed to find the real ip addresses of fake websites and collect information about them and report them to the hosting provider.

#Cloudflare Bypass
#IP Detection
#SSH Test
#DNS Query
#Subdomain
#Server Protection
#Security
#Connection Control
#CF Bypass
