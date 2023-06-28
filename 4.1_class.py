## Решение задачи за O(N**2)

# def strcounter(s):
#     for lit in s:
#         counter = 0
#         for sub_lit in s:
#             if lit == sub_lit:
#                 counter +=1
#         print(lit, counter)
#
# strcounter('aaabcd')

## Решение задачи за O(N*M)

# s = 'aaaaaa________=======444444####aaaaaaaaaa'
# print(list(s))
# print(set(s))

# def strcounter(s):
#     for lit in set(s): #### O(N*M) если M <= N
#         counter=0
#         for sub_lit in s:
#             if lit == sub_lit:
#                 counter += 1
#         print(lit, counter)
#
# strcounter('aaabbcdddd')


# ## Решение задачи за O(N+N) --> O(2N) --> O(N)
#
# def strcounter(s):
#     lits_counter = {}
#     for lit in s:
#         lits_counter[lit] = lits_counter.get(lit, 0) + 1
#     for lit, counter in lits_counter.items():
#         print(lit, counter)
#
# strcounter('aaaddfghhhhhhhhhhj')
#
# # https://git-scm.com
# ## https://github.com ----> GITHUB
#
#
# # На вход подается строка, все символы находятся в нижнем регистре и без пробелов.
# # Напишите функцию, которая будет возвращать True, если строка является палиндромом и False, если строка палиндромом не является.

# str = input("Введите строку: ")
#
# def palindrome(str):
#     return str[::-1] == str
# print (palindrome(str))


