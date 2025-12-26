# Specification: BIP 341 — Taproot & MAST Logic

![Taproot Logic](../assets/taproot-logic.png)

## Overview
BIP 341 (Taproot) is a major upgrade that improves Bitcoin's privacy, efficiency, and smart contract flexibility. It allows complex spending conditions to be committed to a single Public Key, making them indistinguishable from simple single-sig payments on the blockchain.

## Technical Components

### 1. Merkle Alternative Script Trees (MAST)
As shown in the diagram, different spending conditions (e.g., Multisig or Timelocks) are structured into a binary Merkle Tree. 
- **Efficiency:** Only the path used for spending is revealed, saving significant block space.
- **Privacy:** Unused scripts remain hidden from the public ledger.

### 2. The Key Tweak Mechanism
The core of Taproot is the "tweak." We take an **Internal Key (P)** and add the hash of the **Merkle Root (m)** to it to derive the **Output Key (Q)**.
- **Formula:** $Q = P + H(P|m)G$
- **Result:** $Q$ is a valid Schnorr public key that can be spent either by providing a signature for $P$ (Key Path) or by revealing a script from the tree (Script Path).
