import subprocess
import json

def send_request(url):
    try:
        result = subprocess.run(
            ['curl', '-s', '-w', '%{http_code}', '-o', 'response.txt', url],
            capture_output=True, text=True
        )

        status_code = result.stdout[-3:]

        with open('response.txt', 'r') as file:
            response_body = file.read()
        return response_body, int(status_code)
    except json.JSONDecodeError:
        return None, None

def check_response(response, key):
    return key in response

def main():
    base_url = 'https://jsonplaceholder.typicode.com'
    endpoints = ['/users/1', '/posts/1', '/comments/1']
    
    keys = []
    keys.append(['id', 'name', 'username', 'email'])
    keys.append(['id', 'title', 'userId', 'body'])
    keys.append(['id', 'name', 'postId', 'body', 'email'])

    for i, endpoint in enumerate(endpoints):
        url = base_url + endpoint
        response, status_code = send_request(url)
        if response is not None and status_code == 200:
            status_checks = [check_response(response, key) for key in keys[i]]
            if all(status_checks):
                print(f"Test {i+1}: PASSED")
            else:
                print(f"Test {i+1}: FAILED - Missing keys in response")
        else:
            print(f"Test {i+1}: FAILED - Invalid JSON response")

if __name__ == "__main__":
    main()
