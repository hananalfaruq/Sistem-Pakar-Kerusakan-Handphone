import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from tkinter import font as tkfont

class SistemPakarHP:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Diagnosa Kerusakan Handphone")
        self.root.geometry("1000x700")
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.selected_symptoms = []
        self.current_page = "home"
        
        # Database Gejala
        self.symptoms = [
            {'id': 'G1', 'name': 'HP sering hidup/mati sendiri'},
            {'id': 'G2', 'name': 'HP mengeluarkan suhu panas'},
            {'id': 'G3', 'name': 'Baterai boros'},
            {'id': 'G4', 'name': 'Sinyal hilang'},
            {'id': 'G5', 'name': 'Tidak bisa dicas'},
            {'id': 'G6', 'name': 'Mati total'},
            {'id': 'G7', 'name': 'Bootloop/stuck logo'},
            {'id': 'G8', 'name': 'Sering macet'},
            {'id': 'G9', 'name': 'Tidak bisa flash ulang'},
            {'id': 'G10', 'name': 'Tidak bisa menginstall aplikasi'},
            {'id': 'G11', 'name': 'Muncul pesan aplikasi terhenti'},
            {'id': 'G12', 'name': 'Tidak bisa reset'},
            {'id': 'G13', 'name': 'HP sering hidup/mati sendiri'},
            {'id': 'G14', 'name': 'Baterai tidak bisa terisi penuh'},
            {'id': 'G15', 'name': 'HP mengeluarkan suhu panas'},
            {'id': 'G16', 'name': 'Baterai menggembung'},
            {'id': 'G17', 'name': 'Kesehatan baterai dibawah 90%'},
            {'id': 'G18', 'name': 'Layar HP retak'},
            {'id': 'G19', 'name': 'Layar HP pecah'},
            {'id': 'G20', 'name': 'Terdapat titik hitam pada layar'},
            {'id': 'G21', 'name': 'Layar HP tidak bisa disentuh'},
            {'id': 'G22', 'name': 'Layar HP tidak sensitif'},
            {'id': 'G23', 'name': 'Layar terkadang suka mati'},
            {'id': 'G24', 'name': 'Tidak ada sinyal'},
            {'id': 'G25', 'name': 'Panggilan darurat'},
            {'id': 'G26', 'name': 'Panggilan berakhir'},
            {'id': 'G27', 'name': 'No internet access'},
            {'id': 'G28', 'name': 'Error pada indikator baterai walaupun tidak dalam keadaan dicas'}
        ]
        
        # Database Kerusakan
        self.damages = {
            'T1': {
                'code': 'T1',
                'name': 'IC Power',
                'symptoms': ['G1', 'G2', 'G3', 'G4', 'G5', 'G6'],
                'solution': 'IC Power rusak memerlukan penggantian komponen. Konsultasikan dengan teknisi untuk perbaikan.',
                'description': 'IC Power adalah komponen yang mengatur distribusi daya pada handphone.'
            },
            'T2': {
                'code': 'T2',
                'name': 'IC Emmc',
                'symptoms': ['G7', 'G8', 'G9', 'G10', 'G11', 'G12'],
                'solution': 'IC Emmc rusak memerlukan repair atau penggantian. Data mungkin akan hilang.',
                'description': 'IC Emmc adalah chip penyimpanan internal handphone yang menyimpan sistem operasi dan data.'
            },
            'T3': {
                'code': 'T3',
                'name': 'Baterai Drop',
                'symptoms': ['G3', 'G6', 'G13', 'G14', 'G15', 'G16', 'G17'],
                'solution': 'Ganti baterai dengan yang baru dan original untuk performa optimal.',
                'description': 'Baterai drop terjadi ketika baterai sudah menurun performanya dan perlu diganti.'
            },
            'T4': {
                'code': 'T4',
                'name': 'LCD Rusak',
                'symptoms': ['G6', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23'],
                'solution': 'Ganti LCD dengan yang baru. Pastikan menggunakan LCD original atau kualitas bagus.',
                'description': 'LCD rusak dapat disebabkan oleh benturan fisik atau kerusakan internal.'
            },
            'T5': {
                'code': 'T5',
                'name': 'IC PA (Power Amplifier)',
                'symptoms': ['G3', 'G6', 'G24', 'G25', 'G26', 'G27'],
                'solution': 'IC PA rusak memerlukan penggantian komponen oleh teknisi berpengalaman.',
                'description': 'IC PA mengatur sinyal dan komunikasi pada handphone.'
            },
            'T6': {
                'code': 'T6',
                'name': 'IC Charging',
                'symptoms': ['G6', 'G14', 'G28'],
                'solution': 'IC Charging rusak memerlukan penggantian. Hindari menggunakan charger tidak original.',
                'description': 'IC Charging mengatur proses pengisian daya baterai handphone.'
            }
        }
        
        # Create main container
        self.main_container = tk.Frame(root, bg='#f0f0f0')
        self.main_container.pack(fill='both', expand=True)
        
        # Show home page
        self.show_home_page()
    
    def clear_frame(self):
        """Clear all widgets from main container"""
        for widget in self.main_container.winfo_children():
            widget.destroy()
    
    def show_home_page(self):
        """Display home page"""
        self.clear_frame()
        self.current_page = "home"
        
        # Header
        header_frame = tk.Frame(self.main_container, bg='#667eea', height=150)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        title_font = tkfont.Font(family="Arial", size=24, weight="bold")
        subtitle_font = tkfont.Font(family="Arial", size=12)
        
        tk.Label(header_frame, text="🔧 Sistem Pakar Diagnosa Kerusakan Handphone", 
                font=title_font, bg='#667eea', fg='white').pack(pady=(30, 10))
        tk.Label(header_frame, text="Metode Forward Chaining untuk Diagnosa Cepat dan Akurat", 
                font=subtitle_font, bg='#667eea', fg='white').pack()
        
        # Content
        content_frame = tk.Frame(self.main_container, bg='white', padx=40, pady=30)
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Info cards
        info_frame = tk.Frame(content_frame, bg='white')
        info_frame.pack(fill='x', pady=20)
        
        # Metode card
        metode_card = tk.Frame(info_frame, bg='#e8eaf6', relief='solid', bd=1, padx=20, pady=15)
        metode_card.pack(side='left', fill='both', expand=True, padx=5)
        tk.Label(metode_card, text="📱 Metode", font=('Arial', 12, 'bold'), 
                bg='#e8eaf6', fg='#667eea').pack(anchor='w')
        tk.Label(metode_card, text="Forward Chaining", font=('Arial', 10), 
                bg='#e8eaf6', wraplength=300, justify='left').pack(anchor='w', pady=5)
        
        # Domain card
        domain_card = tk.Frame(info_frame, bg='#e8f5e9', relief='solid', bd=1, padx=20, pady=15)
        domain_card.pack(side='left', fill='both', expand=True, padx=5)
        tk.Label(domain_card, text="🔧 Domain", font=('Arial', 12, 'bold'), 
                bg='#e8f5e9', fg='#4caf50').pack(anchor='w')
        tk.Label(domain_card, text="Kerusakan Handphone", font=('Arial', 10), 
                bg='#e8f5e9', wraplength=300, justify='left').pack(anchor='w', pady=5)
        
        # Damage list
        damage_frame = tk.LabelFrame(content_frame, text="Jenis Kerusakan yang Dapat Didiagnosa", 
                                     font=('Arial', 11, 'bold'), bg='white', padx=20, pady=15)
        damage_frame.pack(fill='x', pady=20)
        
        damages_list = [
            "✓ IC Power - Komponen pengatur distribusi daya",
            "✓ IC Emmc - Chip penyimpanan internal",
            "✓ Baterai Drop - Penurunan performa baterai",
            "✓ LCD Rusak - Kerusakan layar display",
            "✓ IC PA (Power Amplifier) - Pengatur sinyal komunikasi",
            "✓ IC Charging - Komponen pengisian daya"
        ]
        
        for damage in damages_list:
            tk.Label(damage_frame, text=damage, font=('Arial', 10), 
                    bg='white', anchor='w').pack(fill='x', pady=3)
        
        # Start button
        start_btn = tk.Button(content_frame, text="🚀 Mulai Diagnosa", 
                             font=('Arial', 14, 'bold'), bg='#667eea', fg='white',
                             padx=30, pady=15, cursor='hand2', relief='flat',
                             command=self.show_diagnosis_page)
        start_btn.pack(pady=20)
        
        # Footer
        footer_text = ("Sistem ini merupakan implementasi dari jurnal penelitian\n"
                      "\"Sistem Pakar Untuk Kerusakan Handphone Dengan Metode Forward Chaining\"\n"
                      "oleh Dilla Kusumawati, Fanisya Alva Mustika, dan Ni Wayan Parwati Septiani\n"
                      "Universitas Indraprasta PGRI")
        tk.Label(content_frame, text=footer_text, font=('Arial', 9), 
                bg='white', fg='#666', justify='center').pack(pady=10)
    
    def show_diagnosis_page(self):
        """Display diagnosis page"""
        self.clear_frame()
        self.current_page = "diagnosis"
        self.selected_symptoms = []
        
        # Header
        header_frame = tk.Frame(self.main_container, bg='#667eea', height=100)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        title_font = tkfont.Font(family="Arial", size=20, weight="bold")
        tk.Label(header_frame, text="🔍 Identifikasi Gejala Kerusakan", 
                font=title_font, bg='#667eea', fg='white').pack(pady=30)
        
        # Content
        content_frame = tk.Frame(self.main_container, bg='white', padx=30, pady=20)
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        tk.Label(content_frame, text="Pilih gejala-gejala yang dialami pada handphone Anda:", 
                font=('Arial', 11), bg='white', fg='#666').pack(anchor='w', pady=10)
        
        # Counter
        self.counter_frame = tk.Frame(content_frame, bg='#e8eaf6', relief='solid', bd=1, padx=20, pady=10)
        self.counter_frame.pack(fill='x', pady=10)
        self.counter_label = tk.Label(self.counter_frame, 
                                      text=f"Gejala Terpilih: 0 dari {len(self.symptoms)}", 
                                      font=('Arial', 11, 'bold'), bg='#e8eaf6', fg='#667eea')
        self.counter_label.pack()
        
        # Symptoms grid with scrollbar
        canvas_frame = tk.Frame(content_frame, bg='white')
        canvas_frame.pack(fill='both', expand=True, pady=10)
        
        canvas = tk.Canvas(canvas_frame, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Create symptom checkboxes
        self.symptom_vars = {}
        row = 0
        col = 0
        
        for symptom in self.symptoms:
            var = tk.BooleanVar()
            self.symptom_vars[symptom['id']] = var
            
            symptom_frame = tk.Frame(scrollable_frame, bg='white', relief='solid', 
                                    bd=1, padx=15, pady=10)
            symptom_frame.grid(row=row, column=col, padx=5, pady=5, sticky='ew')
            
            cb = tk.Checkbutton(symptom_frame, variable=var, bg='white',
                              command=self.update_counter)
            cb.pack(side='left')
            
            text_frame = tk.Frame(symptom_frame, bg='white')
            text_frame.pack(side='left', fill='x', expand=True, padx=10)
            
            tk.Label(text_frame, text=symptom['id'], font=('Arial', 9, 'bold'), 
                    bg='white', fg='#667eea').pack(anchor='w')
            tk.Label(text_frame, text=symptom['name'], font=('Arial', 9), 
                    bg='white', wraplength=300, justify='left').pack(anchor='w')
            
            col += 1
            if col > 1:  # 2 columns
                col = 0
                row += 1
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Buttons
        button_frame = tk.Frame(content_frame, bg='white')
        button_frame.pack(fill='x', pady=20)
        
        back_btn = tk.Button(button_frame, text="← Kembali", 
                            font=('Arial', 12, 'bold'), bg='#e0e0e0', fg='#333',
                            padx=30, pady=10, cursor='hand2', relief='flat',
                            command=self.show_home_page)
        back_btn.pack(side='left', padx=5)
        
        self.diagnose_btn = tk.Button(button_frame, text="📊 Diagnosa Sekarang", 
                                      font=('Arial', 12, 'bold'), bg='#667eea', fg='white',
                                      padx=30, pady=10, cursor='hand2', relief='flat',
                                      command=self.perform_diagnosis, state='disabled')
        self.diagnose_btn.pack(side='right', padx=5)
    
    def update_counter(self):
        """Update symptom counter"""
        count = sum(1 for var in self.symptom_vars.values() if var.get())
        self.counter_label.config(text=f"Gejala Terpilih: {count} dari {len(self.symptoms)}")
        
        if count > 0:
            self.diagnose_btn.config(state='normal', bg='#667eea')
        else:
            self.diagnose_btn.config(state='disabled', bg='#cccccc')
    
    def forward_chaining(self, selected_symptoms):
        """Forward Chaining Algorithm"""
        results = []
        
        for code, damage in self.damages.items():
            matched_symptoms = [s for s in damage['symptoms'] if s in selected_symptoms]
            match_percentage = (len(matched_symptoms) / len(damage['symptoms'])) * 100
            
            if len(matched_symptoms) > 0:
                results.append({
                    'code': damage['code'],
                    'name': damage['name'],
                    'description': damage['description'],
                    'solution': damage['solution'],
                    'matched_symptoms': matched_symptoms,
                    'match_count': len(matched_symptoms),
                    'total_symptoms': len(damage['symptoms']),
                    'confidence': match_percentage
                })
        
        results.sort(key=lambda x: x['confidence'], reverse=True)
        return results
    
    def perform_diagnosis(self):
        """Perform diagnosis using Forward Chaining"""
        selected = [sid for sid, var in self.symptom_vars.items() if var.get()]
        
        if not selected:
            messagebox.showwarning("Peringatan", "Pilih minimal satu gejala untuk diagnosa!")
            return
        
        results = self.forward_chaining(selected)
        self.show_result_page(results)
    
    def show_result_page(self, results):
        """Display result page"""
        self.clear_frame()
        self.current_page = "result"
        
        # Header
        header_frame = tk.Frame(self.main_container, bg='#4caf50', height=100)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        title_font = tkfont.Font(family="Arial", size=20, weight="bold")
        tk.Label(header_frame, text="📋 Hasil Diagnosa", 
                font=title_font, bg='#4caf50', fg='white').pack(pady=30)
        
        # Content with scrollbar
        content_frame = tk.Frame(self.main_container, bg='white')
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        canvas = tk.Canvas(content_frame, bg='white', highlightthickness=0)
        scrollbar = ttk.Scrollbar(content_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='white', padx=30, pady=20)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        if results:
            # Success alert
            alert_frame = tk.Frame(scrollable_frame, bg='#d4edda', relief='solid', 
                                  bd=1, padx=20, pady=15)
            alert_frame.pack(fill='x', pady=10)
            tk.Label(alert_frame, text=f"✓ Diagnosa Berhasil! Ditemukan {len(results)} kemungkinan kerusakan.", 
                    font=('Arial', 11, 'bold'), bg='#d4edda', fg='#155724').pack()
            
            # Display results
            for i, result in enumerate(results):
                result_frame = tk.LabelFrame(scrollable_frame, bg='white', relief='solid', 
                                            bd=2, padx=20, pady=15)
                result_frame.pack(fill='x', pady=10)
                
                # Header with confidence
                header = tk.Frame(result_frame, bg='white')
                header.pack(fill='x', pady=5)
                
                title_text = f"{'🏆 ' if i == 0 else ''}{result['name']}"
                tk.Label(header, text=title_text, font=('Arial', 14, 'bold'), 
                        bg='white').pack(side='left')
                
                confidence_color = '#4caf50' if result['confidence'] >= 80 else \
                                  '#ff9800' if result['confidence'] >= 50 else '#f44336'
                tk.Label(header, text=f"{result['confidence']:.0f}%", 
                        font=('Arial', 18, 'bold'), bg='white', 
                        fg=confidence_color).pack(side='right')
                
                tk.Label(result_frame, text=f"Kode: {result['code']}", 
                        font=('Arial', 9), bg='white', fg='#666').pack(anchor='w')
                
                # Description
                desc_frame = tk.Frame(result_frame, bg='#f0f4ff', relief='solid', 
                                     bd=1, padx=15, pady=10)
                desc_frame.pack(fill='x', pady=10)
                tk.Label(desc_frame, text=result['description'], font=('Arial', 10), 
                        bg='#f0f4ff', wraplength=800, justify='left').pack()
                
                # Matched symptoms
                symptom_frame = tk.LabelFrame(result_frame, 
                                             text=f"Gejala yang Cocok ({result['match_count']}/{result['total_symptoms']})", 
                                             font=('Arial', 10, 'bold'), bg='white', padx=15, pady=10)
                symptom_frame.pack(fill='x', pady=10)
                
                matched_text = ", ".join([s for s in result['matched_symptoms']])
                tk.Label(symptom_frame, text=matched_text, font=('Arial', 9), 
                        bg='white', fg='#667eea', wraplength=800, justify='left').pack()
                
                # Solution
                solution_frame = tk.Frame(result_frame, bg='#e3f2fd', relief='solid', 
                                         bd=1, padx=15, pady=10)
                solution_frame.pack(fill='x', pady=10)
                tk.Label(solution_frame, text="💡 Solusi:", font=('Arial', 10, 'bold'), 
                        bg='#e3f2fd').pack(anchor='w')
                tk.Label(solution_frame, text=result['solution'], font=('Arial', 10), 
                        bg='#e3f2fd', wraplength=800, justify='left').pack(anchor='w', pady=5)
            
            # Warning
            warning_frame = tk.Frame(scrollable_frame, bg='#fff3cd', relief='solid', 
                                    bd=1, padx=20, pady=15)
            warning_frame.pack(fill='x', pady=10)
            warning_text = ("⚠️ Catatan: Hasil diagnosa ini adalah prediksi berdasarkan gejala yang dipilih. "
                          "Untuk penanganan yang tepat, konsultasikan dengan teknisi profesional.")
            tk.Label(warning_frame, text=warning_text, font=('Arial', 9), 
                    bg='#fff3cd', fg='#856404', wraplength=800, justify='left').pack()
        else:
            # No results
            alert_frame = tk.Frame(scrollable_frame, bg='#f8d7da', relief='solid', 
                                  bd=1, padx=20, pady=15)
            alert_frame.pack(fill='x', pady=10)
            tk.Label(alert_frame, text="✗ Tidak ditemukan kerusakan yang cocok dengan gejala yang dipilih.", 
                    font=('Arial', 11, 'bold'), bg='#f8d7da', fg='#721c24').pack()
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Buttons
        button_frame = tk.Frame(self.main_container, bg='white', padx=30, pady=20)
        button_frame.pack(fill='x')
        
        diagnose_again_btn = tk.Button(button_frame, text="🔄 Diagnosa Lagi", 
                                       font=('Arial', 12, 'bold'), bg='#667eea', fg='white',
                                       padx=30, pady=10, cursor='hand2', relief='flat',
                                       command=self.show_diagnosis_page)
        diagnose_again_btn.pack(side='left', padx=5)
        
        home_btn = tk.Button(button_frame, text="🏠 Kembali ke Beranda", 
                            font=('Arial', 12, 'bold'), bg='#e0e0e0', fg='#333',
                            padx=30, pady=10, cursor='hand2', relief='flat',
                            command=self.show_home_page)
        home_btn.pack(side='right', padx=5)


# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = SistemPakarHP(root)
    root.mainloop()