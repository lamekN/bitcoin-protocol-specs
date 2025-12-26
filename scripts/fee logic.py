# Quick check for implicit fees
def get_fee(ins, outs):
    return round(sum(ins) - sum(outs), 8)

if __name__ == "__main__":
    # Data from CLI session
    in_val = [11.0]
    out_val = [10.5, 0.49997180]
    
    fee = get_fee(in_val, out_val)
    print(f"Fee: {fee:.8f}")
    assert fee == 0.00002820
