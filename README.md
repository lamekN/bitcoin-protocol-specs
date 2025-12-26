Bitcoin Protocol Research & Tooling
Technical workspace for the ₿OSS 2026 application. This repository contains protocol verification scripts, Bitcoin Core PR reviews, and local regtest simulation logs.

Project Structure
cli/: Raw terminal logs from bitcoin-cli sessions. Includes wallet initialization, UTXO management, and P2TR (Taproot) transaction construction.

scripts/: Python-based utility scripts for protocol math.

fee_logic.py: Verification of implicit miner fees.

weight_check.py: BIP-341 weight unit and vSize calculations.

tx_decode.py: Local parser for raw transaction hex/JSON.

analysis/: Cross-verification reports. This folder contains the results of running scripts/ against cli/ data to ensure theoretical models match node behavior.

docs/: Technical breakdowns of BIPs (341, 352, 141) and Lightning Network specifications.

reviews/: Deep dives and peer reviews of specific Bitcoin Core Pull Requests.

Featured Analysis: Taproot vSize Audit
I developed a suite of tools to verify the fee efficiency of Taproot Key-path spends.

The Workflow:

Created a P2TR transaction in a local regtest environment.

Exported the raw transaction data.

Used scripts/weight_check.py to predict the weight.

Validated the prediction against the node's getmempoolentry output.

Result: Confirmed 141 vB for a standard 1-in, 2-out spend, verifying the 64-byte Schnorr signature footprint.
Usage (Local Dev)
To run the fee verification script:

Bash

python3 scripts/fee_logic.py
To audit a raw transaction JSON:

Bash

python3 scripts/tx_decode.py cli/raw_tx.json
Goals
Contribute to Bitcoin Core through technical peer review.

Develop localized tools for the African Bitcoin ecosystem.

Deepen understanding of L2 scaling solutions (Lightning, Ark).
