import json
import unittest
import pytest
from src.APILib import APILib
from src.EmployeeAPIs import EmployeeAPIs

class Employee_test(unittest.TestCase):
    api_lib = APILib
    emp_api = EmployeeAPIs

    @pytest.mark.run(order=1)
    def test_get_all_employees(self):
        self.emp_api.get_all_employees(self)

    @pytest.mark.run(order=2)
    def test_create_employee(self):
        global emp_id
        response = self.emp_api.create_employee(self)
        if(response.status_code) == 200:
            response_text = json.loads(response.text)
            emp_id = response_text.get('id')

    @pytest.mark.run(order=3)
    def test_get_employee(self):
        functiontype = 0
        self.emp_api.get_employee(self,emp_id,functiontype)

    @pytest.mark.run(order=4)
    def test_update_employee(self):
        self.emp_api.update_employee(self,emp_id)

    @pytest.mark.run(order=5)
    def test_delete_employee(self):
            self.emp_api.delete_employee(self,emp_id)

    @pytest.mark.run(order=6)
    def test_get_employee_after_deletion(self):
        functiontype = 1
        self.emp_api.get_employee(self, emp_id,functiontype)