"""
Taproot Witness Weight Calculator
---------------------------------
BIP 341 (Taproot) introduces a more efficient witness structure. 
This script calculates the weight of a Taproot Key-Path spend.
"""

def calculate_taproot_weight(num_inputs, num_outputs):
    # Fixed components (in bytes)
    version = 4
    marker = 1
    flag = 1
    input_count = 1
    output_count = 1
    locktime = 4
    
    # Per Input (Non-witness)
    # TxID (32) + vout (4) + scriptSig length (1) + sequence (4)
    overhead_per_input = 41 
    
    # Per Output (P2TR is 34 bytes + 9 bytes overhead)
    # Value (8) + scriptPubKey length (1) + scriptPubKey (34)
    size_per_output = 43 

    # Witness Data (Taproot Key-Path)
    # Witness stack count (1) + Signature length (1) + Schnorr Sig (64)
    witness_per_input = 66 

    # Calculation based on BIP 141 (SegWit)
    base_size = version + input_count + (overhead_per_input * num_inputs) + output_count + (size_per_output * num_outputs) + locktime
    total_size = base_size + marker + flag + (witness_per_input * num_inputs)
    
    # Weight = (Base Size * 3) + Total Size
    weight = (base_size * 3) + total_size
    vsize = weight / 4

    return weight, vsize

# Example: 1 input, 2 outputs (Payment + Change)
w, v = calculate_taproot_weight(1, 2)

print(f"--- Taproot Efficiency Report ---")
print(f"Transaction Weight: {w} WU")
print(f"Virtual Size (vSize): {v} vBytes")
print(f"Note: Schnorr signatures (64 bytes) are smaller than ECDSA (~72 bytes)!")
