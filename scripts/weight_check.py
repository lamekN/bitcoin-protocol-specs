"""
Taproot (BIP 341) weight unit calculator for Key-path spends.
vSize = weight / 4
"""

def calc_p2tr_vsize(n_in, n_out):
    # Fixed overhead
    # n_in * (prevout + nSequence) + version + locktime + counts
    base_bytes = (n_in * 41) + 10 
    
    # P2TR Output size (Value + scriptPubKey)
    out_bytes = n_out * 43
    
    # Schnorr sig + control block + witness overhead
    witness_bytes = n_in * 66
    
    total_base = base_bytes + out_bytes
    total_weight = (total_base * 3) + (total_base + witness_bytes + 2)
    vsize = total_weight / 4
    
    return total_weight, vsize

if __name__ == "__main__":
    # Standard 1-in, 2-out TX
    weight, vsize = calc_p2tr_vsize(1, 2)
    print(f"Weight: {weight} WU | vSize: {vsize} vB")
