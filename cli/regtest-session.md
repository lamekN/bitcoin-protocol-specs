# Session: regtest tx walkthrough
# setup local bitcoind node for testing BIP341/352 
# date: 2025-12-26

$ bitcoind -regtest -daemon -fallbackfee=0.0001
Bitcoin server starting

# ensure we are on the right chain
$ bitcoin-cli -regtest getblockchaininfo | grep chain
  "chain": "regtest",

# setup dev wallet
$ bitcoin-cli -regtest createwallet "test_wallet"
{
  "name": "test_wallet",
  "warning": ""
}

# need an address for the coinbase reward
$ ADDR=$(bitcoin-cli -regtest getnewaddress "mining_reward" "bech32m")
$ echo $ADDR
bcrt1p9sz4z7p5v5ky8x8m9z5yq7p9z5yq7p9z5yq7p9z5yq7p9z5yq7p9z5yq7p

# mine 101 blocks (100 for maturity + 1 to spend)
$ bitcoin-cli -regtest generatetoaddress 101 $ADDR > /dev/null

# confirm balance
$ bitcoin-cli -regtest getbalance
50.00000000

# prep a spend to bob
$BOB_ADDR="bcrt1qmx7890..." # placeholder$ TXID=$(bitcoin-cli -regtest sendtoaddress $BOB_ADDR 10.5)
$ echo "Sent 10.5 BTC. TXID: $TXID"

# check the raw mempool data
$ bitcoin-cli -regtest getmempoolentry $TXID
{
  "vsize": 141,
  "weight": 561,
  "fee": 0.00002820,
  "descendantcount": 1,
  "ancestorcount": 1,
  "depends": [],
  "spentby": [],
  "bip125-replaceable": true
}

# mine the tx
$bitcoin-cli -regtest generatetoaddress 1 > /dev/null$ bitcoin-cli -regtest gettransaction $TXID | grep confirmations
  "confirmations": 1,
