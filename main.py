# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
class Server:
    def __init__(self,type,kernel_num,memory,harware_cost,daily_cost):
        self.type = type
        self.kernel_num = kernel_num
        self.memory = memory
        self.hardware_cost = harware_cost
        self.daily_cost = daily_cost

class VirtualMachine:
    def __init__(self,type,kernel_num,memory,is_double):
        self.type = type
        self.kernel_num = kernel_num
        self.memory = memory
        self.is_double = is_double

class Request:
    def __init__(self,type=0,vm_type=0,vm_id=0):
        self.type = type
        self.vm_type = vm_type
        self.vm_id = vm_id
def readData():
    server_num = int(sys.stdin.readline())
    server_list = []
    for i in range(server_num):
        data = sys.stdin.readline()
        data = data.split(',')
        server_list.append(Server(data[0][1:],int(data[1]),int(data[2]),int(data[3]),int(data[4][:-2])))
    vm_num = int(sys.stdin.readline())
    vm_list = []
    for i in range(vm_num):
        data = sys.stdin.readline()
        data = data.split(',')
        vm_list.append(VirtualMachine(data[0][1:],int(data[1]),int(data[2]),int(data[3][:-2])))
    request_num = int(sys.stdin.readline())
    request_list = []
    for i in range(request_num):
        today_num = int(sys.stdin.readline())
        for j in range(today_num):
            today_list = []
            data = sys.stdin.readline()
            data = data.split(',')
            if data[0][1:] == 'add':
                today_list.append(Request(data[0][1:],data[1],int(data[2][:-2])))
            else:
                today_list.append(Request(data[0][1:], vm_id=int(data[1][:-2])))
        request_list.append(today_list)
    return server_list,vm_list,request_list

if __name__ == '__main__':
    server_list,vm_list,request_list = readData()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
