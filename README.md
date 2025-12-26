# ₿itcoin Protocol Specification & Research Log

This repository serves as a technical archive of my research into Bitcoin's core privacy, scalability, and security protocols. My objective is to bridge the gap between high-level cryptographic theory and intuitive visual logic through BIP-focused documentation and logic verification.

---

## 📂 Project Navigation

### 🛡️ Fundamentals
* **[Identity Derivation](./Fundamentals/identity-derivation.md):** A visual breakdown of the one-way mathematical flow from 256-bit entropy to a Native SegWit address via secp256k1 point multiplication.
* **[UTXO Model](./Fundamentals/utxo-model.md):** Analyzing the "Unspent Transaction Output" architecture, focusing on input consumption and implicit miner fee calculation.

### 🏗️ Advanced BIP Specifications
* **[BIP 341: Taproot](./BIP-Specs/taproot-logic.md):** Visualizing Merkle Alternative Script Trees (MAST) and the Key Tweak mechanism where the Output Key $Q$ is derived as $Q = P + h(P||m)G$.
* **[BIP 352: Silent Payments](./BIP-Specs/silent-payments.md):** Documentation of non-interactive privacy schemas and shared secret derivation using Elliptic Curve Diffie-Hellman (ECDH).

### 💻 Functional Logic & Tooling
* **[UTXO Fee Engine](./scripts/utxo_fee_calc.py):** A Python-based verification script that validates the "Melting Furnace" transaction logic used in my technical designs.
