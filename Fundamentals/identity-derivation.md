# Specification: Bitcoin Identity Derivation
Image Link: ![Identity Trapdoor](../assets/identity-trapdoor.png)
The "Trapdoor" Table:
Step,Function,Output Size
Entropy,CSPRNG,256 bits
Private Key,Scalar k,256 bits
Public Key,k⋅G,33 bytes (Compressed)
Hash160,RIPEMD160(SHA256(P)),20 bytes
Address,Bech32 (BIP 173),~42 characters
