# Sending the transaction
$ bitcoin-cli -regtest sendtoaddress "bcrt1qmx7890..." 10.5
7b1eabe0209b1fe794124575ef807057c77ada2138ae4fa8d6c4de0398a14f3f

# Checking the mempool for our TXID
$ bitcoin-cli -regtest getmempoolentry 7b1eabe0209b1fe794124575ef807057c77ada2138ae4fa8d6c4de0398a14f3f
{
  "vsize": 141,
  "weight": 561,
  "fee": 0.00002820,
  "confirmations": 0
}
