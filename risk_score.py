import csv

# เก็บข้อมูลทั้งหมด
employees = {}

def add_employee():
    emp_id = input("รหัสพนักงาน: ")
    name = input("ชื่อพนักงาน: ")
    employees[emp_id] = {
        "name": name,
        "activities": [],
        "total_score": 0
    }
    print("✅ เพิ่มพนักงานเรียบร้อย\n")

def add_activity():
    emp_id = input("รหัสพนักงาน: ")
    if emp_id not in employees:
        print("❌ ไม่พบพนักงาน\n")
        return

    activity = input("ชื่อกิจกรรม Risk Assessment: ")
    score = int(input("คะแนนที่ได้รับ: "))

    employees[emp_id]["activities"].append({
        "activity": activity,
        "score": score
    })
    employees[emp_id]["total_score"] += score
    print("✅ บันทึกกิจกรรมเรียบร้อย\n")

def show_summary():
    print("\n📊 สรุปคะแนนสะสม")
    for emp_id, data in employees.items():
        print(f"- {data['name']} ({emp_id}) : {data['total_score']} คะแนน")
    print()

def save_to_csv():
    with open("risk_score.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["รหัสพนักงาน", "ชื่อ", "กิจกรรม", "คะแนน"])

        for emp_id, data in employees.items():
            for act in data["activities"]:
                writer.writerow([
                    emp_id,
                    data["name"],
                    act["activity"],
                    act["score"]
                ])
    print("💾 บันทึกข้อมูลลงไฟล์ risk_score.csv เรียบร้อย\n")

def menu():
    while True:
        print("===== ระบบคะแนนสะสม Risk Assessment =====")
        print("1. เพิ่มพนักงาน")
        print("2. เพิ่มกิจกรรม Risk Assessment")
        print("3. ดูสรุปคะแนน")
        print("4. บันทึกเป็นไฟล์ CSV")
        print("0. ออกโปรแกรม")

        choice = input("เลือกเมนู: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            add_activity()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            save_to_csv()
        elif choice == "0":
            print("👋 ออกจากโปรแกรม")
            break
        else:
            print("❌ กรุณาเลือกเมนูที่ถูกต้อง\n")

menu()
