import requests

def get_live_bitcoin_fees():
    """Fetches current recommended fees from mempool.space API"""
    url = "https://mempool.space/api/v1/fees/recommended"
    try:
        response = requests.get(url)
        fees = response.json()
        
        print("--- Live Bitcoin Network Fees (sats/vB) ---")
        print(f"High Priority:   {fees['fastestFee']}")
        print(f"Medium Priority: {fees['halfHourFee']}")
        print(f"Low Priority:    {fees['hourFee']}")
        print(f"Minimum/Purge:   {fees['minimumFee']}")
        
    except Exception as e:
        print(f"Could not connect to network: {e}")

if __name__ == "__main__":
    get_live_bitcoin_fees()
