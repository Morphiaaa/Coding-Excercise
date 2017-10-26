# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
class Mask_Information(object):
    def mask_email(self, string):
        string = string.strip()
        pivot = string.find('@')
        domain = string[pivot:]

        start, end = string[0], string[pivot-1]
        return start + '*****' + end + domain
   
    def mask_phone(self, string):
        string = string.strip()
        temp = []
        if string[0] == '+':
            temp.append('+')
        phoneNumber = list(string)
        digits = 0
        for ele in phoneNumber:
            if ele.isdigit():
                digits += 1
        countrynum = digits - 10
        countrynum1 = countrynum
        index = 0
        while index < len(phoneNumber) and countrynum > 0:
            if phoneNumber[index].isdigit():
                countrynum -= 1
                temp.append('*')
            index += 1
        if countrynum1 != 0:
            temp.append('-')
        count = 0
        while index < len(phoneNumber) and count < 3:
            if phoneNumber[index].isdigit():
                temp.append('*')
                count += 1
            index += 1
        temp.append('-')
        count1 = 0
        while index < len(phoneNumber) and count1 < 3:
            if phoneNumber[index].isdigit():
                temp.append('*')
                count1 += 1
            index += 1
        temp.append('-')
        count2 = 0
        while index < len(phoneNumber) and count2 < 4:
            if phoneNumber[index].isdigit():
                temp.append(phoneNumber[index])
                count2 += 1
            index += 1

        return ''.join(temp)

def main():
    m = Mask_Information()
    for line in sys.stdin:
        array = line.split(':')
        if array[0] == 'E':
            print 'E:' + m.mask_email(array[1])
        elif array[0] == 'P':
            print 'P:' + m.mask_phone(array[1])
        
if __name__ == '__main__':
    main()
    