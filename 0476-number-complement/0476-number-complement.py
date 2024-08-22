class Solution:
    def findComplement(self, num: int) -> int:
        # Step 1: Get the number of bits in the binary representation of num
        bit_length = num.bit_length()
        
        # Step 2: Create a mask with all bits set to 1 for the length of the binary number
        mask = (1 << bit_length) - 1
        
        # Step 3: XOR the number with the mask to flip the bits
        return num ^ mask
