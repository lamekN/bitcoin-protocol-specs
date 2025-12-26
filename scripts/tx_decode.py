import json
import sys

def run_decode(tx_data):
    print(f"TXID: {tx_data['txid']}")
    print(f"vSize: {tx_data['vsize']} vB")
    
    # Simple loop for outputs
    for out in tx_data['vout']:
        print(f"  - {out['value']:.8f} BTC -> {out['scriptPubKey']['address'][:15]}...")

# Mock for testing without a node
mock = {
    "txid": "7b1eabe0209b1fe794124575ef807057c77ada2138ae4fa8d6c4de0398a14f3f",
    "vsize": 141,
    "vout": [
        {"value": 10.5, "scriptPubKey": {"address": "bcrt1qmx7890..."}},
        {"value": 0.49997180, "scriptPubKey": {"address": "bcrt1p9sz4z7p..."}}
    ]
}

if __name__ == "__main__":
    run_decode(mock)
