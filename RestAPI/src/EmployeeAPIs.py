import inspect
import json

class EmployeeAPIs:
    global baseURL
    global file_content
    baseURL= "http://dummy.restapiexample.com/api/v1"
    filename = "../resources/TestData/TestData.json"

    with open(filename) as json_file:
        content = json_file.read()
        file_content = json.loads(content)

    def create_employee(self):
        try:
            relative_url = "/create"
            create_employee_url = baseURL + relative_url
            function_name = inspect.stack()[0].function
            create_employee_data = file_content[function_name]
            global create_employee_payload
            create_employee_payload = create_employee_data["payload"]
            create_employee_headers = create_employee_data["headers"]
            payload_string = json.dumps(create_employee_payload)
            response = self.api_lib.postAPI(create_employee_url, payload_string,create_employee_headers)
            response_json = json.loads(response.text)
            employee_name = response_json.get('name')
            if(employee_name == create_employee_payload.get('name')):
                print("\n")
                print(" Newly created entry : " + response.text)
                assert response.status_code == 200 , "employee creation API failed!"
        except:
            print("Error occured while hitting create employee API : ")
            print(response.text)
        return response


    def get_employee(self,e_id,functiontype):
        relative_url = "/employee/" + str(e_id)
        get_employee_url = baseURL + relative_url
        function_name = inspect.stack()[0].function
        get_employee_data = file_content[function_name]
        get_employee_headers = get_employee_data["headers"]
        get_employee_payload = ""
        response = self.api_lib.getAPI(get_employee_url, get_employee_payload, get_employee_headers)
        response_json = json.loads(response.text)
        if(functiontype == 1):
            assert response_json == False, "Employee deletion failed"
        else:
            empid = response_json["id"]
            assert str(e_id) == str(empid), "Employee not found"
            emp_name = response_json.get('employee_name')
            emp_sal = response_json.get('employee_salary')
            emp_age = response_json.get('employee_age')
            assert (create_employee_payload.get('name')) == str(emp_name), "Employee name does not match"
            assert str(create_employee_payload.get('salary')) == str(emp_sal), "Employee salary does not match"
            assert str(create_employee_payload.get('age')) == str(emp_age), "Employee age does not match"
        return response

    def get_all_employees(self):
        relative_url = "/employees"
        get_employees_url = baseURL  + relative_url
        function_name = inspect.stack()[0].function
        get_employees_data = file_content[function_name]
        get_employees_headers = get_employees_data["headers"]
        get_employees_payload = ""
        response = self.api_lib.getAPI(get_employees_url, get_employees_payload, get_employees_headers)
        assert response.status_code == 200, " Not able to fetch list of all employees"
        return response

    def update_employee(self, e_id):
        relative_url = "/update/" + str(e_id)
        update_employee_url = baseURL + relative_url
        function_name = inspect.stack()[0].function
        update_employee_data = file_content[function_name]
        update_employee_headers = update_employee_data["headers"]
        update_employee_payload = update_employee_data["payload"]
        update_payload = json.dumps(update_employee_payload)
        response = self.api_lib.putAPI(update_employee_url, update_payload, update_employee_headers)
        response_text = json.loads(response.text)
        emp_name = response_text.get('name')
        emp_sal = response_text.get('salary')
        emp_age = response_text.get('age')
        assert str(update_employee_payload.get('name')) == str(emp_name), "Employee name does not match"
        assert str(update_employee_payload.get('salary')) == str(emp_sal), "Employee salary does not match"
        assert str(update_employee_payload.get('age')) == str(emp_age), "Employee age does not match"
        print("\n")
        print("Updated details of the employee :" +str(response_text))
        return response

    def delete_employee(self,e_id):
        relative_url = "/delete/" + str(e_id)
        delete_url = baseURL + relative_url
        payload = ""
        function_name = inspect.stack()[0].function
        delete_employee_data = file_content[function_name]
        delete_employee_headers = delete_employee_data["headers"]
        response = self.api_lib.deleteAPI(delete_url, payload, delete_employee_headers)
        assert response.status_code == 200, "Delete API failed!"
        return response