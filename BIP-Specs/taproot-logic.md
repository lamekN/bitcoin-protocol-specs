# Specification: BIP 341 (Taproot) & MAST

![Taproot Logic](../assets/taproot-logic.png)

## Overview
Taproot introduces a way to collapse complex spending conditions into a single Public Key ($Q$). This improves privacy by making complex "Smart Contracts" look like simple single-signature transactions on the blockchain.

## Technical Components

### 1. MAST (Merkle Alternative Script Trees)
- Individual spending scripts are hashed into a binary tree.
- Only the specific script used for spending is revealed, keeping other conditions private and saving block space.

### 2. Key Tweaking
- The **Internal Key ($P$)** represents the "cooperative" path (where all parties agree).
- The **Merkle Root ($m$)** is committed to the key via a tweak.
- The final **Output Key ($Q$)** is what appears on the ledger. 

### 3. Benefits
- **Privacy:** Observers cannot tell if a transaction was a simple payment or a complex multi-party contract.
- **Scalability:** Large scripts no longer take up massive amounts of data on-chain.
