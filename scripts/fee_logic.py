"""
Implicit fee calc. 
Note: Bitcoin fees are the remainder of inputs - outputs.
"""

def get_fee(ins, outs):
    try:
        # handle list of floats or ints
        total_in = sum(float(x) for x in ins)
        total_out = sum(float(x) for x in outs)
        
        fee = total_in - total_out
        if fee < 0:
            raise ValueError("Negative fee: Inputs < Outputs")
        return round(fee, 8)
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Test values from 'Melting Furnace' design
    inputs = [0.5, 0.2, 0.1]
    outputs = [0.75, 0.045]
    
    fee = get_fee(inputs, outputs)
    print(f"Fee: {fee} BTC")
    assert fee == 0.005
