from client import ApiRateLimitThrottlingGovernorClient

def main():
    client = ApiRateLimitThrottlingGovernorClient()
    res = client.govern_request("client_app_102", 1)
    print(f"Allowed: {res['allowed']}")
    print(f"Remaining Tokens: {res['remaining_tokens']} (Reset in {res['reset_in_seconds']}s)")

if __name__ == "__main__":
    main()
