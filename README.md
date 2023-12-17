# Stockholm - Malware (Cybersecurity)

>  ⚠️ Important notes  :
> - This project is for educational purposes only.
> - It must be run on a virtual machine or on docker

This program encrypts the contents of target files using `AES-128`.
On success, it add extiontion `.ft` encrypted files.
<img width="669" alt="Capture d’écran 2023-12-17 à 17 03 12" src="https://github.com/mfunyu/Stockholm/assets/60470877/e4b5a91b-607a-44ef-93e6-09245da3ab53">

It will only act on files whose extensions have been targetted by `Wannacry`.

Encrypted files can be restored using the secret key.
<img width="690" alt="Capture d’écran 2023-12-17 à 17 03 33" src="https://github.com/mfunyu/Stockholm/assets/60470877/08b5084f-f1cb-48db-9ca5-37cf3a2b88fe">


## Target Files
This program only targets specific files:
- located inside `$HOME/infection` directory
- have extensions which are listed in `wannacry_file_extensions.txt` file

example
```
$> tree ~/infection
~/infection
├── dir0
│   ├── empty0.docx
│   ├── empty1.docx
│   ├── empty2.docx
│   ├── empty3.docx
│   ├── empty4.docx
│   └── empty5.docx
├── dir1
│   ├── long0.123
│   ├── long1.123
│   └── long2.123
├── dir2
│   ├── test1.txt.ft
│   ├── test2.txt.ft
│   └── test3.txt.ft
├── dir3
├── file1.docx
├── file2.docx
└── no_perm.key
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
