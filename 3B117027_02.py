#需要的函式:
#載入、讀取學生資訊、加入課程名稱、計算所有科目平均分、主程式
import json

def load(file_name):            #載入students.json檔案並用with open自動關閉
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:       #未找到檔案 用try和Except FileNotFoundError去判斷
        print("找不到指定的檔案。")
        return None

def get_student_info(data, student_id):                         #讀取json學生資訊
    for student in data:
        if student['student_id'] == student_id:
            return student
    raise ValueError(f"學號 {student_id} 找不到.")

def add_course(data, student_id, course_name, course_score):    #新增科目和分數到指定學生資料中的函式
    if not course_name or not course_score:
        raise ValueError("課程名稱或分數不可空白.")

    for student in data:
        if student['student_id'] == student_id:
            student['courses'].append({"name": course_name, "score": float(course_score)})
            print("課程已成功新增。")
            return
    raise ValueError(f"學號 {student_id} 找不到.")

def calculate_average_score(student_data):      #取平均分函式
    total_score = 0.0
    num_courses = len(student_data['courses'])  #科目的數量
    if num_courses == 0:
        return 0.0

    for course in student_data['courses']:      #從json檔的courses
        total_score += course['score']          #加總成績
    return total_score / num_courses            #取平均分

def main():                                     #主程式
    data = load('students.json')
    if data is None:                            #if data是空
        return

    while True:                                 #loop
        print("***************選單***************")
        print("1. 查詢指定學號成績")
        print("2. 新增指定學號的課程名稱與分數")
        print("3. 顯示指定學號的各科平均分數")
        print("4. 離開")
        print("**********************************")
        choice = input("請選擇操作項目：")

        if choice == '1':                       #輸入1
            student_id = input("請輸入學號: ")
            try:
                student_info = get_student_info(data, student_id)
                print("=>學生資料:", json.dumps(student_info,ensure_ascii=False, indent=2 ))
            except ValueError as e:
                print(f"=>發生錯誤: {e}")
        elif choice == '2':                     #輸入2
            student_id = input("請輸入學號: ")
            course_name = input("請輸入要新增課程的名稱: ")
            course_score = input("請輸入要新增課程的分數: ")
            try:
                add_course(data, student_id, course_name, course_score)
            except ValueError as e:
                print(f"=>其它例外: {e}")
        elif choice == '3':                     #輸入3
            student_id = input("請輸入學號: ")
            try:
                student_info = get_student_info(data, student_id)
                average_score = calculate_average_score(student_info)
                print("=>各科平均分數:", average_score)
            except ValueError as e:
                print(f"=>發生錯誤: {e}")
        elif choice == '4':                     #輸入4
            print("=>程式結束。")
            break
        else:
            print("=>請輸入有效的選項。")        #輸入其他回答

if __name__ == "__main__":
    main()