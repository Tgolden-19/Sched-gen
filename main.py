import PermutationGenerator as pg
import numpy as np
# import csv
import pandas as pd



tree = pg.PermutationTree(depthlim=7)

totalperms = tree.cumulate_perms()

gensched = tree.biweekly_perms_self()

# df = pd.DataFrame(gensched)
# df.to_excel("gen_sched_test1.xlsx")
# print(gensched)

# def seperate_to_groups(orders):
#     index = 201
#     jump = 200
#     previndex = 1
#     temp = None
#     # filenum = 0
#     while index < len(orders):
#         temp = orders[previndex:index]
#         temp.insert(0, orders[0])
#         df = pd.DataFrame(temp)
#         df.to_excel("batched_missing_orders_" + str(previndex) + "-" + str(index) + ".xlsx")
#         previndex = index
#         index += jump
#
# with open("batched_missing_orders.csv", newline='') as orders:
#     ordersreader = csv.reader(orders, delimiter=',')
#     #list(ordersreader)
#     seperate_to_groups(list(ordersreader))



# print(len(gensched))
# print(np.shape(gensched))
# print(tree.generate_schedule_self(10))
# DF = pd.DataFrame(gensched)
# DF.to_csv("generated_schedule.csv")




#
# for i in range(len(totalperms)):
#     totalperms[i] = totalperms[i].split(',')
#
#
# for i in range(len(totalperms)):
#     for j in range(len(totalperms[i])):
#         if totalperms[i][j] == ' ':
#             totalperms[i].pop(j)
#
# # removes all weeks with more than 2 days off
# indexi = 0
# for i in totalperms:
#     indexi += 1
#     count = 0
#     for j in i:
#         #print(j)
#         #print(count)
#         if j != 'AM' or j != 'PM':
#             count += 1
#     #print(indexi)
#     if count > 2:
#         print("removing")
#         totalperms.remove(i)
#
# print(len(totalperms))
#print(totalperms)



#
# print(br1)
# print(br2)
# print(br3)