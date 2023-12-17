# Stockholm - Malware (Cybersecurity)

>  ⚠️ Important notes  :
> - This project is for educational purposes only.
> - It must be run on a virtual machine or on docker

This program encrypts the contents of target files using `AES-128`.
On success, it add extiontion `.ft` encrypted files.

It will only act on files whose extensions have been targetted by `Wannacry`.

Encrypted files can be restored using the secret key.


## Target Files
This program only targets specific files:
- located inside `$HOME/infection` directory
- have extensions which are listed in `wannacry_file_extensions.txt` file
```
ls -R ~/infection
```

## Usage

```
usage: stockholm.py [-h] [-v] [-r KEY] [-s]

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show the version of the program
  -r KEY, --reverse KEY
                        reverse the infection using the key
  -s, --silent          the program will not produce any output
```

- run
  ```
  ./stockholm.py 
  ```

### Requirements

```
$> pip freeze
pycryptodome==3.19.0
```

## References

- JA
  - https://eset-info.canon-its.jp/malware_info/special/detail/230914.html
