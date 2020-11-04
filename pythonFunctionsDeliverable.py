# def sum_to(num):
#   sum = 0
#   for i in range(num+1):
#     sum = sum + i
#   return sum
# print(sum_to(6))
# print(sum_to(10))


# def largest(num_list):
#   if len(num_list):
#     large = num_list[0]
#   for num in num_list:
#     if large<num:
#       large = num
#   return large
# print(largest([1,2,3,4,0]))
# print(largest([10,4,2,231,91, 54]))


# def occurances(word,alphabet):
#   count = 0
#   for i in range(len(word)):
#     if alphabet == word[i]:
#       count += 1
#   return count


# def occurances(word,alphabet):
#   count = 0
#   for i in range(0, len(word),len(alphabet)):
#     if alphabet in word[i:i+len(alphabet)]:  
#       count += 1
#   return count
# print(occurances('fleep floop','e'))
# print(occurances('fleep floop','p'))
# print(occurances('fleep floop','ee'))
# print(occurances('fleep floop','fe'))


def product(*args):
  pro = 1
  for num in args:
    pro = pro*num
  return pro

print(product(-1,4))
print(product(2,5,5))
print(product(4,0.5,5))





