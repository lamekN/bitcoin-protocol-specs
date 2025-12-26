# Specification: The Lightning Network & HTLCs

![Lightning HTLC](../assets/lightning-htlc.png)

## Overview
The Lightning Network is a Layer 2 scaling solution that allows for instant, high-volume micro-payments. It uses **Bidirectional Payment Channels** to move transactions off the main Bitcoin blockchain while maintaining the security of the base layer.

## Technical Mechanics

### 1. Payment Channels (The Pipe)
A channel is a 2-of-2 multisig "anchor" on the blockchain. As shown in the diagram, Alice and Bob can shift the balance slider back and forth infinitely without broadcasting each individual update to the network.

### 2. BIP 199: Hashed Time-Locked Contracts (HTLCs)
HTLCs are the engine that allows payments to be routed safely across multiple hops.
- **Hashlock:** Funds are locked behind a cryptographic puzzle ($Hash(Preimage)$).
- **Timelock:** Provides a fallback expiry. If the payment isn't claimed, the funds revert to the sender.

### 3. Settlement
Only the final state of the "pipe" is broadcast to the Bitcoin network during a **Settlement TX**, drastically reducing on-chain congestion and fees.
