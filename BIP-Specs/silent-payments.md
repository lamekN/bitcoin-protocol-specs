# Specification: BIP 352 — Silent Payments (Non-Interactive Privacy)

![Silent Payments](../assets/silent-payments.png)

## Overview
Silent Payments (BIP 352) solve the problem of public address reuse. They allow a sender to generate a unique, one-time-use address for a receiver without requiring any back-and-forth communication.

## Technical Mechanics

### 1. Elliptic Curve Diffie-Hellman (ECDH)
The core of the "Invisible Handshake" is the Shared Secret ($S$).
- **Sender (Alice):** Derives $S$ using her private key ($a$) and Bob’s public Scan Key ($B_{scan}$).
- **Formula:** $S = a \cdot B_{scan}$

### 2. Dual-Key System
Bob maintains two distinct keys to enhance security:
- **Scan Key ($B_{scan}$):** Used to monitor the blockchain and identify incoming payments by reconstructing the shared secret.
- **Spend Key ($B_{spend}$):** Required to actually sign and move the funds.

### 3. Privacy Impact
Because the unique silent address is derived mathematically by the sender, it never appears in any public registry or on-chain until the transaction is broadcast. This provides "on-chain uniformity," making these transactions indistinguishable from standard Taproot spends.
