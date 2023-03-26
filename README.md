# loyality_module

#Description

First version of loyality module uses CSV file to store data (temporary variant for fast start usage). Calculation of free position base on total buyings without comparing privious count, so you can add same count every time and get new free positions.

In plans:
1. Add MongoDB storage. Decition of storage type on start
2. Make classes (client, data which depends on storage type)
3. Make iteration type usage (increment count on every usage)
4. Check current count and compare with previous
5. Make offer every iteraion if have free position