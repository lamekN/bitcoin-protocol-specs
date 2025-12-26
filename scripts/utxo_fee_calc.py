# Bitcoin UTXO Fee Calculator
# Validating the logic of the 'Melting Furnace' design

def calculate_miner_fee(inputs, outputs):
    total_input = sum(inputs)
    total_output = sum(outputs)
    
    # In Bitcoin, the fee is the implicit remainder
    fee = total_input - total_output
    
    return round(fee, 8)

# Data from technical design:
utxo_inputs = [0.5, 0.2, 0.1]  # 0.8 BTC Total
destination_payment = 0.75
change_amount = 0.045
utxo_outputs = [destination_payment, change_amount]

actual_fee = calculate_miner_fee(utxo_inputs, utxo_outputs)

print(f"--- UTXO Furnace Logic Check ---")
print(f"Total Input:  {sum(utxo_inputs)} BTC")
print(f"Total Output: {sum(utxo_outputs)} BTC")
print(f"Implicit Fee: {actual_fee} BTC")

# Verification against design
if actual_fee == 0.005:
    print("✅ Logic matches technical design specification!")
else:
    print("❌ Fee mismatch. Check input/output values.")
