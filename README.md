# cryptcommsim_py
Simulating real time encrypted communication between clients and server using python socket and ssl modules.

Client and server simulated using SSH between 2 remote laptops. Server Program can also be deployed to 
cloud based application to replicate real environments.

SSL Certificates created using OpenSSL - self signed digital keychain using following UNIX/ LINUX Terminal commands :  
SERVER CERTIFICATE : openssl req -x509 -newkey rsa:4096 -keyout serverkey.pem -out servercert.pem -days 3650

CLIENT CERTIFICATE : openssl req -x509 -newkey rsa:4096 -keyout clientkey.pem -out clientcert.pem -days 3650

->   Public Key Certificate format  X.509
->   Encryption Symmetric Algorithm used : RSA - 4096 bit [Private + Public] keys
->  -days 3650 : Duration of certificate validity [10 years]

Refer https://docs.python.org/3/library/ssl.html#exceptions for further SSL/TSL functions and error handling
