import requests
import sys

# mempool.space is the standard for most dev tools
URL = "https://mempool.space/api/v1/fees/recommended"

def get_fees():
    try:
        r = requests.get(URL, timeout=5)
        r.raise_for_status()
        data = r.json()
        
        print("\n[mempool.space] Current Sat/vB")
        print(f"  Fast: {data['fastestFee']}")
        print(f"  Med:  {data['halfHourFee']}")
        print(f"  Low:  {data['hourFee']}")
        print(f"  Min:  {data['minimumFee']}")
        
    except Exception as e:
        print(f"![Error] API unreachable: {e}")
        sys.exit(1)

if __name__ == "__main__":
    get_fees()
