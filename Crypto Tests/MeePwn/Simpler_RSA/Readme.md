15 March  by **v4d3r**

## Challenge: Simpler than RSA?
### CTF : MeePwn CTF 2017
Points: 100
Category: RSA

Okay, lets analyse the given files. We have:
        simple.py  -->  the encryption script
        pubkey.txt -->  the modulus and keys used
        enc.txt    -->  the encrypted ciphertext

First look at the `simple.py` and we have two additional arguments provided to us, namely `h` and `g`.
The encryption is such that the ascii of each character of flag is encrypted individually using the same `g` and `h`.
```python
m = [ord(char) for char in FLAG]
c = [encrypt(mi, n, g, h) for mi in m]
```

We are provided with `n`, `h`, `q` and we can easily factorise `n` using factordb to get `p` and `q`.
Further the wierd thing is the description of `n = p*p*q`. We calculate `phi(n)` using Euler's Totient funtion:
phi(n) = phi(p^2) * phi(q)
phi(n) = p * (p-1) * (q-1)

From the ecnryption function, we get to `c = g^m * h^r mod n`
which implies `c = g^m * g^nr mod n`
```python
        c = pow(pow(g, m, n) * pow(h, r, n), 1, n)
```

Now, if we power both sides with `phi(n)`, we would get something like
`c^phi(n) mod n = g^m*phi(n) * g^nr*phi(n) mod n`
but unfortunately, that might turn to `1 = 1 * 1`. So we have to raise the power such that only the term containg the random `r` gets eliminated. One way to get over with it is to power with `(p-1)(q-1)`, resulting in
..*`c^(p-1)(q-1) mod n = g^m(p-1)(q-1) * g^p*p*q*r*(p-1)(q-1) mod n`
..*`c^(p-1)(q-1) mod n = g^m(p-1)(q-1) * g^phi(n)*p*q*r mod n`
..*`c^(p-1)(q-1) mod n = g^m(p-1)(q-1) mod n`


We now have a simplified equation with just m unknown. So work on with bruteforce to get back the message! lol and that just gave away the flag :p

```python
a=(p-1) * (q-1)
flag=""
for i in c:
        for j in range(127):
                if pow(i,a,n)==pow(g,j*a,n):
                        flag+=chr(j)
print flag
```

### FLAG: MeePwnCTF{well_is_fact0rizati0n_0nly_w4y_to_s0lve_it?}



The complete script is here - 
```python
from Crypto.Util.number import *

n=1235280093599323856390922798440377476467763531842392869674688408727824382702235317
g=1110549711091392805024587195974719739929628997819528005374351081843256209971586072
h=610466084395822279908554174354632326166097007218620288020807622478449585661028278
p=1057817919251064684989791981
q=1103935256393984899021164397
with open ("enc.txt") as f:
        c=f.read().strip("\n[]").split()
for i in range(len(c)):
        c[i]=int(c[i].strip("L,"))

# we have c = g^m * h^r mod n
#i.e, c = g^m * g^nr mod n
#now powering both sides with a=(p-1)(q-1) we get to eliminate r as g^nra mod n is 1 [Generates phi(n)] (Eulers Theorem)
#this reduces the equation to c^a mod n = g^ma mod n


a=(p-1) * (q-1)
#now bruteforcing for m, we get the flag

flag=""
for i in c:
        for j in range(127):
                if pow(i,a,n)==pow(g,j*a,n):
                        flag+=chr(j)
print flag
```
