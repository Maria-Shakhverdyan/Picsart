import json

data = {
  "company": "TechCorp",
  "departments": [
    {
      "name": "Engineering",
      "employees": [
        {"id": 1, "name": "Alice", "role": "Engineer"},
        {"id": 2, "name": "Bob", "role": "Manager"}
      ]
    },
    {
      "name": "Sales",
      "employees": [
        {"id": 3, "name": "Charlie", "role": "Sales Rep"},
        {"id": 4, "name": "Dana", "role": "Sales Lead"}
      ]
    }
  ]
}

try:
    with open('company_data.json', 'w') as file:
        json.dump(data, file, indent=2)
except Exception as e:
    print(e)