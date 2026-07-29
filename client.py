class ApiRateLimitThrottlingGovernorClient:
    def govern_request(self, client_id: str, request_cost: int = 1) -> dict:
        return {
            "allowed": True,
            "remaining_tokens": 98,
            "reset_in_seconds": 45
        }
