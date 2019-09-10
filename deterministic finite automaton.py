Name = Arif
ID = 1611041


def move(intial_state, i, state):
    v = intial_state
    if v in state:
        if i in state[v]:
            v = state[intial_state][i]
            return v
        else:
            return v

    
state = {}
user_input = input("how many state, transitions and final states, give space in between--> ")
print("      ")
bol = True
#user_secondInput = input("Numer of transitions--> ")
#print("      ")
user_thirdInput = input("size of alphabet--> ")
u = user_input.split(" ")
print(" ")
n = int(u[0])
m = int(u[1])
F = int(u[2])
a = user_thirdInput

for i in range(0,n):
    state[i] = {}

x = input("what are the alphabet symbol give space in between--> ")
xx = x.split(" ")
print(xx)
print("      ")
print("Which states will be connected with which char put space in between. For example 0 1 a and than press enter to give the next connection ")
print("      ")
for j in range(0, m):
    input_string = input()
    lst = input_string.split(" ")
    start = int(lst[0])
    char = lst[2]
    next = int(lst[1])
    if start in state:
        if char in state[start]:
            print("NOT A DFA")
            bol = False
            break
        else:
            state[start][char] = next
     
if bol == True:
   final_state = input("Which states are the final state.If more than 1 give space in between. For example 1 3 are the final states--> ")
   print("      ")
   final = []
   f = final_state.split(" ")
   for i in range(len(f)):
       f2 = int(f[i])
       final.append(f2)
           
   
   string = (input("Input a string "))
   print("      ")
   intial_state = 0

   for i in string:
       intial_state= move(intial_state,i,state)
    
 
   if intial_state in final:
        print("DFA accpets the input string")
   else:
       if intial_state in state:
           for i in range(len(xx)):
               if xx[i] in state[intial_state]:
                   if state[intial_state][xx[i]] in final:
                       print("DFA reject the input string")
                   else:
                       print("NO move from intial state to final")
#       print("DFA rejectes the input string")
         
 

    


    
    
    
