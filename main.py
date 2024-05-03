import flet as ft
import time
#import psycopg2
import sqlite3
#from config import host, db_name, passwordd, user


    

    
    


def main(page: ft.Page):
    
    
    page.title = "Gygole"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = 'dark'
    name_company = ft.Text('     Gygole ui', color=ft.colors.WHITE, weight=ft.FontWeight.W_900, animate_opacity=300, opacity=0)
    icon1 = ft.Icon(name=ft.icons.MENU, color=ft.colors.WHITE, animate_opacity=300, opacity=1)
    icon2 = ft.Icon(name=ft.icons.CLOSE, color=ft.colors.WHITE, animate_opacity=300, opacity=0)
    text_home = ft.Text(' Home', color=ft.colors.WHITE, weight=ft.FontWeight.W_700, animate_opacity=300, opacity=0)
    text_settings = ft.Text(' Settings', color=ft.colors.WHITE, weight=ft.FontWeight.W_700, animate_opacity=300, opacity=0)
    text_wrench = ft.Text(' Build', color=ft.colors.WHITE, weight=ft.FontWeight.W_700, animate_opacity=300, opacity=0)
    text_cloud = ft.Text(' Cloud', color=ft.colors.WHITE, weight=ft.FontWeight.W_700, animate_opacity=300, opacity=0)
    text_mail = ft.Text(' Mail', color=ft.colors.WHITE, weight=ft.FontWeight.W_700, animate_opacity=300, opacity=0)
    text_bookmark = ft.Text(' Bookmark', color=ft.colors.WHITE, weight=ft.FontWeight.W_700, animate_opacity=300, opacity=0)
    text_account = ft.Text('Account', color=ft.colors.WHITE, weight=ft.FontWeight.W_700, animate_opacity=300, opacity=0, size=50)
    account_text = ft.Text(' Account', color=ft.colors.WHITE, weight=ft.FontWeight.W_700, animate_opacity=300)
    facebook = ft.Icon(name=ft.icons.FACEBOOK, color=ft.colors.BLUE_500, size=30, animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE), scale=ft.transform.Scale(1))
    instagram = ft.Icon(name=ft.icons.LAPTOP_MAC, color=ft.colors.PINK_100, size=30, animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE), scale=ft.transform.Scale(1))
    youtube = ft.Icon(name=ft.icons.YOUTUBE_SEARCHED_FOR_SHARP, color=ft.colors.RED, size=30, animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE), scale=ft.transform.Scale(1))
    content_cont = ft.Container (
                            width=5,
                            height=5,
                            margin=ft.margin.only(-10,0),
                            offset=ft.transform.Offset(0.25,0.5),
                            animate_offset=ft.animation.Animation(700, ft.AnimationCurve.EASE),
                            animate=ft.animation.Animation(450, ft.AnimationCurve.EASE),
                            bgcolor=ft.colors.GREEN_ACCENT_700,
                            border_radius=7,   
                            animate_opacity=300,
                            padding=50,
                            opacity = 0
                        )
    
    
    
    
            
    def animate_hover_facebook(event):
        match event.data:
            case 'true':
            
                event.control.bgcolor = ft.colors.GREEN_ACCENT_700
                facebook.color=ft.colors.WHITE
                facebook.scale = ft.transform.Scale(1.250)
                page.update()
            
            case 'false':
                event.control.bgcolor = ft.colors.WHITE
                facebook.color=ft.colors.BLUE_500
                facebook.scale = ft.transform.Scale(1)
                page.update()
            
    def animate_hover_instagram(event):
        match event.data:
            case 'true':
            
                event.control.bgcolor = ft.colors.GREEN_ACCENT_700
                instagram.color=ft.colors.WHITE
                instagram.scale = ft.transform.Scale(1.250)
                page.update()
            
            case 'false':
                event.control.bgcolor = ft.colors.WHITE
                instagram.color=ft.colors.PINK_100
                instagram.scale = ft.transform.Scale(1)
                page.update()
            
    def animate_hover_youtube(event):
        match event.data:
            case 'true':
            
                event.control.bgcolor = ft.colors.GREEN_ACCENT_700
                youtube.color=ft.colors.WHITE
                youtube.scale = ft.transform.Scale(1.250)
                page.update()
            
            case 'false':
                event.control.bgcolor = ft.colors.WHITE
                youtube.color=ft.colors.RED
                youtube.scale = ft.transform.Scale(1)
                page.update()
            
            
    def animate_hover_github(event):
        match event.data:
            case 'true':
            
            
                build_cont.scale = ft.transform.Scale(1.1)
                page.update()
            
            case 'false':
                build_cont.scale = ft.transform.Scale(1)
                page.update()
            
            
    def animate_hover_cloud(event):
        match event.data:
            case 'true':
            
            
                cont_cloud.scale = ft.transform.Scale(1.1)
                page.update()
            
            case 'false':
                cont_cloud.scale = ft.transform.Scale(1)
                page.update()
            
    def animate_hover_mail(event):
        match event.data:
            case 'true':
            
            
                cont_mail.scale = ft.transform.Scale(1.1)
                page.update()
            
            case 'false':
                cont_mail.scale = ft.transform.Scale(1)
                page.update()
                
    def animate_hover_account(event):
        match event.data:
            case 'true':
            
            
                cont_account.scale = ft.transform.Scale(1.1)
                page.update()
            
            case 'false':
                cont_account.scale = ft.transform.Scale(1)
                page.update()
                
    def exit_to_reg_and_auth(event):
        home_text2.value = 'Welcome to\nGygole UI!'
        cont_account.opacity = 0
        page.update()
        time.sleep(0.1)
        
        cont_account.padding = ft.padding.only(0,10)
        exit_btn.opacity = 0
        name.opacity = 0
        reg_entry_name.opacity = 0
        passw.opacity = 0
        reg_entry_pass.opacity = 0
        reg_button.opacity = 0
        page.update()
        time.sleep(0.2)
        cont_account.height=180
        page.update()
        exit_btn.scale = ft.transform.Scale(0.9)
        page.update()
        time.sleep(0.1)
        exit_btn.scale = ft.transform.Scale(1)
        page.update()
        
        
        time.sleep(0.1)
        cont_account.content = ft.Column([
            regist_cont,
            auth_cont
        ])
        page.update()
        time.sleep(0.1)
        
        regist_cont.opacity = 1
        page.update()
        time.sleep(0.250)
        auth_cont.opacity = 1
        page.update()
        time.sleep(0.1)
        cont_account.opacity = 1
        cont_account.height=180
        page.update()
        
    def auth_account(event):
        
        try:
            connection = sqlite3.connect(
                #psycopg2.connect()
                #dbname=db_name,
                #host=host,
                #password=passwordd,
                #user=user
                'gygolebase.db'
            )
            connection.autocommit = True

            #with connection.cursor() as cursor:
            cursor = connection.cursor()
            cursor.execute('''SELECT username, password, id FROM users''')
            existing_credentials = cursor.fetchall()

            for username, password, id in existing_credentials:
                if auth_entry_name.value == username and auth_entry_pass.value == password:
                    cont_account.height=325
                    cont_account.opacity = 0
                    page.update()
                    time.sleep(0.5)
                    cont_account.padding = ft.padding.only(10,25)
                    cont_account.content = ft.Column([
                        ft.Text('Информация о аккаунте:', color=ft.colors.BLACK, size=20, weight=ft.FontWeight.W_900),
                        ft.Text(f'Никнейм: {auth_entry_name.value}', color=ft.colors.BLACK, size=15, weight=ft.FontWeight.W_800,),
                        ft.Text(f'Пароль: {auth_entry_pass.value}', color=ft.colors.BLACK, size=15, weight=ft.FontWeight.W_800,),
                        ft.Text(f'Ваш ID: {id}', color=ft.colors.BLACK, size=15, weight=ft.FontWeight.W_800,),
                        ft.Container(
                            bgcolor=ft.colors.WHITE,
                            shadow=ft.BoxShadow(
                                blur_radius=2
                            ),
                            border_radius=10,
                            width=140,
                            height=60,
                            alignment=ft.alignment.center,
                            on_click = exit_to_reg_and_auth,
                            padding=ft.padding.only(15,0),
                            content=ft.Stack([
                                ft.Text('Выйти из аккаунта', color=ft.colors.BLACK, size=15, weight=ft.FontWeight.W_800,)
                            ])
                        )
                    ])
                    home_text2.value = f'Welcome to Gygole UI\n{auth_entry_name.value}!'
                    cont_account.opacity = 1
                    page.update()
                    break
            else:
                cont_account.height=400
                home_text2.value = f'Welcome to Gygole UI!'
                cont_account.content = ft.Column([
                        exit_btn,
                        name,
                        auth_entry_name,
                        passw,
                        auth_entry_pass,
                        auth_button,
                        ft.Text('Неверные\nданные', color=ft.colors.RED, size=20, weight=ft.FontWeight.W_800)
                    ])
                page.update()
            
            connection.close()

        except Exception as ex:
            print('Ошибка:', ex)
        
        
            
        
        
    def reg_account(event):
        
        try:
            connection = sqlite3.connect(
            #dbname=db_name,
            #host=host,
            #password=passwordd,
            #user=user
            'gygolebase.db'
            )
            connection.autocommit = True
    
            #with connection.cursor() as cursor:
            cursor = connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    Id INTEGER,
                    UserName VARCHAR(30),
                    Password VARCHAR(30),
                    PRIMARY KEY(id)
                )  
            ''')
        

            
                
            
                
            cursor.execute(f'''INSERT INTO users(username, password) VALUES ('{reg_entry_name.value}','{reg_entry_pass.value}');
                               ''')
            cont_account.padding=ft.padding.only(10,15)
            cont_account.height = 375
            cont_account.content = ft.Column([
                    exit_btn,
                    name,
                    reg_entry_name,
                    passw,
                    reg_entry_pass,
                    reg_button,
                    ft.Text(f'Новый аккаунт: {reg_entry_name.value}', color=ft.colors.GREEN, size=15, weight=ft.FontWeight.W_800)
                ])
            page.update()
            connection.close()
                    

                
            
                
                    
                
                
                    
                    
                
            
                
                
            
            
            
    
        
        

        except Exception as ex:
            print('Ошибка:', ex)
            
    auth_entry_name = ft.CupertinoTextField(bgcolor=ft.colors.WHITE, border=5, focused_border_color=ft.colors.BLACK, width=140, color=ft.colors.BLACK,animate_opacity=500,)  
    auth_entry_pass = ft.CupertinoTextField(bgcolor=ft.colors.WHITE, border=5, focused_border_color=ft.colors.BLACK, width=140, color=ft.colors.BLACK,animate_opacity=500,)  
    auth_button = ft.Container (
        bgcolor=ft.colors.WHITE,
        shadow=ft.BoxShadow(
            blur_radius=3
        ),
        width=140,
        height=60,
        border_radius=10,
        alignment=ft.alignment.center,
        on_click=auth_account,
        animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE),
        animate_opacity=500,
        content=ft.Stack([
            ft.Text('Войти', size=20, color=ft.colors.BLACK, weight=ft.FontWeight.W_800)
        ])
    )
            
    def auth_account_info(event):
        
        cont_account.height=325
        page.update()
        time.sleep(0.2)
        regist_cont.opacity = 0
        page.update()
        time.sleep(0.250)
        auth_cont.opacity = 0
        page.update()
        time.sleep(0.2)
        cont_account.content = ft.Column([
            exit_btn,
            name,
            auth_entry_name,
            passw,
            auth_entry_pass,
            auth_button
        ])
        page.update()
        time.sleep(0.2)
        exit_btn.opacity = 1
        name.opacity = 1
        reg_entry_name.opacity = 0
        passw.opacity = 1
        reg_entry_pass.opacity = 0
        reg_button.opacity = 0
        
        
        
        auth_entry_name.opacity = 1
        
        auth_entry_pass.opacity = 1
        auth_button.opacity = 1
        page.update()
            
    
    
    exit_btn = ft.Container (
        width=50,
        height=50,
        border_radius=25,
        
        bgcolor=ft.colors.WHITE,
        alignment=ft.alignment.center,
        animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE),
        shadow=ft.BoxShadow(
            blur_radius=2
        ),
        on_click = exit_to_reg_and_auth,
        animate_opacity=500,
        content=ft.Stack([
            ft.Icon(name=ft.icons.EXIT_TO_APP, color=ft.colors.BLACK)
        ])
        
    )
    name = ft.Text('Никнейм', size=20, color=ft.colors.BLACK, weight=ft.FontWeight.W_800,animate_opacity=500,)
    reg_entry_name = ft.CupertinoTextField(bgcolor=ft.colors.WHITE, border=5, focused_border_color=ft.colors.BLACK, width=140, color=ft.colors.BLACK,animate_opacity=500,)  
    passw = ft.Text('Пароль', size=20, color=ft.colors.BLACK, weight=ft.FontWeight.W_800,animate_opacity=500,)
    reg_entry_pass = ft.CupertinoTextField(bgcolor=ft.colors.WHITE, border=5, focused_border_color=ft.colors.BLACK, width=140, color=ft.colors.BLACK,animate_opacity=500,)  
    reg_button = ft.Container (
        bgcolor=ft.colors.WHITE,
        shadow=ft.BoxShadow(
            blur_radius=3
        ),
        width=140,
        height=60,
        border_radius=10,
        alignment=ft.alignment.center,
        on_click=reg_account,
        animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE),
        animate_opacity=500,
        content=ft.Stack([
            ft.Text('Создать', size=20, color=ft.colors.BLACK, weight=ft.FontWeight.W_800)
        ])
    )
    def new_account(event):
        
        cont_account.height=325
        page.update()
        time.sleep(0.2)
        regist_cont.opacity = 0
        page.update()
        time.sleep(0.250)
        auth_cont.opacity = 0
        page.update()
        time.sleep(0.2)
        cont_account.content = ft.Column([
            exit_btn,
            name,
            reg_entry_name,
            passw,
            reg_entry_pass,
            reg_button
        ])
        page.update()
        time.sleep(0.2)
        exit_btn.opacity = 1
        name.opacity = 1
        reg_entry_name.opacity = 1
        passw.opacity = 1
        reg_entry_pass.opacity = 1
        reg_button.opacity = 1
        
        
       
        auth_entry_name.opacity = 0
        
        auth_entry_pass.opacity = 0
        auth_button.opacity = 0
        page.update()
    
    
    home = ft.Container (
        bgcolor=ft.colors.GREEN_ACCENT_700,
        border_radius=10,
        height=50,
        width=50,
        opacity=1,
        animate_opacity=300,
        padding=ft.padding.only(12.5,0),
        animate=ft.animation.Animation(300, ft.AnimationCurve.EASE),
        
        on_click= lambda e: page.go('/home'),
        content=ft.Row([
            ft.Icon(name=ft.icons.HOME, color=ft.colors.WHITE),
            text_home
        ])
    )
    
    
    home_cont = ft.Container (
                        animate_offset=ft.animation.Animation(450, ft.AnimationCurve.EASE),
                        padding=ft.padding.only(15,0),
                        content=ft.Column([
                            home,
                            
                        ])
                    )
    
    settings = ft.Container (
        bgcolor=ft.colors.GREEN_ACCENT_700,
        border_radius=10,
        height=50,
        width=50,
        opacity=1,
        animate_opacity=300,
        animate=ft.animation.Animation(300, ft.AnimationCurve.EASE),
        padding=ft.padding.only(12.5,0),
        
        on_click= lambda e: page.go('/settings'),
        content=ft.Row([
            ft.Icon(name=ft.icons.SETTINGS, color=ft.colors.WHITE),
            text_settings
        ])
    )
    
    settings_cont = ft.Container (
                        animate_offset=ft.animation.Animation(450, ft.AnimationCurve.EASE),
                        padding=ft.padding.only(15,0),
                        content=ft.Column([
                            settings,
                            
                        ])
                    )
    
    wrench = ft.Container (
        bgcolor=ft.colors.GREEN_ACCENT_700,
        border_radius=10,
        height=50,
        width=50,
        opacity=1,
        animate_opacity=300,
        animate=ft.animation.Animation(300, ft.AnimationCurve.EASE),
        padding=ft.padding.only(12.5,0),
        
        on_click= lambda e: page.go('/build'),
        content=ft.Row([
            ft.Icon(name=ft.icons.BUILD, color=ft.colors.WHITE),
            text_wrench
        ])
    )
    
    wrench_cont = ft.Container (
                        animate_offset=ft.animation.Animation(450, ft.AnimationCurve.EASE),
                        padding=ft.padding.only(15,0),
                        content=ft.Column([
                            wrench,
                            
                        ])
                    )
    
    cloud = ft.Container (
        bgcolor=ft.colors.GREEN_ACCENT_700,
        border_radius=10,
        height=50,
        width=50,
        opacity=1,
        animate_opacity=300,
        animate=ft.animation.Animation(300, ft.AnimationCurve.EASE),
        padding=ft.padding.only(12.5,0),
        
        on_click= lambda e: page.go('/cloud'),
        content=ft.Row([
            ft.Icon(name=ft.icons.CLOUD, color=ft.colors.WHITE),
            text_cloud
        ])
    )
    
    cloud_cont = ft.Container (
                        animate_offset=ft.animation.Animation(450, ft.AnimationCurve.EASE),
                        padding=ft.padding.only(15,0),
                        content=ft.Column([
                            cloud,
                            
                        ])
                    )
    
    mail = ft.Container (
        bgcolor=ft.colors.GREEN_ACCENT_700,
        border_radius=10,
        height=50,
        width=50,
        opacity=1,
        animate_opacity=300,
        animate=ft.animation.Animation(300, ft.AnimationCurve.EASE),
        padding=ft.padding.only(12.5,0),
        
        on_click= lambda e: page.go('/mail'),
        content=ft.Row([
            ft.Icon(name=ft.icons.EMAIL, color=ft.colors.WHITE),
            text_mail
        ])
    )
    
    mail_cont = ft.Container (
                        animate_offset=ft.animation.Animation(450, ft.AnimationCurve.EASE),
                        padding=ft.padding.only(15,0),
                        content=ft.Column([
                            mail
                        ])
                    )
    
    bookmark = ft.Container (
        bgcolor=ft.colors.GREEN_ACCENT_700,
        border_radius=10,
        height=50,
        width=50,
        opacity=1,
        animate_opacity=300,
        animate=ft.animation.Animation(300, ft.AnimationCurve.EASE),
        padding=ft.padding.only(12.5,0),
       
        on_click= lambda e: page.go('/bookmark'),
        content=ft.Row([
            ft.Icon(name=ft.icons.BOOKMARK, color=ft.colors.WHITE),
            text_bookmark
        ])
    )
    
    bookmark_cont = ft.Container (
                        animate_offset=ft.animation.Animation(450, ft.AnimationCurve.EASE),
                        padding=ft.padding.only(15,0),
                        content=ft.Column([
                            bookmark
                        ])
                    )
    
    account = ft.Container (
        bgcolor=ft.colors.GREEN_ACCENT_700,
        border_radius=10,
        height=50,
        width=50,
        opacity=1,
        animate_opacity=300,
        animate=ft.animation.Animation(300, ft.AnimationCurve.EASE),
        padding=ft.padding.only(12.5,0),
       
        on_click= lambda e: page.go('/account'),
        content=ft.Row([
            ft.Icon(name=ft.icons.ACCOUNT_BOX, color=ft.colors.WHITE),
            account_text
        ])
    )
    
    account_cont = ft.Container (
                        animate_offset=ft.animation.Animation(450, ft.AnimationCurve.EASE),
                        padding=ft.padding.only(15,0),
                        content=ft.Column([
                            account
                        ])
                    )
    
    
    def close_menu_bar(event):
        
        
        icon2.opacity = 0
        text_home.opacity = 0
        text_settings.opacity = 0
        text_wrench.opacity = 0
        text_mail.opacity = 0
        text_cloud.opacity = 0
        text_bookmark.opacity = 0
        account_text.opacity = 0
        home_cont.opacity = 0
        settings_cont.opacity = 0
        wrench_cont.opacity = 0
        cloud_cont.opacity = 0
        mail_cont.opacity = 0
        bookmark_cont.opacity = 0
        account_cont.opacity = 0
        
        name_company.opacity = 0
        page.update()
        time.sleep(0.1)
        home_cont.offset=ft.transform.Offset(0,0)
        home.width=50
        settings_cont.offset=ft.transform.Offset(0,0)
        settings.width=50
        wrench_cont.offset=ft.transform.Offset(0,0)
        wrench.width=50
        cloud_cont.offset=ft.transform.Offset(0,0)
        cloud.width=50
        mail_cont.offset=ft.transform.Offset(0,0)
        mail.width=50
        bookmark_cont.offset=ft.transform.Offset(0,0)
        bookmark.width=50
        account_cont.offset=ft.transform.Offset(0,0)
        account.width=50
        time.sleep(0.1)
        
        menu_bar.width=75
       
        content_cont.opacity = 1

        menu_bar.content = ft.Stack ([
                    ft.Column([
                        bar,
                        home_cont,
                        settings_cont,
                        wrench_cont,
                        cloud_cont,
                        mail_cont,
                        bookmark_cont,
                        account_cont
                        
                    ])
                ])
        
        page.update()
        time.sleep(0.1)
        icon1.opacity = 1
        home.opacity = 1
        settings.opacity = 1
        wrench.opacity = 1
        cloud.opacity = 1
        mail.opacity = 1
        bookmark.opacity = 1
        account.opacity = 1
        home_cont.opacity = 1
        settings_cont.opacity = 1
        wrench_cont.opacity = 1
        cloud_cont.opacity = 1
        mail_cont.opacity = 1
        bookmark_cont.opacity = 1
        account_cont.opacity = 1
        page.update()
        
        
        
    def open_menu_bar(event):
                
                home.opacity = 0
                settings.opacity = 0
                wrench.opacity = 0
                cloud.opacity = 0
                mail.opacity = 0
                bookmark.opacity = 0
                account.opacity = 0
                icon1.opacity = 0
                
                page.update()
                time.sleep(0.2)
                menu_bar.width=250
                content_cont.opacity = 0.5
                home_cont.offset=ft.transform.Offset(0.170,0)
                settings_cont.offset=ft.transform.Offset(0.170,0)
                wrench_cont.offset=ft.transform.Offset(0.170,0)
                cloud_cont.offset=ft.transform.Offset(0.170,0)
                mail_cont.offset=ft.transform.Offset(0.170,0)
                bookmark_cont.offset=ft.transform.Offset(0.170,0)
                account_cont.offset=ft.transform.Offset(0.170,0)
                page.update()
                time.sleep(0.1)
                
                home.width=190
                settings.width=190
                wrench.width=190
                cloud.width=190
                mail.width=190
                bookmark.width=190
                account.width=190
                page.update()
                time.sleep(0.1)
                
                
                
                page.update()
                
                
                
                
                
                time.sleep(0.2)
                
        
                close_bar.width=250
                menu_bar.content = ft.Stack ([
                    ft.Column([
                        close_bar,
                        home_cont,
                        settings_cont,
                        wrench_cont,
                        cloud_cont,
                        mail_cont,
                        bookmark_cont,
                        account_cont
                        
                    ])
                ])
                
                page.update()
                time.sleep(0.1)
                icon2.opacity = 1
                
                name_company.opacity = 1
                page.update()
                time.sleep(0.1)
                home.opacity = 1
                settings.opacity = 1
                wrench.opacity = 1
                cloud.opacity = 1
                mail.opacity = 1
                bookmark.opacity = 1
                account.opacity = 1
                
                
                text_home.opacity = 1
                text_settings.opacity = 1
                text_wrench.opacity = 1
                text_mail.opacity = 1
                text_cloud.opacity = 1
                text_bookmark.opacity = 1
                account_text.opacity = 1
                
                page.update()
                
    bar = ft.Container (
                
                alignment=ft.alignment.Alignment(-0,0),
                
                bgcolor=ft.colors.GREEN_300,
                
                width = 250,
                height = 75,
                animate=ft.animation.Animation(300, ft.AnimationCurve.EASE),
                on_click=open_menu_bar,
                
                content=ft.Stack([
                    icon1
                    
                    
                        
                
                    
                    
                ])
    )
            
    
    close_bar = ft.Container (
                
                
                alignment=ft.alignment.Alignment(-0.1,0),
                bgcolor=ft.colors.GREEN_300,
                
                width=250,
                height=75,
                animate=ft.animation.Animation(300, ft.AnimationCurve.EASE),
                on_click=close_menu_bar,
                
                content=ft.Stack([
                    ft.Container (
                        offset=ft.transform.Offset(0.250,0),
                        content=ft.Row([
                            
                            icon2,
                            name_company
                        ])
                    )
                    
                    
                ])
            )
    
    
    
    
    
    
    
    
    
                
            
           
                
            
    
    menu_bar = ft.Container (
        width=75,
        height=1900,
        bgcolor=ft.colors.GREEN_100,
        
        animate=ft.animation.Animation(450, ft.AnimationCurve.EASE),
        offset=ft.transform.Offset(-0.200,-0.0100),
        content=ft.Stack([
            ft.Column([
                    bar,
                    home_cont,
                    settings_cont,
                    wrench_cont,
                    cloud_cont,
                    mail_cont,
                    bookmark_cont,
                    account_cont
                    
                    
                    
            ])
        ])
    )
    
    text_theme = ft.Text('Dark theme', color=ft.colors.WHITE, weight=ft.FontWeight.W_800, animate_opacity=300)
    
    def theme_mode(event):
        
        page.theme_mode = (
            ft.ThemeMode.DARK
            if page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        
        time.sleep(0.2)
        text_theme.opacity = 0
        icon.opacity = 0
        page.update()
        time.sleep(0.2)
        text_theme.opacity = 1
        icon.opacity = 1
        page.update()
        text_theme.value = (
            "Light theme" if page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        
        icon.name = (ft.icons.SUNNY if page.theme_mode == ft.ThemeMode.LIGHT else ft.icons.SHIELD_MOON_SHARP)
        
        icon.color = (ft.colors.YELLOW if page.theme_mode == ft.ThemeMode.LIGHT else ft.colors.WHITE)
        page.update()
        
    
    icon = ft.Icon(
                            name=ft.icons.SUNNY, color=ft.colors.YELLOW,
                            animate_opacity=300
                            
                        )
    icon.name = (ft.icons.SUNNY if page.theme_mode == ft.ThemeMode.LIGHT else ft.icons.SHIELD_MOON_SHARP)
    
    icon.color = (ft.colors.YELLOW if page.theme_mode == ft.ThemeMode.LIGHT else ft.colors.WHITE)
    
    page.route = '/home'
    
    content_cont.opacity = 1
    
    
    build_cont = ft.Container (
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    border_radius = 10,
                    width=150,
                    height=150,
                    on_click = lambda e: page.launch_url('https://github.com/alisherkamalov'),
                    content = ft.Stack([
                        ft.Text('GitHub', color=ft.colors.BLACK, weight=ft.FontWeight.W_900, size=30)
                    ]), 
                    opacity=0, 
                    animate_opacity=300,
                    animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE),
                    on_hover=animate_hover_github
                )
    
    cont_cloud = ft.Container (
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    alignment=ft.alignment.center,
                    width=210,
                    height=150,
                    on_click = lambda e: page.launch_url('https://www.cloudflare.com'),
                    content=ft.Stack([
                        ft.Image(src='https://avatars.mds.yandex.net/get-entity_search/2331613/575518760/S122x122Fit_2x')
                    ]), 
                    opacity=0, 
                    animate_opacity=300,
                    animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE),
                    on_hover=animate_hover_cloud
                )
    
    cont_mail = ft.Container (
                    width=210,
                    height=150,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    content=ft.Stack([
                        ft.Text('alisherkamal404@\ngmail.com', color=ft.colors.BLACK, weight=ft.FontWeight.W_900, size=20)
                    ]), 
                    opacity=0, 
                    animate_opacity=300,
                    animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE),
                    on_hover=animate_hover_mail
                )
    
    regist_cont = ft.Container (
                            bgcolor=ft.colors.WHITE,
                            width=160,
                            height=70,
                            
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(35,-5),
                            shadow=ft.BoxShadow(
                                blur_radius=2,
                                color=ft.colors.BLACK
                            ),
                            content=ft.Stack([
                                ft.Text('Создать аккаунт', color=ft.colors.BLACK, size=20, weight=ft.FontWeight.W_800)
                            ]),
                            border_radius=10,
                            on_click=new_account,
                            animate_opacity=500
                            )
    
    auth_cont = ft.Container (
                            bgcolor=ft.colors.WHITE,
                            width=160,
                            height=70,
                            margin=ft.margin.only(0,10),
                            alignment=ft.alignment.center,
                            padding=ft.padding.only(35,-5),
                            shadow=ft.BoxShadow(
                                blur_radius=2,
                                color=ft.colors.BLACK
                            ),
                            content=ft.Stack([
                                ft.Text('Войти в аккаунт', color=ft.colors.BLACK, size=20, weight=ft.FontWeight.W_800)
                            ]),
                            border_radius=10,
                            animate_opacity=500,
                            on_click=auth_account_info
                            )
    
    cont_account = ft.Container (
                    width=180,
                    height=180,
                    margin=ft.margin.only(0,5),
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.WHITE,
                    border_radius=10,
                    padding=ft.padding.only(0,10),
                    
                    content=ft.Column([
                        regist_cont,
                        auth_cont
                        
                        
                    ]), 
                    opacity=0, 
                    animate_opacity=300,
                    animate=ft.animation.Animation(300, ft.AnimationCurve.EASE),
                    animate_scale=ft.animation.Animation(300, ft.AnimationCurve.EASE),
                    on_hover=animate_hover_account
                )
    
    home_text2 = ft.Text('Welcome to\nGygole UI!', color=ft.colors.WHITE, weight=ft.FontWeight.W_800, size=30, opacity=0, animate_opacity=300)
    
    def route_change(route):
        
        content_cont.content = ft.Stack ([
                ft.Text('', color=ft.colors.WHITE, weight=ft.FontWeight.W_900, size=50)
            ])
        page.add(
        ft.Stack([
                    
                    content_cont,
                    menu_bar,
                    
                ]),
            )
        page.update()
        time.sleep(0.250)
        content_cont.offset=ft.transform.Offset(0.25,0)
        content_cont.width=1000
        content_cont.height=1450
        page.update()
        
        home_text = ft.Text('Home', color=ft.colors.WHITE, weight=ft.FontWeight.W_900, size=50, opacity=0, animate_opacity=300)
        
        settings_text = ft.Text('Settings', color=ft.colors.WHITE, weight=ft.FontWeight.W_900, size=50, opacity=0, animate_opacity=300)
        bookmark_text = ft.Text('Book\nmark', color=ft.colors.WHITE, weight=ft.FontWeight.W_900, size=50, opacity=0, animate_opacity=300)
        mail_text = ft.Text('Mail', color=ft.colors.WHITE, weight=ft.FontWeight.W_900, size=50, opacity=0, animate_opacity=300)
        
        
        cloud_text = ft.Text('Cloud', color=ft.colors.WHITE, weight=ft.FontWeight.W_900, size=50, opacity=0, animate_opacity=300)
        
        
        build_text = ft.Text('Build', color=ft.colors.WHITE, weight=ft.FontWeight.W_900, size=50, opacity=0, animate_opacity=300)
        
        
        cont_theme2 = ft.Container (
                            on_click=theme_mode,
                            content=ft.Row([
                                icon,
                                text_theme
                            ]), 
                            
                        )
        
        cont_theme = ft.Container (
            opacity=0, 
            animate_opacity=300,
                    content=ft.Row([
                        cont_theme2
                        
                    ])
                )
        facebook_cont = ft.Container(
                        width=50,
                        height=50,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.WHITE,
                        border_radius=30,
                        opacity=0, 
                        animate_opacity=300,
                        animate=ft.animation.Animation(300, ft.AnimationCurve.EASE),
                        on_hover=animate_hover_facebook,
                        content=ft.Stack([
                            facebook
                        ])
                    )
        
        instagram_cont = ft.Container(
                        width=50,
                        height=50,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.WHITE,
                        border_radius=30,
                        opacity=0, 
                        animate_opacity=300,
                        animate=ft.animation.Animation(300, ft.AnimationCurve.EASE),
                        on_hover=animate_hover_instagram,
                        content=ft.Stack([
                            instagram
                        ])
                    )
        
        youtube_cont = ft.Container(
                        width=50,
                        height=50,
                        alignment=ft.alignment.center,
                        bgcolor=ft.colors.WHITE,
                        border_radius=30,
                        opacity=0, 
                        animate_opacity=300,
                        animate=ft.animation.Animation(300, ft.AnimationCurve.EASE),
                        on_hover=animate_hover_youtube,
                        content=ft.Stack([
                            youtube
                        ])
                    )
        
        
        
        match page.route:
            case '/home':
                content_cont.content = ft.Column ([
                home_text, home_text2,
                ft.Row([
                    facebook_cont,
                    instagram_cont,
                    youtube_cont
                ])
            ])
            
            
                page.update()
                time.sleep(0.2)
                facebook_cont.opacity = 1
                instagram_cont.opacity = 1
                youtube_cont.opacity = 1
                home_text.opacity = 1
                home_text2.opacity = 1
                home.bgcolor = ft.colors.GREEN_ACCENT_700
                settings.bgcolor = ft.colors.GREEN_100
                wrench.bgcolor = ft.colors.GREEN_100
                cloud.bgcolor = ft.colors.GREEN_100
                mail.bgcolor = ft.colors.GREEN_100
                bookmark.bgcolor = ft.colors.GREEN_100
                account.bgcolor = ft.colors.GREEN_100
                page.update()
            
        
            case "/settings":
                content_cont.content = ft.Column ([
                    settings_text,
                    cont_theme
                ])
            
                page.update()
                time.sleep(0.2)
                cont_theme.opacity = 1
                settings_text.opacity = 1
                home.bgcolor = ft.colors.GREEN_100
                settings.bgcolor = ft.colors.GREEN_ACCENT_700
                wrench.bgcolor = ft.colors.GREEN_100
                cloud.bgcolor = ft.colors.GREEN_100
                mail.bgcolor = ft.colors.GREEN_100
                bookmark.bgcolor = ft.colors.GREEN_100
                account.bgcolor = ft.colors.GREEN_100
                page.update()
            
            
            case "/build":
                content_cont.content = ft.Column ([
                    build_text,
                    build_cont
                
                ])
            
                page.update()
                time.sleep(0.2)
                build_text.opacity = 1
                build_cont.opacity = 1
                page.update()
                time.sleep(0.2)
                home.bgcolor = ft.colors.GREEN_100
                settings.bgcolor = ft.colors.GREEN_100
                wrench.bgcolor = ft.colors.GREEN_ACCENT_700
                cloud.bgcolor = ft.colors.GREEN_100
                mail.bgcolor = ft.colors.GREEN_100
                bookmark.bgcolor = ft.colors.GREEN_100
                account.bgcolor = ft.colors.GREEN_100
                page.update()
            
           
            
        
            case "/cloud":
                content_cont.content = ft.Column ([
                    cloud_text,
                    cont_cloud
                
                ])
            
                page.update()
                time.sleep(0.2)
                cloud_text.opacity = 1
                cont_cloud.opacity = 1
                home.bgcolor = ft.colors.GREEN_100
                settings.bgcolor = ft.colors.GREEN_100
                wrench.bgcolor = ft.colors.GREEN_100
                cloud.bgcolor = ft.colors.GREEN_ACCENT_700
                mail.bgcolor = ft.colors.GREEN_100
                bookmark.bgcolor = ft.colors.GREEN_100
                account.bgcolor = ft.colors.GREEN_100
                page.update()
            
            
            
        
            case  "/mail":
                content_cont.content = ft.Column ([
                    mail_text,
                    cont_mail
                
                ])
            
                page.update()
                time.sleep(0.2)
                mail_text.opacity = 1
                cont_mail.opacity = 1
                home.bgcolor = ft.colors.GREEN_100
                settings.bgcolor = ft.colors.GREEN_100
                wrench.bgcolor = ft.colors.GREEN_100
                cloud.bgcolor = ft.colors.GREEN_100
                mail.bgcolor = ft.colors.GREEN_ACCENT_700
                bookmark.bgcolor = ft.colors.GREEN_100
                account.bgcolor = ft.colors.GREEN_100
                page.update()
                
            
           
            
            case "/bookmark":
                content_cont.content = ft.Stack ([
                    bookmark_text
                ])
            
                page.update()
                time.sleep(0.2)
                bookmark_text.opacity = 1
                home.bgcolor = ft.colors.GREEN_100
                settings.bgcolor = ft.colors.GREEN_100
                wrench.bgcolor = ft.colors.GREEN_100
                cloud.bgcolor = ft.colors.GREEN_100
                mail.bgcolor = ft.colors.GREEN_100
                bookmark.bgcolor = ft.colors.GREEN_ACCENT_700
                account.bgcolor = ft.colors.GREEN_100
                page.update()
                
            case '/account':
                text_account.opacity = 0
                cont_account.opacity = 0
                content_cont.content = ft.Column ([
                    text_account,
                    cont_account
                ])
                page.update()
                time.sleep(0.2)
                text_account.opacity = 1
                cont_account.opacity = 1
                home.bgcolor = ft.colors.GREEN_100
                settings.bgcolor = ft.colors.GREEN_100
                wrench.bgcolor = ft.colors.GREEN_100
                cloud.bgcolor = ft.colors.GREEN_100
                mail.bgcolor = ft.colors.GREEN_100
                bookmark.bgcolor = ft.colors.GREEN_100
                account.bgcolor = ft.colors.GREEN_ACCENT_700
                page.update()
                
            
        
            
        
        
        page.update()
        
        
        
        
    

    
    
    
    
    
    
    
    
    
    page.on_route_change = route_change
    page.go(page.route)
    page.update()
            
            
            
            
        
    
        
    
    
    
    #view=ft.WEB_BROWSER

ft.app(target=main,)