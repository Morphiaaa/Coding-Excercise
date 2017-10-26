
import collections

class FileOwners:

    @staticmethod
    def group_by_owners(files):
    	res = collections.defaultdict(list)
    	for key,value in files.items():
    		res[value].append(key)

    	return res


files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}
print(FileOwners.group_by_owners(files))