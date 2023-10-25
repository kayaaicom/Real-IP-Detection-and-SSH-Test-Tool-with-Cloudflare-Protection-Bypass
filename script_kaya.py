import socket
import threading
import paramiko

def find_real_ips(domain, subdomain, real_ips, checked_ips):
    host = f"{subdomain}.{domain}"
    try:
        ip = socket.gethostbyname(host)
        print(f"Cloudflare Bypass: {host} => {ip}")

        # If this IP address has not been checked before and is not in the list of found IP addresses
        if ip not in checked_ips:
            checked_ips.add(ip)  # Mark IP address as checked
            real_ips.append(ip)  # Add Cloudflare Bypass results to the list

            # Query CNAME record with DNS query
            cname_result = socket.gethostbyname_ex(host)
            cname = cname_result[0]
            if cname != host:
                print(f"CNAME Record: {host} => {cname}")

            # Test SSH using a thread
            ssh_thread = threading.Thread(target=ssh_test, args=(ip,))
            ssh_thread.start()

    except Exception as e:
        print(f"Not found: {host}")

def ssh_test(ip):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=22, timeout=5)
        ssh.close()
        print(f"SSH Connection Successful to {ip}")
    except paramiko.AuthenticationException:
        print(f"SSH Authentication Failed for {ip}")
    except Exception as e:
        print(f"SSH Connection Failed for {ip}")

def main():
    target_domain = input("Enter the target domain (e.g., example.com): ")
    subdomains = [
        'ftp', 'cpanel', 'webmail', 'localhost', 'news', 'resources', 'insights',
        'articles', 'local', 'landing', 'mysql', 'forum', 'direct-connect', 'blog',
        'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin',
        'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin',
        'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5',
        'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure',
        'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support',
        'web', 'dev'
    ]

    real_ips = []  # Create a list to store Cloudflare Bypass results
    checked_ips = set()  # Create a cluster to monitor controlled IP addresses

    for subdomain in subdomains:
        thread = threading.Thread(target=find_real_ips, args=(target_domain, subdomain, real_ips, checked_ips))
        thread.start()

    for thread in threading.enumerate():
        if thread != threading.current_thread():
            thread.join()

    print("\nReal IP Addresses:")
    for ip in real_ips:
        print(f"{ip}")

if __name__ == '__main__':
    main()
