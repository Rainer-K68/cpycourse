!!! question "Lesson: Customers Class"
    Create a class-hierarchy:
    
    - Class Customer
      - class-attribute: number_of_customers (which should increment with every new class-instance)
      - class constructor with parameter: 'email', 'employees'
      - instance-attribute: 'id' (number of the current value of 'number_of_customers')
      - instance-attribute: 'email'
      - instance-attribute: 'employees'  (number of employees))
      - isntance-method: 'getEmployees' (returning 'employees')
    - Class Retail(Customer)
      - private class attribute: '__type'
      - class constructor with parameters: 'name', 'email', 'employees'
      - private instance-attribute: '__retailname' (initialized with 'name'-parameter
      - instance-method: 'getRetailName' (returning private instance-attribute '__retailname')
      - instance-method: 'getType' (returning private class_attribute '__type')
    - Class Wholesale(Customer)
      - private class attribute: '__type'
      - class constructor with parameters: 'name', 'email', 'employees'
      - private instance-attribute: '__wholesalename' (initialized with 'name'-parameter
      - instance-method: 'geWholesaleName' (returning private instance-attribute '__retailname')
      - instance-method: 'getType' (returning private class_attribute '__type')
      
   1.) Create a list of Customers of different types ('Retail'-customers and 'Wholesale'-customers)
        
   2.) Iterate the list and output 'name', 'type', 'id' and 'employees' of each customer
      
      
   Hint: provide a callable interface `__call__()`
