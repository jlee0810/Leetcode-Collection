"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = {}

        for employee in employees:
            employee_dict[employee.id] = employee

        # DFS
        def dfs(id):
            employee_obj = employee_dict[id]
            if not employee_obj.subordinates:
                return employee_obj.importance
            subord_import_total = 0
            for subord_id in employee_obj.subordinates:
                subord_import_total += dfs(subord_id)
            
            return employee_dict[id].importance + subord_import_total
        
        return dfs(id)

        # BFS
        # for employee in employees:
        #     if employee.id != id:
        #         continue
        #     if employee.id == id:
                # q = deque()
                # q.append(employee)
                # total_importance = employee.importance

                # while q:
                #     curr_employee = q.popleft()
                #     for subord in curr_employee.subordinates:
                #         subord_obj = employee_dict[subord]
                #         total_importance += subord_obj.importance
                #         q.append(subord_obj)
                
                # return total_importance