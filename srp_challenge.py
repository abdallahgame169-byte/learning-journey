# 1. الدالة الأولى: مسؤولة فقط عن الحساب (SRP)
def calculate_bonus(salary):
    return salary * 1.1

# 2. الدالة الثانية: مسؤولة فقط عن الطباعة (SRP)
def print_employee_report(name, final_salary):
    print(f"Employee: {name} has a new salary of: {final_salary}")

# 3. الدالة الثالثة: تدير العملية وتربط الدوال ببعضها
def process_all_employees(employees):
    for emp in employees:
        # أ- نحسب الراتب الجديد باستخدام الدالة الأولى
        new_salary = calculate_bonus(emp['salary'])
        
        # ب- نرسل الاسم والراتب الجديد لدالة الطباعة
        print_employee_report(emp['name'], new_salary)

# --- البيانات وتشغيل الكود ---
staff = [
    {'name': 'Abdullah', 'salary': 1000},
    {'name': 'Sami', 'salary': 1200}
]

process_all_employees(staff)
