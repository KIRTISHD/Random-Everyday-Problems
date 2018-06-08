#When jump limit given
def stairway_dp(n,x):
	if n==0: 
		return 1
	nums = [0]*(n+1)
	nums[0]=1
	for i in range(1,n+1):
		total = 0
		for j in x:
			if i-j >= 0:
				total += nums[i-j]
		nums[i] = total
        print(nums)
	return nums[n]

# When no particular step limit given
def stair_dp(n):
    if n==0 or n==1: return 1
    nums = [0]*(n+1)
    nums[0] = 1
    nums[1] = 1
    for i in range(2,n+1):
        nums[i]=nums[i-1] + nums[i-2]
    return nums[n]
	
if __name__=="__main__":
	no_of_staircase = 4
	no_of_jumps =  [1,3,5]
	no = stair_dp(no_of_staircase)
	print(no)
	no = stairway_dp(no_of_staircase,no_of_jumps)
	print(no)
