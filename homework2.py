def menu():
    print("\n--- 人事資料管理系統 ---")
    print("1. 新增資料")
    print("2. 查詢資料")
    print("3. 修改資料")
    print("4. 刪除資料")
    print("5. 顯示所有資料")
    print("6. 退出系統")
    print("------------------------")

def add_rec(rec):
    while True:
        dep = input("請輸入部門: ")
        name = input("請輸入姓名: ")
        age = input("請輸入年齡: ")
        phone = input("請輸入手機號碼: ")
        rec = {"部門": dep, "姓名": name, "年齡": age, "手機": phone}
        rec.append(rec)
        
        cont = input("是否繼續新增資料? (y/n): ")
        if cont.lower() != 'y':
            break

def che_rec(rec):
    name = input("請輸入要查詢的姓名: ")
    found = [r for r in rec if r["姓名"] == name]
    
    if found:
        print("\n--- 查詢結果 ---")
        print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機'}")
        print("--------------------------------")
        for r in found:
            print(f"{r['部門']:<10}{r['姓名']:<10}{r['年齡']:<10}{r['手機']}")
    else:
        print("查無此人。")

def rev_rec(rec):
    name = input("請輸入要修改的姓名: ")
    found = [r for r in rec if r["姓名"] == name]
    
    if found:
        rec = found[0]
        print("當前資料:")
        print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機'}")
        print("--------------------------------")
        print(f"{rec['部門']:<10}{rec['姓名']:<10}{rec['年齡']:<10}{rec['手機']}")
        
        option = input("1. 修改部門\n2. 修改姓名\n3. 修改年齡\n4. 修改手機\n請選擇要修改的欄位: ")
        if option == '1':
            rec["部門"] = input("請輸入新的部門: ")
        elif option == '2':
            rec["姓名"] = input("請輸入新的姓名: ")
        elif option == '3':
            rec["年齡"] = input("請輸入新的年齡: ")
        elif option == '4':
            rec["手機"] = input("請輸入新的手機: ")
        
        print("\n--- 更新後的資料 ---")
        print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機'}")
        print("--------------------------------")
        print(f"{rec['部門']:<10}{rec['姓名']:<10}{rec['年齡']:<10}{rec['手機']}")
    else:
        print("查無此人。")

def del_rec(rec):
    name = input("請輸入要刪除的姓名: ")
    found = [r for r in rec if r["姓名"] == name]
    
    if found:
        rec = found[0]
        print(f"確定要刪除 {rec['姓名']} 的資料嗎? (y/n): ", end="")
        confirm = input()
        
        if confirm.lower() == 'y':
            rec.remove(rec)
            print(f"{rec['姓名']} 的資料已刪除。")
            all_rec(rec)
        else:
            print("刪除操作已取消。")
    else:
        print("查無此人。")

def all_rec(rec):
    if rec:
        print("\n--- 剩餘的所有資料 ---")
        print(f"{'部門':<10}{'姓名':<10}{'年齡':<10}{'手機'}")
        print("--------------------------------")
        for r in rec:
            print(f"{r['部門']:<10}{r['姓名']:<10}{r['年齡']:<10}{r['手機']}")
    else:
        print("目前沒有任何資料。")

def main():
    rec = []
    while True:
        menu()
        choice = input("請選擇功能: ")
        
        if choice == '1':
            add_rec(rec)
        elif choice == '2':
            che_rec(rec)
        elif choice == '3':
            rev_rec(rec)
        elif choice == '4':
            del_rec(rec)
        elif choice == '5':
            all_rec(rec)
        elif choice == '6':
            print("系統已退出。")
            break
        else:
            print("無效的選擇，請再試一次。")

if __name__ == "__main__":
    main()
