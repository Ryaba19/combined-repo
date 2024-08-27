import sys

def min_moves_to_equal(nums):
    
    nums.sort()
    
    
    median = nums[len(nums) // 2]
    
    
    moves = sum(abs(num - median) for num in nums)
    
    return moves

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python task4.py numbers.txt")
        sys.exit(1)
    
    
    input_file = sys.argv[1]
    with open(input_file, 'r') as file:
        nums = [int(line.strip()) for line in file]
    
    
    result = min_moves_to_equal(nums)
    print(result)
