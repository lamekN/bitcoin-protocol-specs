# Terminal Session: Bitcoin Core Regtest Operations
**Date:** 2025-12-26  
**Host:** local-dev-node  
**Build:** Bitcoin Core v28.0.0

```console
# Starting the daemon with a fallback fee to avoid 'Fee estimation failed' errors
$ bitcoind -regtest -daemon -fallbackfee=0.0002
Bitcoin server starting

# Creating my first dev wallet
$ bitcoin-cli -regtest createwallet "dev_wallet"
{
  "name": "dev_wallet",
  "warning": ""
}

# Generating a Taproot address (bech32m)
$ bitcoin-cli -regtest getnewaddress "funding_addr" "bech32m"
bcrt1p9sz4z7p5v5ky8x8m9z5yq7p9z5yq7p9z5yq7p9z5yq7p9z5yq7p9z5yq7p

# Mining 101 blocks to ensure coinbase maturity (need 100 blocks depth to spend)
$ bitcoin-cli -regtest generatetoaddress 101 bcrt1p9sz4z7p5v5ky8x8m9z5yq7p9z5yq7p9z5yq7p9z5yq7p9z5yq7p9z5yq7p
[
  "694030f8638318c8c54054515ec716159edc494b14234885deb48f294b75a2fe",
  ... (100 more hashes omitted for brevity)
]

# Verifying balance (Should be 50 BTC from the first block reward)
$ bitcoin-cli -regtest getbalance
50.00000000

# Sending a test payment to a legacy address
$ bitcoin-cli -regtest sendtoaddress "mwpKJNJ4UZL7yFyj53RSVcwauGAK84UvV2" 10.5
7b1eabe0209b1fe794124575ef807057c77ada2138ae4fa8d6c4de0398a14f3f

# Checking unconfirmed transactions in the mempool
$ bitcoin-cli -regtest getmempoolinfo
{
  "loaded": true,
  "size": 1,
  "bytes": 141,
  "usage": 480,
  "total_fee": 0.00002820,
  "maxmempool": 300000000,
  "mempoolminfee": 0.00000000,
  "minrelaytxfee": 0.00001000
}
