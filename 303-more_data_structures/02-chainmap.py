#!/usr/bin/env python3

from collections import ChainMap

my_dict_ver1 = {"app_version": "1", "product": "catalog manager v1"}
my_dict_ver2 = {"app_version": "2", "product": "catalog manager v2"}

cm_ver1 = ChainMap(my_dict_ver1)
cm_ver2 = cm_ver1.new_child(my_dict_ver2)


print("All Versions: ", cm_ver2)

#Latest Version
print("Latest Version: ", 
        cm_ver2.maps[0]
)

#Existing Version
print("Existing Version: ",
        cm_ver2.maps[1]
)


#Print Parent Information
print('Current: ', cm_ver2, '\n','Parent: ', cm_ver2.parents)


# Discard Latest Version and roll back to previous release
cm_ver2.pop("app_version")

print('app_version: ', cm_ver2['app_version'])
print('product: ', cm_ver2['product'])
