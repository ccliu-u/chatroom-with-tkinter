from tkinter import *  # 导入模块，用户创建GUI界面
from PIL import Image, ImageTk  # 导入处理图像模块
import os

# 注册界面类
class RegisterPanel(object):
    # 构造方法，参数为按钮事件处理函数，从客户端main传进来，可以实现按钮回调
    def __init__(self, file_open_face, close_register_window, register_submit):
        # 初始化参数实例变量
        self.file_open_face = file_open_face
        self.close_register_window = close_register_window
        self.register_submit = register_submit
        self.file_name = ""  # 文件路径

    # 显示注册界面的实例方法
    def show_register_panel(self):
        # 声明全局变量方便，在静态函数重调用
        global register_frame
        global frames
        global imgLabel
        global numIdx

        # 创建主窗口
        self.register_frame = Tk()
        register_frame = self.register_frame  # 绑定全局变量
        # 设置背景颜色
        self.register_frame.configure(background="white")
        # 得到屏幕宽度，高度
        screen_width = self.register_frame.winfo_screenwidth()
        screen_height = self.register_frame.winfo_screenheight()
        # 声明宽度，高度变量
        width = 503
        height = 400
        # 设置窗口在屏幕局中变量
        gm_str = "%dx%d+%d+%d" % (width, height, (screen_width - width) / 2,
                                  (screen_height - 1.2 * height) / 2)
        # 设置窗口局中
        self.register_frame.geometry(gm_str)
        # 设置窗口标题
        self.register_frame.title("注册")
        # 设置窗口不能改变大小
        self.register_frame.resizable(width=False, height=False)

        self.p1 = Image.open('./button/添加头像按钮.png') 
        self.p1= self.p1.resize((40, 40), Image.ANTIALIAS)  # 指定缩放后的宽高
        self.p1 = ImageTk.PhotoImage(self.p1)

        '''
        numIdx = 9  # gif的帧数
        # 循环遍历动图的帧
        frames = [PhotoImage(file='register.gif', format='gif -index %i' % (i)) for i in range(numIdx)]
        # 创建存放gif的标签
        imgLabel = Label(self.register_frame, height=400, width=500)
        # 设置标签的位置
        imgLabel.place(x=-252, y=-200, relx=0.5, rely=0.5, relwidth=1, relheigh=0.5)
        '''

        # 加载 JPG 图像
        image = Image.open("register.jpg")
        # 调整图像大小
        image = image.resize((500, 400), Image.ANTIALIAS)
        # 将 PIL 图像转换成 Tkinter 支持的格式
        tk_image = ImageTk.PhotoImage(image)
        # 创建标签并设置图像
        img_label = Label(self.register_frame, image=tk_image, height=400, width=500)
        img_label.place(x=-252, y=-200, relx=0.5, rely=0.5, relwidth=1, relheight=0.5)
        # img_label.configure(image=tk_image)

        # 设置文本框，用户存放头像
        self.face_show = Text(self.register_frame, bg="white", height=3.5, width=7,
                                 highlightcolor="white")
        # 设置文本框不可编辑
        self.face_show.config(state=DISABLED)
        # 设置文本框的位置
        self.face_show.place(x=370, y=230)

        # 声明宽度高度，用来设置图片大小
        self.width = 50
        self.height = 50
        # 打开图片，用在注册页面文本框中显示默认头像
        img = Image.open("默认头像.png")
        # 设置图片的大小
        out = img.resize((self.width, self.height), Image.ANTIALIAS)
        img_path = os.path.join('头像', '默认头像.png')
        # 保存图片，类型为png
        out.save(img_path, 'png')

        # 把头像转换为PhotoImage类型，用于在文本框显示
        self.p2 = PhotoImage(file=img_path)
        # 设置文本框可编辑
        self.face_show.config(state=NORMAL)
        # 把头像图片插入文本框
        self.face_show.image_create(END, image=self.p2)
        # 设置文本框不可编辑
        self.face_show.config(state=DISABLED)
        # 设置文本框滑到最低
        self.face_show.see(END)

        # 设置文本标签及位置
        Label(self.register_frame, text="   用户名：", font=("等线", 11), bg="white", fg="grey") \
            .place(x=60, y=230)
        Label(self.register_frame, text="   密    码：", font=("等线", 11), bg="white", fg="grey") \
            .place(x=60, y=260)
        Label(self.register_frame, text="确认密码：", font=("等线", 11), bg="white", fg="grey") \
            .place(x=60, y=290)

        # 声明用户名，密码，确认密码变量
        self.user_name = StringVar()
        self.password = StringVar()
        self.confirm_password = StringVar()

        # 设置输入文本框和位置，用于获取用户的输入
        Entry(self.register_frame, textvariable=self.user_name, fg="black", width=30, highlightthickness=1) \
            .place(x=140, y=230)
        Entry(self.register_frame, textvariable=self.password, show="*", fg="black", width=30, highlightthickness=1) \
            .place(x=140, y=260)
        Entry(self.register_frame, textvariable=self.confirm_password, show="*", fg="black", width=30, highlightthickness=1) \
            .place(x=140, y=290)

        # 设置退出注册页面按钮及位置，按钮事件为close_register_window函数
        self.botton_quit = Button(self.register_frame, text="返回",  relief=FLAT, bg='white', fg="grey",
                               font=('等线', 11), command=self.close_register_window).place(x=4, y=370)

        self.register_frame.bind('<Return>', self.register_submit)  # 绑定注册按钮回车事件
        # 设置注册按钮及位置，按钮事件为register.submit函数
        self.botton_register = Button(self.register_frame, text="立即注册", relief="flat", bg="#00BFFF", fg="white", width=21, height=2,
                              font=('等线', 14, 'bold'), command=lambda: self.register_submit(self)).place(x=124, y=324)

        # 设置添加头像按钮及位置，事件处理为为file_open_face函数
        self.botton_file_open = Button(self.register_frame, image=self.p1, relief=FLAT, bd=0,
                                       command=self.file_open_face).place(x=430, y=235)

    '''
    # 定时器静态函数，用于刷新gif的帧
    @staticmethod
    def update(idx):
        frame = frames[idx]
        idx += 1  # 下一张的序号
        imgLabel.configure(image=frame)
        register_frame.after(200, RegisterPanel.update, idx % numIdx)  # 200毫秒之后继续执行定时器函数
        '''

    # 调用定时器函数，执行循环mainloop显示界面实例方法
    def load(self):
        # RegisterPanel.update(0)
        self.register_frame.mainloop()

    # 添加头像实例方法
    def add_face(self, file_name):
        if not os.path.exists('头像'):
            os.makedirs('头像')

        img_path = os.path.join('头像', f'{self.user_name}.png')

        self.file_name = file_name
        # 打开图片
        img = Image.open(file_name)
        # 设置图片大小
        out = img.resize((self.width, self.height), Image.ANTIALIAS)
        # 保存图片，类型为png
        out.save(img_path, 'png')
        # 把头像转化为PhotoImage
        self.p = PhotoImage(file=img_path)
        # 设置文本框可编辑
        self.face_show.config(state=NORMAL)
        self.face_show.delete('0.0', END)
        # 把头像插入文本框
        self.face_show.image_create(END, image=self.p)
        # 设置文本不可编辑
        self.face_show.config(state=DISABLED)
        # 设置文本框滑到最低
        self.face_show.see(END)

    # 关闭注册界面实例方法
    def close_register_panel(self):
        if self.register_frame == None:
            print("未显示界面")
        else:
            # 关闭注册界面
            self.register_frame.destroy()

    # 获取输入的用户名、密码、确认密码实例方法
    def get_input(self):
        return self.user_name.get(), self.password.get(), self.confirm_password.get(), self.file_name