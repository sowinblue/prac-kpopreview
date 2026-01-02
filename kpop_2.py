import tkinter as tk
from tkinter import messagebox, ttk

class ModernKpopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("K-POP Review Record")
        self.root.geometry("1100x750")
        self.root.configure(bg="#FFFFFF") 

        # 테마 스타일 설정
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TButton", font=("Pretendard", 10), padding=30)
        self.style.configure("Header.TFrame", background="#FFFFFF")

        self.posts = []
        self.post_id_counter = 1

        # --- 상단 헤더 (Shadow 효과 느낌) ---
        self.header = tk.Frame(self.root, bg="#FFFFFF", height=70, relief="flat")
        self.header.pack(side="top", fill="x")
        self.header.pack_propagate(False)

        # 로고 (부드러운 폰트 적용)
        self.logo_btn = tk.Button(self.header, text="KRR", font=("Arial", 16, "bold"),
                                fg="#000000", bg="white", bd=0, cursor="hand2", command=self.show_main)
        self.logo_btn.pack(side="left", padx=50)

        # 상단 메뉴 (둥근 버튼 느낌)
        self.menu_area = tk.Frame(self.header, bg="#FFFFFF")
        self.menu_area.pack(side="right", padx=20)

        menus = [("소개", self.show_intro), ("품평장", self.show_board), ("문의/FAQ", self.show_faq)]
        for text, cmd in menus:
            btn = tk.Button(self.menu_area, text=text, command=cmd, font=("Pretendard", 10),
                           fg="#000000", bg="white", bd=0, padx=15, cursor="hand2")
            btn.pack(side="left")
            btn.bind("<Enter>", lambda e, b=btn: b.configure(fg="#6200EE")) # 호버 효과
            btn.bind("<Leave>", lambda e, b=btn: b.configure(fg="#555555"))

        # --- 구분선 ---
        line = tk.Frame(self.root, height=1, bg="#DEE2E6")
        line.pack(fill="x")

        # --- 콘텐츠 영역 ---
        self.container = tk.Frame(self.root, bg="#F8F9FA")
        self.container.pack(fill="both", expand=True, padx=40, pady=30)

        self.show_main()

    def clear_container(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def show_main(self):
        self.clear_container()
        # 메인 환영 문구
        main_frame = tk.Frame(self.container, bg="#F8F9FA")
        main_frame.place(relx=0.5, rely=0.4, anchor="center")
        
        tk.Label(main_frame, text="K-POP 음악 품평회", font=("Pretendard", 40, "bold"), 
                 bg="#F8F9FA", fg="#212529").pack()
        tk.Label(main_frame, text="나랑 음악얘기 해줄 사람", font=("Pretendard", 14), 
                 bg="#F8F9FA", fg="#6C757D").pack(pady=10)
        
        start_btn = tk.Button(main_frame, text="품평 시작하기", font=("Arial", 12, "bold"),
                             fg="white", bg="#1B0046", padx=30, pady=10, bd=0, 
                             command=self.show_board, cursor="hand2")
        start_btn.pack(pady=30)

    def show_intro(self):
        self.clear_container()
        card = tk.Frame(self.container, bg="white", padx=40, pady=40, relief="flat")
        card.pack(fill="both", expand=True)

        title = tk.Label(card, text="프로젝트 소개", font=("Arial", 24, "bold"), bg="white", fg="#212529")
        title.pack(anchor="w", pady=(0, 20))

        content = (
            "우리는 음악을 듣기 위해 반드시 모든 정보를 알아야 할 필요는 없다.\n"
            "음악은 그 자체로 감상할 수 있다.\n"
            "그러나 현재의 K-POP은 음악 외적인 요소와 강하게 결합된 산업 구조 속에 놓여 있다.\n"
            "이는 자연스러운 흐름이지만, 음악 그 자체로 이야기할 수 있는 공간은 점점 줄어들고 있다.\n\n"

            "이 프로젝트는 그러한 문제의식에서 출발했다.\n"
            "외부적인 요소가 아닌 음악을 구성하는 트랙과 사운드, 가사와 흐름을 이야기하는 공간. 감정적인 찬반이 아닌, 음악적 사고가 오가는 공간을 만들고자 한다.\n\n"

            "이 게시판은 작곡가의 시선에서 곡을 바라보는 분석을 지향한다.\n" 
            "다만 참여 자격은 제한하지 않으며, 음악을 깊이 있게 듣고자 하는 모든 사람에게 열려 있다."
        )
        tk.Label(card, text=content, font=("Arial", 16, "bold"), bg="white", 
                fg="#495057", justify="left", wraplength=800).pack(anchor="w")

    def show_board(self):
        self.clear_container()
        
        # 품평장 레이아웃 (좌측 카테고리 / 우측 쓰기)
        left_side = tk.Frame(self.container, bg="#F8F9FA", width=180)
        left_side.pack(side="left", fill="y", padx=(0, 20))

        tk.Label(left_side, text="CATEGORY", font=("Arial", 9, "bold"), bg="#F8F9FA", fg="#ADB5BD").pack(anchor="w", pady=10)
        for cat in ["전체 보기", "가수별", "곡 제목별", "장르별"]:
            btn = tk.Button(left_side, text=cat, font=("Arial", 10), bg="#F8F9FA", 
                        fg="#495057", bd=0, anchor="w", cursor="hand2")
            btn.pack(fill="x", pady=2)

        # 라이팅 카드
        write_card = tk.Frame(self.container, bg="white", padx=30, pady=30)
        write_card.pack(side="right", fill="both", expand=True)

        tk.Label(write_card, text="새 품평 작성", font=("Arial", 18, "bold"), bg="white").pack(anchor="w", pady=(0, 20))

        # 입력 필드
        row1 = tk.Frame(write_card, bg="white")
        row1.pack(fill="x", pady=5)
        
        tk.Label(row1, text="가수명", bg="white", font=("Arial", 10)).pack(side="left")
        self.ent_artist = tk.Entry(row1, bg="#F1F3F5", bd=0, highlightthickness=1, highlightcolor="#6200EE")
        self.ent_artist.pack(side="left", padx=10, expand=True, fill="x")

        tk.Label(row1, text="곡 제목", bg="white", font=("Arial", 10)).pack(side="left", padx=(10, 0))
        self.ent_title = tk.Entry(row1, bg="#F1F3F5", bd=0, highlightthickness=1, highlightcolor="#6200EE")
        self.ent_title.pack(side="left", padx=10, expand=True, fill="x")

        # 메모장
        tk.Label(write_card, text="분석 리포트", bg="white", font=("Arial", 10)).pack(anchor="w", pady=(10, 5))
        self.txt_content = tk.Text(write_card, bg="#F1F3F5", bd=0, font=("Pretendard", 11), 
                                  highlightthickness=1, highlightcolor="#6200EE", padx=10, pady=10)
        self.txt_content.pack(fill="both", expand=True, pady=10)

        # 하단 버튼
        btn_row = tk.Frame(write_card, bg="white")
        btn_row.pack(fill="x")
        
        save_btn = tk.Button(btn_row, text="품평 등록하기", font=("Pretendard", 10, "bold"),
                            fg="white", bg="#6200EE", padx=20, pady=8, bd=0, command=self.save_post)
        save_btn.pack(side="right")
        
        temp_btn = tk.Button(btn_row, text="임시 저장", font=("Pretendard", 10),
                            fg="#6200EE", bg="white", bd=0, padx=15)
        temp_btn.pack(side="right", padx=10)

    def save_post(self):
        # 금지 키워드 체크 로직 (예시)
        content = self.txt_content.get("1.0", tk.END)
        forbidden = ["트리플에스", "엔믹스", "아일릿", "뉴진스"] # 가수명 차단 예시
        
        for word in forbidden:
            if word in content:
                messagebox.showerror("차단 알림", f"'{word}'와 같은 가수 정보는 기재할 수 없습니다.\n음악 요소에 집중해주세요!")
                return
        
        messagebox.showinfo("성공", "품평이 성공적으로 등록되었습니다!")

    def show_faq(self):
        self.clear_container()

        Suggestion_email = ("문의사항 있을 시 이메일로 보내주세요\n"
                            "email: hahahahohoho@kpopreviewrecord.com")
        
        tk.Label(self.container, text=Suggestion_email, font=("Arial", 20, "bold"), bg="#F8F9FA", padx= 200, pady= 100).pack(anchor="w")
        

if __name__ == "__main__":
    root = tk.Tk()
    # 폰트가 설치되어 있지 않을 경우를 대비해 기본 폰트 설정
    app = ModernKpopApp(root)
    root.mainloop()


