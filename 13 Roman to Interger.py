class Solution(object):
    def romanToInt(s):
        """
        :type s: str
        :rtype: int
        """
        rom_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sub_dict = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}

        value = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s):
                if s[i:i + 2] in sub_dict:
                    value += sub_dict[s[i:i + 2]]
                    i += 2
                    continue
            value += rom_dict[s[i]]
            i +=1
        return value

    print(romanToInt(s="IVXLCD"))