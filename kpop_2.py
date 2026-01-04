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
        self.style.configure("TButton", font=("Arial", 10), padding=30)
        self.style.configure("Header.TFrame", background="#FFFFFF")

        self.posts = []
        self.post_id_counter = 1

        # --- 상단 헤더 (Shadow 효과 느낌) ---
        self.header = tk.Frame(self.root, bg="#FFFFFF", height=70, relief="flat")
        self.header.pack(side="top", fill="x")
        self.header.pack_propagate(False)

        # 로고 (부드러운 폰트 적용)
        self.logo_btn = tk.Button(self.header, text="KRR", font=("Arial", 16, "bold"),
                                fg="#FFFFFF", bg="#1B0046", bd=0, cursor="hand2", command=self.show_main)
        self.logo_btn.pack(side="left", padx=50)

        # 상단 메뉴 (둥근 버튼 느낌)
        self.menu_area = tk.Frame(self.header, bg="#FFFFFF")
        self.menu_area.pack(side="right", padx=20)

        menus = [("소개", self.show_intro), ("품평장", self.show_board), ("문의/FAQ", self.show_faq)]
        for text, cmd in menus:
            btn = tk.Button(self.menu_area, text=text, command=cmd, font=("Pretendard", 10),
                        fg="#000000", bg="#FFFFFF", bd=0, padx=15, cursor="hand2")
            btn.pack(side="left")
            btn.bind("<Enter>", lambda e, b=btn: b.configure(fg="#6200EE")) # 호버 효과
            btn.bind("<Leave>", lambda e, b=btn: b.configure(fg="#000000"))

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
        main_frame.place(relx=0.5, rely=0.4,anchor="center")
        
        tk.Label(main_frame, text="K-POP 음악 품평회", font=("Arial", 40, "bold"), 
                 bg="#F8F9FA", fg="#212529").pack()
        tk.Label(main_frame, text="(드르륵칵) 케이팝 \"음악\" 덕후들 잠시 모여봐 ", font=("Arial", 14), 
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
            "다만 참여 자격은 제한하지 않으며, 음악을 깊이 있게 듣고자 하는 모든 사람에게 열려 있다.\n"
        )
        tk.Label(card, text=content, font=("Arial", 16, "bold"), bg="white", 
                fg="#495057", justify="left", wraplength=800).pack(anchor="w")

    def show_board(self):
        self.clear_container()
        
        # 품평장 레이아웃 (좌측 카테고리 / 우측 쓰기)
        left_side = tk.Frame(self.container, bg="#F8F9FA", width=180)
        left_side.pack(side="left", fill="y", padx=(0, 20))

        tk.Label(left_side, text="CATEGORY", font=("Arial", 9, "bold"), bg="#F8F9FA", fg="#ADB5BD").pack(anchor="w", pady=10)
        categories = [
            ("전체 보기", lambda: self.show_list()),
            ("아티스트", lambda: self.show_index_selector("artist")),
            ("곡 제목", lambda: self.show_index_selector("title")),
        ]

        for text, cmd in categories:
            btn = tk.Button(
                left_side,
                text=text,
                font=("Arial", 10),
                bg="#F8F9FA",
                fg="#495057",
                bd=0,
                anchor="w",
                cursor="hand2",
                command=cmd
            )
            btn.pack(fill="x", pady=2)

        # 라이팅 카드
        write_card = tk.Frame(self.container, bg="white", padx=30, pady=30)
        write_card.pack(side="right", fill="both", expand=True)

        tk.Label(write_card, text="새 품평 작성", font=("Arial", 18, "bold"), bg="white").pack(anchor="w", pady=(0, 20))

        # 입력 필드
        row1 = tk.Frame(write_card, bg="white")
        row1.pack(fill="x", pady=5)
        
        tk.Label(row1, text="아티스트", bg="white", font=("Arial", 10)).pack(side="left")
        self.ent_artist = tk.Entry(row1, bg="#F1F3F5", bd=0, highlightthickness=1, highlightcolor="#6200EE")
        self.ent_artist.pack(side="left", padx=10, expand=True, fill="x")

        tk.Label(row1, text="곡 제목", bg="white", font=("Arial", 10)).pack(side="left", padx=(10, 0))
        self.ent_title = tk.Entry(row1, bg="#F1F3F5", bd=0, highlightthickness=1, highlightcolor="#6200EE")
        self.ent_title.pack(side="left", padx=10, expand=True, fill="x")

        # 메모장
        tk.Label(write_card, text="분석 리포트", bg="white", font=("Arial", 10)).pack(anchor="w", pady=(10, 5))
        self.txt_content = tk.Text(write_card, bg="#F1F3F5", bd=0, font=("Pretendard", 11), highlightthickness=1, highlightcolor="#6200EE", padx=10, pady=10)
        self.txt_content.pack(fill="both", expand=True, pady=10)

        # 하단 버튼
        btn_row = tk.Frame(write_card, bg="white")
        btn_row.pack(fill="x")
        
        save_btn = tk.Button(btn_row, text="품평 등록하기", font=("Pretendard", 10, "bold"),
                            fg="white", bg="#1B0046", padx=20, pady=8, bd=0, command=self.save_post)
        save_btn.pack(side="right")
        
        temp_btn = tk.Button(btn_row, text="임시 저장", font=("Pretendard", 10),
                            fg="#6200EE", bg="white", bd=0, padx=15)
        temp_btn.pack(side="right", padx=10)


    def show_list(self, field=None, keyword=None):
        self.clear_container()

        frame = tk.Frame(self.container, bg="#F8F9FA")
        frame.pack(fill="both", expand=True)

        title_text = "전체 품평 목록"
        if field and keyword:
            title_text = f"{field} : {keyword} 조회 결과"

        tk.Label(
            frame,
            text=title_text,
            font=("Arial", 18, "bold"),
            bg="#F8F9FA"
        ).pack(anchor="w", pady=(0, 20))

        list_frame = tk.Frame(frame, bg="#F8F9FA")
        list_frame.pack(fill="both", expand=True)

        posts = self.posts

        if field and keyword:
            posts = [
                p for p in self.posts
                if self.get_initial(p[field][0]) == keyword
            ]

        if not posts:
            tk.Label(
                list_frame,
                text="조회된 품평이 없습니다.",
                bg="#F8F9FA",
                fg="#868E96"
            ).pack()
            return

        for post in reversed(posts):
            card = tk.Frame(list_frame, bg="white", padx=20, pady=15)
            card.pack(fill="x", pady=8)

            tk.Label(
                card,
                text=f"{post['artist']} - {post['title']}",
                font=("Arial", 12, "bold"),
                bg="white"
            ).pack(anchor="w")

            tk.Label(
                card,
                text=post["content"],
                font=("Arial", 10),
                bg="white",
                wraplength=800,
                justify="left"
            ).pack(anchor="w", pady=(8, 0))


    def save_post(self):
        artist = self.ent_artist.get().strip()
        title = self.ent_title.get().strip()
        content = self.txt_content.get("1.0", tk.END).strip()

        # 빈 값 체크
        if not artist or not title or not content:
            messagebox.showwarning("입력 오류", "모든 항목을 입력해주세요.")
            return


        # 금지 키워드 체크
        forbidden = ["트리플에스", "엔믹스", "아일릿", "뉴진스"]
        for word in forbidden:
            if word in content or word in artist:
                messagebox.showerror(
                    "차단 알림",
                    f"'{word}'와 같은 가수 정보는 기재할 수 없습니다.\n음악 요소에 집중해주세요!"
                )
                return

        # 🔹 실제 저장
        post = {
            "id": self.post_id_counter,
            "artist": artist,
            "title": title,
            "content": content
        }

        self.posts.append(post)
        self.post_id_counter += 1

        # 입력창 초기화
        self.ent_artist.delete(0, tk.END)
        self.ent_title.delete(0, tk.END)
        self.txt_content.delete("1.0", tk.END)

        # 저장 확인용
        print(self.posts)

        messagebox.showinfo("성공", "품평이 성공적으로 등록되었습니다!")


    def render_posts(self, keyword=None, field=None):
        # 기존 목록 지우기
        for widget in self.post_list_frame.winfo_children():
            widget.destroy()

        posts = self.posts

        # 필터링
        if keyword and field:
            posts = [
                p for p in self.posts
                if p[field].startswith(keyword)
            ]

        # 출력
        for post in reversed(posts):
            card = tk.Frame(
                self.post_list_frame,
                bg="#F8F9FA",
                padx=15,
                pady=10
            )
            card.pack(fill="x", pady=5)

            tk.Label(
                card,
                text=f"{post['artist']} - {post['title']}",
                font=("Arial", 11, "bold"),
                bg="#F8F9FA"
            ).pack(anchor="w")

            tk.Label(
                card,
                text=post["content"],
                font=("Arial", 10),
                bg="#F8F9FA",
                wraplength=700,
                justify="left"
            ).pack(anchor="w", pady=(5, 0))


    def get_initial(self, char):
        초성 = [
            "ㄱ","ㄲ","ㄴ","ㄷ","ㄸ","ㄹ","ㅁ","ㅂ","ㅃ",
            "ㅅ","ㅆ","ㅇ","ㅈ","ㅉ","ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"
        ]
        if "가" <= char <= "힣":
            return 초성[(ord(char) - ord("가")) // 588]
        return char.upper()


    def show_index_selector(self, field):
        self.clear_container()

        frame = tk.Frame(self.container, bg="#F8F9FA")
        frame.pack(fill="both", expand=True)

        title_map = {
            "artist": "아티스트 초성 선택",
            "title": "곡 제목 초성 선택"
        }

        tk.Label(
            frame,
            text=title_map.get(field, "초성 선택"),
            font=("Arial", 18, "bold"),
            bg="#F8F9FA"
        ).pack(anchor="w", pady=(0, 20))

        btn_frame = tk.Frame(frame, bg="#F8F9FA")
        btn_frame.pack(anchor="w")


                # ── 한글 초성 ──
        korean_initials = [
            "ㄱ","ㄴ","ㄷ","ㄹ","ㅁ","ㅂ","ㅅ","ㅇ","ㅈ",
            "ㅊ","ㅋ","ㅌ","ㅍ","ㅎ"
        ]

        tk.Label(
            frame,
            text="한글",
            font=("Arial", 11, "bold"),
            bg="#F8F9FA",
            fg="#495057"
        ).pack(anchor="w", pady=(10, 5))

        ko_frame = tk.Frame(frame, bg="#F8F9FA")
        ko_frame.pack(anchor="w", pady=(0, 15))

        for i, ch in enumerate(korean_initials):
            btn = tk.Button(
                ko_frame,
                text=ch,
                width=4,
                height=2,
                font=("Arial", 10, "bold"),
                bg="white",
                bd=1,
                cursor="hand2",
                command=lambda c=ch: self.show_list(field, c)
            )
            btn.grid(row=0, column=i, padx=4, pady=4)

        # ── 영어 알파벳 ──
        english_initials = [
            "A","B","C","D","E","F","G",
            "H","I","J","K","L","M",
            "N","O","P","Q","R","S",
            "T","U","V","W","X","Y","Z"
        ]

        tk.Label(
            frame,
            text="ENGLISH",
            font=("Arial", 11, "bold"),
            bg="#F8F9FA",
            fg="#495057"
        ).pack(anchor="w", pady=(0, 5))

        en_frame = tk.Frame(frame, bg="#F8F9FA")
        en_frame.pack(anchor="w")

        for i, ch in enumerate(english_initials):
            btn = tk.Button(
                en_frame,
                text=ch,
                width=4,
                height=2,
                font=("Arial", 10, "bold"),
                bg="white",
                bd=1,
                cursor="hand2",
                command=lambda c=ch: self.show_list(field, c)
            )
            btn.grid(row=i//7, column=i%7, padx=4, pady=4)


    def show_faq(self):
        self.clear_container()

        Suggestion_email = ("문의사항 있을 시 이메일 보내주세요\n"
                            "email: hahahoho@kpopreviewrecord.com")
        
        tk.Label(self.container, text=Suggestion_email, font=("Arial", 20, "bold"), bg="#F8F9FA", padx= 300, pady= 200).pack(anchor="w")
        

if __name__ == "__main__":
    root = tk.Tk()
    # 폰트가 설치되어 있지 않을 경우를 대비해 기본 폰트 설정
    app = ModernKpopApp(root)
    root.mainloop()


