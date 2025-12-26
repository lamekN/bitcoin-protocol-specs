"""
Bitcoin Raw Transaction Decoder
-------------------------------
A utility to parse raw transaction hex into a human-readable format.
"""

import json

def human_readable_tx(raw_json):
    """
    Parses the messy JSON output from a node into a clean summary.
    """
    txid = raw_json.get("txid")
    vsize = raw_json.get("vsize")
    
    print(f"\n--- Transaction Audit: {txid[:10]}... ---")
    print(f"Virtual Size: {vsize} vBytes")
    
    print("\nInputs (Spending):")
    for vin in raw_json.get("vin", []):
        print(f"  - From Tx: {vin.get('txid')[:8]}... Output index: {vin.get('vout')}")
        
    print("\nOutputs (Receiving):")
    for vout in raw_json.get("vout", []):
        addr = vout.get("scriptPubKey", {}).get("address", "Unknown/OP_RETURN")
        value = vout.get("value")
        print(f"  - {value:.8f} BTC -> {addr}")

# --- Example Raw Hex (A real P2TR/Taproot spend) ---
# In a real environment, you would get this via 'bitcoin-cli getrawtransaction <txid>'
mock_tx_data = {
    "txid": "7b1eabe0209b1fe794124575ef807057c77ada2138ae4fa8d6c4de0398a14f3f",
    "vsize": 141,
    "vin": [{"txid": "3f4fa19803dec4d6a84fae3821da7ac7577080ef75451294e71f9b20e0ab1e7b", "vout": 0}],
    "vout": [
        {"value": 0.45, "scriptPubKey": {"address": "bcrt1p9sz4z7p5v5ky8x8m9z5yq7p9z5yq7p9z5yq7p9z5yq7p9z5yq7p9z5yq7p"}},
        {"value": 0.0499, "scriptPubKey": {"address": "bcrt1qmx7890..."}} # Change
    ]
}

if __name__ == "__main__":
    print("Decoding raw transaction data...")
    human_readable_tx(mock_tx_data)
