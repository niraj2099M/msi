
# Input data: List of dictionaries
employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

# Function to be passed to the map() function. Do not change this.
def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

def to_mod_list(employee_list):

   map_emp=map(mod,employee_list)
   #print(map_emp)                             #memory allocation
   print(hex(id(map_emp)))
   return list(map_emp)

#print("Test :",id(to_mod_list))  

def generate_usernames(mod_list):

   lst=[x.replace(" ","_") for x in mod_list ]
   return lst
   

def map_id_to_initial(employee_list):

   l=len(employee_list)
   dic1={employee_list[x]["name"][0]:employee_list[x]["id"] for x in range(l)}  #imp_
   return dic1
   

def main():
   mod_emp_list = to_mod_list(employee_list)
   print("Modified employee list: " + str(mod_emp_list) + "\n")

   print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

   print(f"Initials and ids: {map_id_to_initial(employee_list)}")

if __name__ == "__main__":
   main()