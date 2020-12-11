The series of prime numbers:

```
2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199
```

## cpp
```shell script
g++ cpp/main.cpp -o cpp/is_prime && ./cpp/is_prime
```
> 2.59483 sec


## js
```shell script
node --version  
v15.0.1

node ./js/index.js
```
> 3.266


## go
```shell script
cd ./go && make check

cd ./go && go build -o is_prime && ./is_prime
```
> 7.427660718s


## py
```shell script
python3 ./py/main.py
```
> 59.643482964


## py_numba

```shell script
pip3 install numba
# or 
pip3 install -r ./py_numba/requirements.txt
```


```shell script
python3 ./py_numba/main.py
```
> 5.9623570

## php7
```shell script
php --version

PHP 7.3.11 (cli) (built: Jun  5 2020 23:50:40) ( NTS )
Copyright (c) 1997-2018 The PHP Group
Zend Engine v3.3.11, Copyright (c) 1998-2018 Zend Technologies


php ./php/index.php
```
> 22.418176174164



## php8
```shell script
php8 --version
 
PHP 8.0.0 (cli) (built: Nov 26 2020 17:53:04) ( NTS )
Copyright (c) The PHP Group
Zend Engine v4.0.0-dev, Copyright (c) Zend Technologies
    with Zend OPcache v8.0.0, Copyright (c), by Zend Technologies

/usr/local/Cellar/php/8.0.0/bin/php -dopcache.enable=1 -dopcache.enable_cli=1 -dopcache.jit=1255 -dopcache.jit_buffer_size=100M ./php/index.php
```
> 8.63338804245
