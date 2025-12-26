"""
Parses raw transaction JSON from bitcoin-cli or mempool API.
"""
import json

def parse_tx(data):
    tx_id = data.get('txid', 'N/A')
    vsize = data.get('vsize', 0)
    
    print(f"\nTXID: {tx_id}")
    print(f"vSize: {vsize} vB")
    print("-" * 20)
    
    print("Inputs:")
    for i in data.get('vin', []):
        print(f"  {i.get('txid')[:12]}... [{i.get('vout')}]")
        
    print("\nOutputs:")
    for o in data.get('vout', []):
        spk = o.get('scriptPubKey', {})
        addr = spk.get('address', 'non-standard/OP_RETURN')
        print(f"  {o.get('value'):.8f} -> {addr}")

# Mock data for signet/regtest P2TR spend
raw_data = {
    "txid": "7b1eabe0209b1fe794124575ef807057c77ada2138ae4fa8d6c4de0398a14f3f",
    "vsize": 141,
    "vin": [{"txid": "3f4fa19803dec4d6a84fae3821da7ac7577080ef75451294e71f9b20e0ab1e7b", "vout": 0}],
    "vout": [
        {"value": 0.45, "scriptPubKey": {"address": "bcrt1p9sz4z7p5v5ky8x8m9z5yq7p9z5yq7p9z5yq7p9z5yq7p9z5yq7p9z5yq7p"}},
        {"value": 0.0499, "scriptPubKey": {"address": "bcrt1qmx7890..."}}
    ]
}

if __name__ == "__main__":
    parse_tx(raw_data)
