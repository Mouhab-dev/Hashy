'''
This program is created by Mouhab-dev
Github: https://www.github.com/Mouhab-dev
'''
from sys import exit
import argparse
import hashlib as h

# colored output
CRED = '\033[91m'
CBLUE = '\033[94m'
CGREEN = '\033[92m'
CEND = '\033[0m'

def hash_file(filepath, args):
    # buffer size that would load a part of the file into memory to hash it
    # the bigger the buffer size the faster the hashing process but with more memory usage
    BLOCK_SIZE = 65536 # buffer size is 64kb

    switcher = {
        "md5": h.md5(),
        "sha1": h.sha1(),
        "sha224": h.sha224(),
        "sha256": h.sha256(),
        "sha384": h.sha384(),
        "sha512": h.sha512(),
        "sha3_224": h.sha3_224(),
        "sha3_256":h.sha3_256(),
        "sha3_384": h.sha3_384(),
        "sha3_512": h.sha3_512(),
        "blake2b": h.blake2b(),
        "blake2s": h.blake2s()
    }

    try:
        with open(filepath, 'rb') as f: # Open the file to read its bytes
            print(CBLUE + f"Hashing file: {filepath} ..." + CEND)
            hash_list=[] # list to store hash values for each hash function
            reader = f.read(BLOCK_SIZE) # Read from the file with block size of 65536

            while len(reader) > 0: # While we did not reach the end of the file
                for i in range(len(args)):
                    file_hash = switcher.get(args[i])
                    file_hash.update(reader) # Update the hash with new bytes
                    hash_list.append("")
                    hash_list[i] = file_hash.hexdigest()
                reader = f.read(BLOCK_SIZE) # Read the next block from the file
    except IOError or FileNotFoundError:
        print(f"No such file or directory: {filepath}")
        exit(5)

    return hash_list

def hash_print(hashlist_f, args_hf, hashlist_s = [], cf = False ,filename=""):
    
    if cf == True :
        if hashlist_f != hashlist_s:
            hash_print(hashlist_f, args_hf, filename=args.cf[0])
            hash_print(hashlist_s, args_hf, filename=args.cf[1])
            print()
            print(CRED + "The Two Files Mismatches" + CEND)
        else:
            hash_print(hashlist_f, args_hf)
            print()
            print(CGREEN + "The Two Files Matches" + CEND)
    else:
        print()
        print('{:<19s}{:>20s}'.format("Algorithm:", f"Hash value: {filename}"))
        print('{:<19s}{:>20s}'.format("------------", "--------------------------------------"))
        for i in range(len(args_hf)):
            print('{:<19s}{:>30s}'.format(args_hf[i], hashlist_f[i]))

if __name__ == "__main__":
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description = "Hashy is a CLI program to hash files, compare two files (integrity check), strings.",
                                    epilog="Find me on Github: https://www.github.com/Mouhab-dev")

    # Create a mutually exclusive group of arguments where one of them is required
    group = parser.add_mutually_exclusive_group(required=True)
    # -v/--version argumment for version display
    parser.add_argument('-v','--version', action='version', version='Hashy current version: v1.0', help="display current version of Hashy")
    # -hf argument description
    parser.add_argument("-hf", metavar="MD5:SHA1:blake2b", type=str, help="the required hash function.", required=True, 
                        nargs="+", choices=['sha512', 'sha3_256', 'md5', 'sha3_224', 'sha1', 'blake2s', 'sha3_512', 'sha256', 'blake2b', 'sha224', 'sha384', 'sha3_384'])
    # -cf argument description
    group.add_argument("-cf", metavar="<file path>", type=str, nargs=2,
                        help="check hash of two files for a match using the provided hash function.")
    # -f argument description
    group.add_argument("-f", metavar="<file path>", type=str, nargs=1,
                        help="calculate hash for a file using the provided hash function.")
    # -s argument description
    group.add_argument("-s", metavar='"String"', type=str,
                        help='calculate hash for a string using the provided hash function (string inside " " is recommended).')

    args = parser.parse_args()

    if args.cf != None :
        # call hash_file function on (file 1), returns a list of hash values
        hash_list1 = hash_file(args.cf[0], args.hf)

        # call hash_file function on (file 2), returns a list of hash values
        hash_list2 = hash_file(args.cf[1], args.hf)

        # check for match or mismatch then display the hash value of each file
        hash_print(hash_list1, args.hf, hash_list2, True)

        # exit successfully
        exit(0)

    elif args.f != None :
        # call hash_file function, returns a list of hash values
        hash_list = hash_file(args.f[0], args.hf)

        # call hash_print function to display each hash value the user has requested
        hash_print(hash_list, args.hf, filename = args.f[0])

        print()
        print(CGREEN + "Process Finished" + CEND)

        # exit successfully
        exit(0)

    elif args.s != None :

        switcher = {
            "md5": h.md5(args.s.encode('utf-8')).hexdigest(),
            "sha1": h.sha1(args.s.encode('utf-8')).hexdigest(),
            "sha224": h.sha224(args.s.encode('utf-8')).hexdigest(),
            "sha256": h.sha256(args.s.encode('utf-8')).hexdigest(),
            "sha384": h.sha384(args.s.encode('utf-8')).hexdigest(),
            "sha512": h.sha512(args.s.encode('utf-8')).hexdigest(),
            "sha3_224": h.sha3_224(args.s.encode('utf-8')).hexdigest(),
            "sha3_256":h.sha3_256(args.s.encode('utf-8')).hexdigest(),
            "sha3_384": h.sha3_384(args.s.encode('utf-8')).hexdigest(),
            "sha3_512": h.sha3_512(args.s.encode('utf-8')).hexdigest(),
            "blake2b": h.blake2b(args.s.encode('utf-8')).hexdigest(),
            "blake2s": h.blake2s(args.s.encode('utf-8')).hexdigest()
        }

        print(CBLUE + "Hashing string ..." + CEND)
        print()
        print('{:<1s}{:>20s}'.format("Algorithm:", "Hash value:"))
        print('{:<19s}{:>20s}'.format("------------", "--------------------------------------"))

        # calculate each hash value the user has requested
        for i in range(len(args.hf)):
            m = switcher.get(args.hf[i])
            print("{:<19s}{:>30s}".format(args.hf[i], m))

        print()
        print(CGREEN + "Process Finished" + CEND)

        # exit successfully    
        exit(0)
