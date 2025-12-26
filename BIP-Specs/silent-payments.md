# Specification: BIP 352 — Silent Payments

![Silent Payments](../assets/silent-payments.png)

## Overview
Silent Payments (BIP 352) enable non-interactive, reusable payment metadata. Unlike traditional addresses, a Silent Payment address allows a sender to derive a unique, one-time-use on-chain address for the receiver without any interaction.

## Technical Mechanics

### 1. Key Pair Differentiation
The receiver provides two public keys:
- **Scan Key:** Used by the receiver to identify payments belonging to them on the blockchain.
- **Spend Key:** Used to authorize the movement of those funds.

### 2. Diffie-Hellman Key Exchange (ECDH)
The sender uses their own private key and the receiver's scan key to derive a **Shared Secret**. This secret is then used to "tweak" the receiver's spend key, creating a unique output address.

### 3. Privacy Benefits
- **No Address Reuse:** Every transaction goes to a different address, even if the same "Silent Address" is used.
- **On-chain Uniformity:** These transactions look like standard Taproot outputs, making them blend in with other network traffic.
