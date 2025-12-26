"""
Basic utility for calculating implicit miner fees.
Bitcoin fees = sum(inputs) - sum(outputs).
"""

def get_implicit_fee(in_vals, out_vals):
    try:
        total_in = sum(float(x) for x in in_vals)
        total_out = sum(float(x) for x in out_vals)
        
        fee = total_in - total_out
        
        if fee < 0:
            raise ValueError("Outputs exceed inputs. Invalid TX.")
            
        return round(fee, 8)
    except Exception as e:
        return f"Error: {e}"

# Test against 'Melting Furnace' design values
if __name__ == "__main__":
    inputs = [0.5, 0.2, 0.1]
    outputs = [0.75, 0.045]
    
    res = get_implicit_fee(inputs, outputs)
    print(f"Calculated Fee: {res} BTC")
    
    # Expected fee for this design is 0.005
    assert res == 0.005, "Logic mismatch"
