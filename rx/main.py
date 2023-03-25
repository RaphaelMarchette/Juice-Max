from tkinter import*
from awesometkinter import *
import awesometkinter as atk
import sqlite3
from sqlite3 import Error
import json

root = Tk()

class System:
    def __init__(self):
        BancoDados = 'DicionaryKV'
        extensao = '.json'
        extensao_db = '.db'
        self.titular = f'{BancoDados}{extensao}'
        self.db = f'{BancoDados}{extensao_db}'
        self.saw = self.saw()
        self.table_name     = self.table_name()
        self.table_lista    = self.table_lista()
        self.pre_columns    = self.pre_columns()
        self.pre_values     = self.pre_values()

    def saw(self):
        with open(self.titular, 'r', newline='', encoding='utf-8') as arquivo:
            saw = json.load(arquivo)
        return saw

    def table_name(self):
        x = self.saw.keys()
        for table_name in x:
            return table_name

    def table_lista(self):
        table_lista = self.saw[self.table_name]
        return table_lista

    def pre_columns(self):
        pre_columns = ()
        for k in self.table_lista[0].keys():
            pre_columns += k,
        return pre_columns

    def pre_values(self):
        pre_values = ()
        for v in self.table_lista[0].values():
            pre_values += v,
        return pre_values

class Banco:
    def ConexaoBanco(self):
        con=None
        try:
            con=sqlite3.connect(System().db)
        except Error as ex:
            print(ex)
        return con

    def dql(self,query): #select
        vcon=self.ConexaoBanco()
        c=vcon.cursor()
        c.execute(query)
        res=c.fetchall()
        vcon.close()
        return res

    def dml(self,query): #insert, update, delete
        try:
            vcon=self.ConexaoBanco()
            c=vcon.cursor()
            c.execute(query)
            vcon.commit()
            vcon.close()
        except Error as ex:
            print(ex)

class Pre_Query:
    def Update_Table(self,trv,rows):
        trv.delete(*trv.get_children())
        for i in rows:
            trv.insert('', 'end', values=i)

    def Tirar_Parentes_e_Aspas(self,query):
        query = query.replace("'","")
        query = query.replace("(","")
        query = query.replace(")","")
        return query
    
    def fechar(self,frame):
        frame.destroy()

class CRUD(Pre_Query,Banco):
    def Creat_Dados_SQL(self,trv,frame,group):
        valores = ()
        for i in range(len(group)):
            g = group[i].get()
            valores += f"{g}",
        query = f"INSERT INTO {System().table_name} {System().pre_columns} VALUES {valores}"
        self.dml(query)
        self.Read_Dados_SQL(trv)
        self.fechar(frame)

    def Read_Dados_SQL(self,trv):
        query = f"SELECT {System().pre_columns} from {System().table_name}"
        query = self.Tirar_Parentes_e_Aspas(query)
        self.Update_Table(trv,self.dql(query))

    def Update_Dados_SQL(self,trv,frame,group):
        kv = ()
        for i in range(2,len(group)):
            kv += f'{System().pre_columns[i]} = {group[i].get()}',
        query = f'UPDATE {System().table_name} SET {kv} WHERE {System().pre_columns[0]} = "{group[0].get()}"'
        query = self.Tirar_Parentes_e_Aspas(query)
        self.dml(query)
        self.Read_Dados_SQL(trv)
        self.fechar(frame)

    def Delete_Dados_SQL(self,trv,frame,group):
        excluir = f"DELETE FROM {System().table_name} WHERE {System().pre_columns[0]} ='{group[0].get()}'"
        self.dml(excluir)
        self.Read_Dados_SQL(trv)
        self.fechar(frame)

class Funcs(CRUD):
    # Separar Pesquisa
    def Separar(self,trv,q):
        q2 = q.get()
        query = f"SELECT {System().pre_columns} from {System().table_name}"
        self.Tirar_Parentes_e_Aspas(query)
        query += " WHERE tool_name LIKE '%"+q2+"%' OR tool_type LIKE '%"+q2+"%'"
        self.Update_Table(trv,self.dql(query))

    # Basicas
    def Limpa_Entry(self,group):
        for i in range(len(group)):
            group[i].set('')

    def Abrir_2_Cliks(self,trv,group):
            item = trv.item(trv.focus())
            for i in range(len(group)):
                group[i].set(item['values'][i])
    
    def zerar_lista(self):
        self.lista_exe = []

    def status(self,lista):
        if len(lista) > 0:
            lista[0].destroy()
            self.zerar_lista()

class Cor:
    def cor(self):
        self.cor =  {   '--cor-azul'        : '#116fff'   ,
            '--cor-branca'      : '#fff'      ,
            '--cor-cinza-claro' : '#ededed'   ,
            '--cor-cinza-10'    : '#333'      ,
            '--cor-cinza-8'     : '#494950'   ,
            '--cor-verde'       : '#45a049'   ,
            '--cor-vermelho'    : 'red'       ,
            '--cor-preta'       : 'black'     ,
            '--cor-laranja'     : 'orange'    ,
            '--cor-roxo'        : 'purple'    ,
            '--azul_gelo'       : '#dfe3ee'   ,
            '--azul_bebe'       : '#759fe6'   ,
            '--azul_office'     : '#107db2'   ,
            '--azul_marinho'    : '#1e3743'
            }

class validadores:
    def valid_str(self,text):
        if text == "": return True
        try:
            text = int(text)
            return False
        except:
            return text

    def valid_int(self,text):
        if text == "": return True
        try:
            text = int(text)
            return text
        except:
            return False

    def valid_float(self,text):
        if text == "": return True
        try:
            text = float(text)
            return text
        except:
            return False

    def valid_float_1_250(self,text):
        value = self.valid_float(text)
        return 1 <= value <= 250


    def valid_int_1_20(self,text):
        value = self.valid_int(text)
        return 1 <= value <= 20

    def valid_int_1_300(self,text):
        value = self.valid_int(text)
        return 1 <= value <= 300

    def valid_str_1(self,text):
        value = self.valid_str(text)
        return value

    def valid_int_0_90(self,text):
        value = self.valid_int(text)
        return 0 <= value <= 90

    def valid_int_1_8(self,text):
        value = self.valid_int(text)
        return 1 <= value <= 8

class Application(Funcs,Cor,validadores):
    def __init__(self):
        self.root = root
        self.zerar_lista()
        self.validaEntradas()
        self.cor()
        self.tela()
        self.frames_da_tela()
        self.widgrts_frame_1()
        self.widgrts_frame_2()
        root.mainloop()
    
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background=self.cor['--azul_marinho'])
        self.root.geometry("900x300")
        self.root.resizable(True,True)
        self.root.maxsize(width=1000,height=700)
        self.root.minsize(width=500,height=400)

    def frames_da_tela(self):
        self.fundo = atk.Frame3d(self.root, bg=self.cor['--azul_marinho'])
        self.fundo.place(relx=0.01, rely=0.01,relwidth=0.98, relheight=0.98)

        self.frame_1 = atk.Frame3d(self.fundo, bg=self.cor['--azul_marinho'])
        self.frame_1.place(relx=0.01, rely=0.02,relwidth=0.96, relheight=0.15)
        #self.root.configure(background=cor['--azul_gelo'])
        #self.root.configure(background=cor['--azul_marinho'])

        self.frame_2 = atk.Frame3d(self.root, bg=self.cor['--azul_marinho'])
        self.frame_2.place(relx=0.02, rely=0.18,relwidth=0.695, relheight=0.78)

    def widgrts_frame_1(self):
        bt_1 = atk.Button3d(self.frame_1, text="Criar Geometria",bg=self.cor['--azul_office'],command='')
        bt_2 = atk.Button3d(self.frame_1, text="Criar Ferramenta",bg=self.cor['--azul_office'],command=self.Criar_Frame_4)
        bt_3 = atk.Button3d(self.frame_1, text="Criar Operacões",bg=self.cor['--azul_office'],command='')
        bt_4 = atk.Button3d(self.frame_1, text="Pos Processar",bg=self.cor['--azul_office'],command='')

        bt_1.place(relx=0.01 ,rely=0.1, relwidth=0.15,relheight=0.8)
        bt_2.place(relx=0.17 ,rely=0.1, relwidth=0.15,relheight=0.8)
        bt_3.place(relx=0.33 ,rely=0.1, relwidth=0.15,relheight=0.8)
        bt_4.place(relx=0.49 ,rely=0.1, relwidth=0.15,relheight=0.8)

    def widgrts_frame_2(self):
        self.trv = ttk.Treeview(self.frame_2, columns=(0,1,2,3,4,5,6),show='headings', height='13')
        self.trv.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        for i in range(len(System().pre_columns)):
            self.trv.heading(i,text=System().pre_values[i])
            self.trv.column(i, width=50)


        self.scroolLista = Scrollbar(self.frame_2,orient='vertical')
        self.trv.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96,rely=0.1,relwidth=0.02,relheight=0.85)

        #listar_values_tools_Json(trv)
        self.Read_Dados_SQL(self.trv)
        self.trv.bind('<Double 1>',lambda e:(self.Criar_Frame_3(1),self.Abrir_2_Cliks(self.trv,self.group_var)))

    def Criar_Frame_3(self,modelo):
        self.status(self.lista_exe)
        self.frame_3 = atk.Frame3d(self.fundo, bg=self.cor['--azul_marinho'])
        self.frame_3.place(relx=0.73, rely=0.175,relwidth=0.26, relheight=0.8)

        if modelo == 1:
            self.group_var = []
            self.group_var.append(StringVar())
            self.group_var.append(StringVar())
        self.lista_exe.append(self.frame_3)
        self.widgrts_frame_3(modelo)

    def widgrts_frame_3(self,modelo):
        lb_nome = Label(self.frame_3,textvariable=self.group_var[0])
        lb_tipo = Label(self.frame_3,textvariable=self.group_var[1])

        lb_tipo.place(relx=0.03 ,rely=0.03, relwidth=0.25,relheight=0.08)
        lb_nome.place(relx=0.3 ,rely=0.03, relwidth=0.4,relheight=0.08)

        for i in range(2,7):
            self.group_var.append(StringVar())
            l_1 = Label(self.frame_3,text=System().pre_values[i])

            if i == 2:
                ent = Entry(self.frame_3,textvariable=self.group_var[i],validate="key",validatecommand=self.vcmd2)

            elif i == 3:
                ent = Entry(self.frame_3,textvariable=self.group_var[i],validate="key",validatecommand=self.vcmd3)
            
            elif i == 4:
                ent = Entry(self.frame_3,textvariable=self.group_var[i],validate="key",validatecommand=self.vcmd4)

            elif i == 5:
                ent = Entry(self.frame_3,textvariable=self.group_var[i],validate="key",validatecommand=self.vcmd5)

            elif i == 6:
                ent = Entry(self.frame_3,textvariable=self.group_var[i],validate="key",validatecommand=self.vcmd6)
            else:
                ent = Entry(self.frame_3,textvariable=self.group_var[i])

            i-=0.7
            l_1.place(relx=0.1,rely=0.13*i, relwidth=0.4,relheight=0.11)
            ent.place(relx=0.5,rely=0.13*i, relwidth=0.4,relheight=0.11)

        if modelo == 1:
            bt_ok = Button(self.frame_3, text="OK",bg=self.cor['--azul_office'],fg= 'white',command=lambda:self.Update_Dados_SQL(self.trv,self.frame_3,self.group_var))

            bt_del = Button(self.frame_3, text="Delete",bg=self.cor['--azul_office'],fg= 'white', command=lambda:self.Delete_Dados_SQL(self.trv,self.frame_3,self.group_var))

            bt_ok.place(relx=0.1 ,rely=0.84, relwidth=0.3,relheight=0.12)
            bt_del.place(relx=0.5 ,rely=0.84, relwidth=0.4,relheight=0.12)

        else:
            bt_criar = Button(self.frame_3, text="Criar",bd=2,bg=self.cor['--azul_office'],fg= 'white',font= ('verdana',8,'bold'), command=lambda:self.Creat_Dados_SQL(self.trv,self.frame_3,self.group_var))
            bt_criar.place(relx=0.26 ,rely=0.84, relwidth=0.44,relheight=0.12)
        


        bt_close = Button(self.frame_3, text="X",bg=self.cor['--azul_office'],fg= 'white', command=lambda:self.fechar(self.frame_3))
        bt_close.place(relx=0.8 ,rely=0.03, relwidth=0.15,relheight=0.12)

    def Criar_1_Clik(self,group,entry_name,lb_type):
        a = entry_name
        b = lb_type
        group[0].set(a)
        #group[1].set(b)
        self.group_var[1].set(lb_type.get(ACTIVE))
        return group

    def imp(self,lb_type):
        self.group_var[1].set(lb_type.get(ACTIVE))
    
    def Criar_Frame_4(self):
        self.status(self.lista_exe)

        self.frame_4 = atk.Frame3d(self.fundo, bg=self.cor['--azul_marinho'])
        self.frame_4.place(relx=0.73, rely=0.175,relwidth=0.26, relheight=0.8)


        self.widgrts_frame_4()

        self.lista_exe.append(self.frame_4)

    def widgrts_frame_4(self):
        self.group_var = []

        self.group_var.append(StringVar())
        self.frame_tl = atk.Frame3d(self.frame_4,bg=self.cor['--azul_marinho'])
        self.frame_tl.place(relx=0 ,rely=0, relwidth=1,relheight=0.18)

        tl = Label(self.frame_4,text='Criar '+ System().table_name)

        tl.place(relx=0.1 ,rely=0.05, relwidth=0.3,relheight=0.08)

        lb = Label(self.frame_4,text=System().pre_values[0])
        entry_name = Entry(self.frame_4,textvariable=self.group_var[0])

        self.group_var.append(StringVar())
        list_type_tool=["Fresa","Esferica","Br_Centro","Br","Rosca"]

        lb_type=Listbox(self.frame_4)
        lb_guarda_type=Label(self.frame_4,textvariable=self.group_var[1])

        for tipo in list_type_tool:
            lb_type.insert(END,tipo)
        
        modelo = 0

        bt_ok = Button(self.frame_4, text="OK",bg=self.cor['--azul_office'],fg= 'white',command=lambda:(self.imp(lb_type),self.Criar_Frame_3(modelo)))
        bt_ok.place(relx=0.1 ,rely=0.84, relwidth=0.3,relheight=0.12)


        bt_close = Button(self.frame_4, text="X",bg=self.cor['--azul_office'],fg= 'white', command=lambda:self.fechar(self.frame_4))
        bt_close.place(relx=0.8 ,rely=0.03, relwidth=0.15,relheight=0.12)


        lb_type.place(relx=0.1,rely=0.2,relwidth=0.50,relheight=0.4)

        lb.place(relx=0.1,rely=0.65, relwidth=0.3,relheight=0.14)
        entry_name.place(relx=0.42,rely=0.65,relwidth=0.5,relheight=0.14)

    def validaEntradas(self):
        self.vcmd2 = (self.root.register(self.valid_float_1_250), "%P")
        self.vcmd3 = (self.root.register(self.valid_int_1_300), "%P")
        self.vcmd4 = (self.root.register(self.valid_int_0_90), "%P")
        self.vcmd5 = (self.root.register(self.valid_int_1_8), "%P")
        self.vcmd6 = (self.root.register(self.valid_int_1_20), "%P")

Application()