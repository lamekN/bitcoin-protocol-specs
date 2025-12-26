import requests

# Recommended fees from mempool.space
API_URL = "https://mempool.space/api/v1/fees/recommended"

def fetch_fees():
    try:
        r = requests.get(API_URL, timeout=5)
        r.raise_for_status()
        res = r.json()
        
        print(f"High: {res['fastestFee']} sat/vB")
        print(f"Med:  {res['halfHourFee']} sat/vB")
        print(f"Low:  {res['hourFee']} sat/vB")
        
    except Exception as e:
        print(f"Network error: {e}")

if __name__ == "__main__":
    fetch_fees()
