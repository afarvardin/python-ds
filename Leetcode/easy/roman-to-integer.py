class Solution:
    def __init__(self) -> None:
        self.romanInitials = {
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4,
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
        }

    def romanToInt(self, num_str: str) -> int:
        get_pattern = []
        # num_str = s
        while(num_str != ''):
            for ri in self.romanInitials:
                get_pattern.append(self.romanInitials.get(ri)) if num_str.find(ri) != -1 else 0
                num_str = num_str.replace(ri, '', 1)

        return sum(get_pattern)
    

rti = Solution()

for n in ['MCMXCIV', 'III', 'VI', 'XXIX']:
    print(rti.romanToInt(n))
