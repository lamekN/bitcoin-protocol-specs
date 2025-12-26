"""
Parses raw TX JSON from bitcoin-cli or mempool.
"""
import json

def decode_tx(data):
    txid = data.get('txid')
    vsize = data.get('vsize')
    
    print(f"\nTX: {txid[:12]}...")
    print(f"Size: {vsize} vB")
    
    print("\nInputs:")
    for vin in data.get('vin', []):
        print(f"  - {vin.get('txid')[:8]}...:{vin.get('vout')}")
        
    print("\nOutputs:")
    for vout in data.get('vout', []):
        addr = vout.get('scriptPubKey', {}).get('address', 'OP_RETURN/Unknown')
        print(f"  - {vout.get('value'):.8f} BTC -> {addr}")

# Mock data (Signet P2TR)
mock = {
    "txid": "7b1eabe0209b1fe794124575ef807057c77ada2138ae4fa8d6c4de0398a14f3f",
    "vsize": 141,
    "vin": [{"txid": "3f4fa19803dec4d6a84fae3821da7ac7577080ef75451294e71f9b20e0ab1e7b", "vout": 0}],
    "vout": [
        {"value": 0.45, "scriptPubKey": {"address": "bcrt1p9sz...p9z5"}},
        {"value": 0.049, "scriptPubKey": {"address": "bcrt1qmx..."}}
    ]
}

if __name__ == "__main__":
    decode_tx(mock)
