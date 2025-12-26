# Specification: The UTXO Ledger Model

![UTXO Model](../assets/utxo-model.png)

## Overview
Bitcoin operates on an **Unspent Transaction Output (UTXO)** model rather than an account-balance system. To execute a payment, specific "pieces" of bitcoin (outputs from previous transactions) are gathered as inputs and "melted down" to create new outputs.

## Technical Mechanics

### 1. Atomic Consumption
Every input used in a transaction must be spent in its entirety. If the total value of your inputs exceeds the amount you wish to pay, the protocol creates a **Change Address** to return the surplus to your wallet.

### 2. Transaction Integrity
- **Inputs:** References to existing UTXOs verified by cryptographic signatures.
- **Outputs:** New UTXOs locked to the recipient's public key hash (or script).
- **The Equation:** $\sum Inputs = \sum Outputs + Miner Fee$

### 3. Implicit Miner Fees
Fees are not explicitly declared in the transaction data. Instead, they are the difference between the total input value and the total output value. In the illustrated example:
- **Total Input:** 0.8 BTC
- **Total Output:** 0.795 BTC
- **Resulting Fee:** 0.005 BTC
