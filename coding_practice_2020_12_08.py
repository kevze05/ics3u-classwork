def first_last6(nums):
  if nums[0] == 6 or nums[len(nums)-1] == 6:
    return True
  else:
    return False


def same_first_last(nums):
  if len(nums) == 0:
    return False
  elif nums[0] == nums[len(nums)-1]:
    return True
  else:
    return False


def make_pi():
  li = [3,1,4]
  return li


def common_end(a, b):
  if a[len(a)-1] == b[len(b)-1] or a[0] == b[0]:
    return True
  else:
    return False


def sum3(nums):
  total = 0
  for i in nums:
    total += i
  return total


def rotate_left3(nums):
  li = []
  for i in range(1,len(nums)):
    li.append(nums[i])
  li.append(nums[0])
  return li


def reverse3(nums):
  li = []
  for i in range(1,len(nums)+1):
    li.append(nums[len(nums)-i])
  return li


def max_end3(nums):
  li = []
  if nums[0] > nums[len(nums)-1]:
    for i in nums:
      li.append(nums[0])
  else:
    for i in nums:
      li.append(nums[len(nums)-1])
  return li


def sum2(nums):
  total = 0
  for i in range(0,min(2,len(nums))):
    total += nums[i]
  return total


def middle_way(a, b):
  li = []
  li.append(a[1])
  li.append(b[1])
  return li


def make_ends(nums):
  li = []
  li.append(nums[0])
  li.append(nums[len(nums)-1])
  return li
  

def has23(nums):
  for i in nums:
    if i == 2 or i == 3:
      return True
  return False


def count_evens(nums):
  total = 0
  for i in nums:
    if i % 2 == 0:
      total += 1
  return total
  
  
def big_diff(nums):
  mx = -1000000
  mi = 1000000
  for i in nums:
    mx = max(mx,i)
    mi = min(mi,i)
  return mx-mi
  

def centered_average(nums):
  mx = -1000000
  mi = 1000000
  total = 0
  for i in nums:
    mx = max(mx,i)
    mi = min(mi,i)
    total += i  
  return (total-mx-mi)/(len(nums)-2)


def sum13(nums):
  total = 0
  i = 0
  while i < len(nums):
    if nums[i] == 13:
      i += 2
    else:
      total += nums[i]
      i += 1
  return total
  
  
def sum67(nums):
  total = 0
  i = 0
  tf = True
  while i < len(nums):
    if nums[i] == 6:
      tf = False
    
    if tf == True:
      total += nums[i]
    if nums[i] == 7:
      tf = True
      
    i += 1      
  return total


def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  return False


