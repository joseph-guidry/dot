#!/usr/bin/env python3
import dbm
def main():
    file = dbm.open('american_history', 'c')
    file['1812'] = 'War of 1812'
    file['1860'] = 'Civil War'
    file['1898'] = 'Spanish/American War'
    file.close()
    
    # Re-open file and work with its contents
    with dbm.open('american_history', 'c') as file:
        print(file.keys())
        print()
        
        print(file['1898'])
        print(file.get("1775", b"Revolutionary War"))
        print(file['1898'].decode())
        
        print(len(file))
        print(b'1898' in file)
        
        for each_key in file.keys():
            print(each_key.decode(), ":",
                  file[each_key].decode())
if __name__ == "__main__": main()