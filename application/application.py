import io
import sys
import os
from odoo.ERP import ERP
from PIL import Image, ImageTk
from tkinter import Tk, Label, Entry, Button, Frame, ttk
import tkinter as tk
from tkinter import messagebox
 
class Application(tk.Tk):
    #Création de l'environnement

#----------------------------------------------------------------------------------------------------
#     Constructeur
#----------------------------------------------------------------------------------------------------
    
    def __init__(self):
        super().__init__()

        self.erp = ERP("db_cybervest")

        self.entry_username = tk.StringVar()
        self.entry_password = tk.StringVar()

        #Creation de la page Client
        self.title("Application CyberVest")#Titre
        self.screen_width = self.winfo_screenwidth()#Largeur fenetre
        self.screen_height = self.winfo_screenheight()#Longueur fenetre
        self.geometry(f"{self.screen_width}x{self.screen_height}+0+0")#Equation des L*l
        #---------------------------------------------------------------------------------------------------------------
        # Fond d'écran
        # Chargement de l'image avec Pillow
        fond_ecran = "images/v915-wit-012.png"
        self.image_pil = Image.open(fond_ecran)
        self.image_tk = ImageTk.PhotoImage(self.image_pil)

        # Création du Canvas pour afficher l'image
        self.canvas_FD = tk.Canvas(self, bg="white", highlightthickness=0)
        self.canvas_FD.pack(fill=tk.BOTH, expand=True)
        self.canvas_FD.create_image(0, 0, anchor=tk.NW, image=self.image_tk)

        # Création du frame client
        client = tk.Frame(self.canvas_FD, bg="", width=self.screen_width, height=self.screen_height)
        client.place(relx=0, rely=0)

        # Associer la fonction de redimensionnement à l'événement de redimensionnement de la fenêtre
        self.bind("<Configure>", self.redimensionner_image)

        # Bloquer le redimensionnement de la fenêtre
        self.resizable(False, False)

        #---------------------------------------------------------------------------------------------------------------
        # Mise en place du logo cybervest
        logo_path = "images/Logo1.png"
        self.image_pil_2 = Image.open(logo_path)
        self.image_tk_2 = ImageTk.PhotoImage(self.image_pil_2)
        self.canvas_logo = tk.Canvas(client, width=self.image_tk_2.width(), height=self.image_tk_2.height())
        self.canvas_logo.place(relx=0.03, rely=0.85, anchor='center')
        self.canvas_logo.create_image(0, 0, anchor=tk.NW, image=self.image_tk_2)
        self.iconphoto(True, self.image_tk_2)

        # Mise en place du logo cybervest
        logo_path = "images/Logo1.png"
        self.image_pil_2 = Image.open(logo_path)
        self.image_tk_2 = ImageTk.PhotoImage(self.image_pil_2)
        self.canvas_logo = tk.Canvas(self, width=self.image_tk_2.width(), height=self.image_tk_2.height())
        self.canvas_logo.place(relx=0.05, rely=0.85, anchor='center')
        self.canvas_logo.create_image(0, 0, anchor=tk.NW, image=self.image_tk_2)
        self.iconphoto(True, self.image_tk_2)
        # Mise en place du logo UIMM
        logo_path_2 = "images/logo-uimm-250x250.jpg"
        self.image_pil_3 = Image.open(logo_path_2)
        self.image_tk_3 = ImageTk.PhotoImage(self.image_pil_3)
        self.canvas_logo_2 = tk.Canvas(client, width=self.image_tk_3.width(), height=self.image_tk_3.height())
        self.canvas_logo_2.place(relx=0.08, rely=0.85, anchor='center')
        self.canvas_logo_2.create_image(0, 0, anchor=tk.NW, image=self.image_tk_3)
        #---------------------------------------------------------------------------------------------------------------

        # Création d'un bouton pour quitter l'application
        bouton_quit = tk.Button(client, text="Quitter", bg="#DAD7D7", font=("Arial", 12), command=self.destroy)
        bouton_quit.place(relx=1, rely=0.90, anchor='se')  # Positionne le bouton en bas à droite

        #Afficher La page de login
        self.login_page()


    def redimensionner_image(self, event):
        nouvelle_largeur = self.winfo_width()
        nouvelle_hauteur = self.winfo_height()

        # Redimensionnement de l'image avec Pillow
        image_redimensionnee = self.image_pil.resize((nouvelle_largeur, nouvelle_hauteur), Image.ANTIALIAS)

        # Création d'une nouvelle image Tkinter
        nouvelle_image_tk = ImageTk.PhotoImage(image_redimensionnee)

        # Configuration du Canvas avec la nouvelle taille
        self.canvas_FD.config(width=nouvelle_largeur, height=nouvelle_hauteur)

        # Affichage de la nouvelle image
        self.canvas_FD.create_image(0, 0, anchor=tk.NW, image=nouvelle_image_tk)

        # Mise à jour de la référence à l'image pour éviter la suppression
        self.canvas_FD.image = nouvelle_image_tk
        

        # Création d'un widget Canvas pour afficher l'image
        self.canvas_FD = tk.Canvas(self, width=self.image_tk.width(), height=self.image_tk.height())
        self.canvas_FD.pack(expand=tk.YES, fill=tk.BOTH)

        # Affichage de l'image en fond d'écran
        self.canvas_FD.create_image(0, 0, anchor=tk.NW, image=self.image_tk)

        # Associer la fonction de redimensionnement à l'événement de redimensionnement de la fenêtre
        self.bind("<Configure>", self.redimensionner_image)



        
#--------------------------------------------------------------------------------------------------------------------------------------------
    #Fonction Login
    def connexion(client):
        # Récupérer les informations de connexion de l'utilisateur
        username = client.entry_username.get()
        password = client.entry_password.get()

        # Connexion avec les informations fournies
        resultat_connexion = client.erp.connexion(username, password)

        # Vérifier le résultat de la connexion
        if resultat_connexion == 9:
            client.pageProd()
            client.login_frame.destroy()
        elif resultat_connexion == 10:
            client.pageLog()
            client.login_frame.destroy()
        elif resultat_connexion == 13:
            client.pageAdmin()
            client.login_frame.destroy()
        else:
            client.pageProd()
            client.login_frame.destroy()
            client.update()
            # Afficher un message d'erreur si l'identification échoue
            #messagebox.showerror("Erreur", "Identifiant ou mot de passe incorrect")

    #Création de la page login
    def login_page(client):
        # Création de la frame pour la page login
        client.login_frame = tk.Frame(client, bg="#c2bebd")
        client.login_frame.place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.2, anchor="center")

        # Création du border_frame à l'intérieur du login_frame
        client.border_frame = tk.Frame(client.login_frame, bg="#DAD7D7")
        client.border_frame.place(relx=0.013, rely=0.02, relwidth=0.975, relheight=0.96)

        # Création de tous les widgets à l'intérieur du border_frame
        client.label_username = tk.Label(client.border_frame, text="Nom d'utilisateur:", bg="#DAD7D7")
        client.label_password = tk.Label(client.border_frame, text="Mot de passe:", bg="#DAD7D7")

        client.entry_username = tk.Entry(client.border_frame)
        client.entry_password = tk.Entry(client.border_frame, show="*")
        client.button_login = tk.Button(client.border_frame, text="Connexion", command=lambda: client.connexion())

        # Placement des widgets à l'intérieur du border_frame
        client.label_username.place(relx=0.2, rely=0.2, anchor='center')
        client.label_password.place(relx=0.2, rely=0.45, anchor='center')
        client.entry_username.place(relx=0.7, rely=0.2, relwidth=0.5, relheight=0.15, anchor='center')
        client.entry_password.place(relx=0.7, rely=0.45, relwidth=0.5, relheight=0.15, anchor='center')
        client.button_login.place(relx=0.5, rely=0.8, relwidth=0.5, relheight=0.2, anchor='center')
#----------------------------------------------------------------------------------------------------
#     Méthodes page PRODUCTION
#----------------------------------------------------------------------------------------------------
        
    #Creation de la page Production
    def pageProd(client):
        
        #Création de la page
        client.page_prod_frame = tk.Frame(client,bg= "")
        client.page_prod_frame.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.6)
         
        label = Label(client.page_prod_frame, text="Production", font=('Helvetica', 24), bg=client.page_prod_frame['bg'])
        label.pack(pady=10)
 
        # Création de la grille pour afficher les articles
        client.tree = ttk.Treeview(client.page_prod_frame, columns=("Numéro d'OF", "Date", "Quantité à réaliser", "Quantité en production"), show="headings")
 
        # Configuration des en-têtes de colonnes
        client.tree.heading("Numéro d'OF", text="Numéro d'OF", command=lambda: client.sort_column("Numéro d'OF", False))
        client.tree.heading("Date", text="Date", command=lambda: client.sort_column("Date", False))
        client.tree.heading("Quantité à réaliser", text="Quantité à réaliser", command=lambda: client.sort_column("Quantité à réaliser", False))
        client.tree.heading("Quantité en production", text="Quantité en production", command=lambda: client.sort_column("Quantité en production", False))
 
        # Ajout des colonnes avec une largeur augmentée de 50%
        client.tree.column("Numéro d'OF", width=int(150 * 1.5), anchor="center")
        client.tree.column("Date", width=int(150 * 1.5), anchor="center")
        client.tree.column("Quantité en production", width=int(150 * 1.5), anchor="center")
        client.tree.column("Quantité à réaliser", width=int(150 * 1.5), anchor="center")
 
        client.tree.place(relx=0.03, rely=0.15)
 
        # Appeler la méthode pour obtenir les informations des produits et afficher le tableau
        client.affichage_tableau_prod()
 
        # Ajouter un bouton pour activer la modification du stock
        #client.modify_stock_button = Button(client, text="Modifier", command=client.modif_stock)
        #client.modify_stock_button.pack(pady=10)

 
    def affichage_tableau_prod(client):
        # Utiliser l'instance de la classe ERP
        client.erp.obtenir_informations_ordres_fabrication()
 
        # Afficher les valeurs récupérées pour le débogage
        print("OF:", client.erp.ordres_fabrication)
        print("Date ordre fabrication:", client.erp.dates_ordres_fabrication)
        print("Quantité à produire:", client.erp.quantite_a_produire)
        print("Quantité en production:", client.erp.qty_producing)
 
        # Effacer les éléments existants dans la Treeview
        for item in client.tree.get_children():
            client.tree.delete(item)
 
        # Ajouter les nouvelles données obtenues à la Treeview
        for i in range(len(client.erp.ordres_fabrication)):
            # Utiliser anchor pour centrer le texte
            client.tree.insert("", "end", values=(client.erp.ordres_fabrication[i], client.erp.dates_ordres_fabrication[i],
                                                client.erp.qty_producing[i], client.erp.quantite_a_produire[i]))
 
    def update_table_prod(client):
        # Effacer les éléments existants dans la Treeview
        for item in client.tree.get_children():
            client.tree.delete(item)
 
        # Ajouter les nouvelles données obtenues à la Treeview après mise à jour
        for i in range(len(client.erp_instance.ordres_fabrication)):
            client.tree.insert("", "end", values=(client.erp.ordres_fabrication[i], client.erp.dates_ordres_fabrication[i],
                                                client.erp.quantite_a_produire[i], client.erp.qty_producing[i]))

#----------------------------------------------------------------------------------------------------
#     Méthodes page LOGISTIQUE
#----------------------------------------------------------------------------------------------------

    def pageLog(self):
 
        # Supprime les widgets de la page de connexion
        #self.login_frame.grid_forget()
        
        self.page_log_frame = tk.Frame(self)
        self.page_log_frame.place(relx=0.3, rely=0.5, relwidth=0.5, relheight=0.5, bg = None)
 
        self.label = Label(self.page_log_frame, text="Logistique", font=('Helvetica', 24))
        self.label.pack(pady=10)
        
        # Création de la grille pour afficher les articles
        self.tree = ttk.Treeview(self.page_log_frame, columns=("Nom", "Prix", "Référence Interne", "Stock Disponible"), show="headings")
 
        # Configuration des en-têtes de colonnes
        self.tree.heading("Nom", text="Nom", command=lambda: self.sort_column_log("Nom", False))
        self.tree.heading("Prix", text="Prix", command=lambda: self.sort_column_log("Prix", False))
        self.tree.heading("Référence Interne", text="Référence Interne", command=lambda: self.sort_column_log("Référence Interne", False))
        self.tree.heading("Stock Disponible", text="Stock Disponible", command=lambda: self.sort_column_log("Stock Disponible", False))
 
        # Ajout des colonnes avec une largeur augmentée de 50%
        self.tree.column("Nom", width=int(150 * 1.5), anchor="center")
        self.tree.column("Prix", width=int(100 * 1.5), anchor="center")
        self.tree.column("Référence Interne", width=int(100 * 1.5), anchor="center")
        self.tree.column("Stock Disponible", width=int(100 * 1.5), anchor="center")
 
        self.tree.pack()
 
        # Appeler la méthode pour obtenir les informations des produits et afficher le tableau
        self.affichage_tableau_log()
 
        # Binding de l'événement de clic
        self.tree.bind("<ButtonRelease-1>", self.show_image_log)
 
        # Ajoutez la variable self.sort_order pour suivre l'état du tri (ascendant ou descendant)
        self.sort_order = {}
 
        # Configuration des en-têtes de colonnes
        columns = ("Nom", "Prix", "Référence Interne", "Stock Disponible")
        for col in columns:
            self.sort_order[col] = True  # Initialisation à True pour tri ascendant par défaut
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_column_log(c))
        
        # Ajout de la case d'entrée pour la quantité d'articles à retirer
        self.stock_entry_label = Label(self.page_log_frame, text="Affectation stock:")
        self.stock_entry_label.place(relx=0.5, rely=0.5, anchor='center')
 
        self.stock_entry = Entry(self.page_log_frame)
        self.stock_entry.place(relx=0.455, rely=0.51)
 
        # Ajout du bouton Valider
        self.validate_stock_button = tk.Button(self.page_log_frame, text="Valider", command=self.update_stock_log)
        self.validate_stock_button.place(relx=0.50, rely=0.56, anchor='center')

    # Creation et gestion bouton retour
    def Bouton_retour(self):
        self.Button_retour.place(relx=0, rely=1, anchor="sw")
    def Retour(self):
        #Fonction pour revenir sur le menu admin
        self.Button_retour.place_forget()
        self.page_prod_frame.place_forget()
        self.page_log_frame.place_forget()
        self.pageAdmin()

    # Création et fonction bouton déco
    def show_button_deconnexion(self):
        self.Button_deco.place(relx=0.92, rely=0.03)

    def deconnexion(self):
        if self.Number_page == 1:
            self.page_admin_frame.place_forget()
        elif self.Number_page == 2:
            self.page_prod_frame.place_forget()
        elif  self.Number_page == 3:     
            self.page_log_frame.place_forget() 

        self.Button_deco.place_forget()        
        self.Button_retour.place_forget()
        self.page_prod_frame.place_forget()
        self.page_log_frame.place_forget()
        self.pageAdmin()

        self.login_page()

    def affichage_tableau_log(self):
        # Utiliser l'instance de la classe ERP
        self.erp.obtenir_informations_produits()
 
        # Afficher les valeurs récupérées pour le débogage
        print("Nom des articles:", self.erp.nom_article)
        print("Prix des articles:", self.erp.prix_article)
        print("Référence Interne:", self.erp.reference_interne)
        print("Stock Disponible:", self.erp.stock_disponible)
 
        # Effacer les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Ajouter les nouvelles donné   es obtenues à la Treeview
        for i in range(len(self.erp.nom_article)):
            # Utiliser anchor pour centrer le texte
            self.tree.insert("", "end", values=(self.erp.nom_article[i], self.erp.prix_article[i],
                                                self.erp.reference_interne[i], self.erp.stock_disponible[i]))

    def update_stock_log(self):
        # Récupération de la quantité saisie dans la case d'entrée
        quantite = self.stock_entry.get()

        # Assurez-vous que la quantité est un nombre entier
        try:
            quantite = int(quantite)
        except ValueError:
            print("Veuillez saisir un nombre entier pour la quantité.")
            return

        # Stockage de la nouvelle quantité dans la variable new_stock
        self.new_stock = quantite

        # Obtenez la ligne sélectionnée
        item_selectionne = self.tree.selection()

        details_element = self.tree.item(item_selectionne)

        reference_interne = details_element['values'][2]  # 2 est l'index de la colonne "Référence Interne"
        stock_selectionne = float(details_element['values'][3])
    
        print(reference_interne)
        print(stock_selectionne)

        if not item_selectionne:
            print("Aucune ligne sélectionnée.")
            return
        
        nouvelle_quantite = quantite + stock_selectionne

        # Mise à jour du stock dans Odoo
        self.erp.modifier_stock_odoo(reference_interne, nouvelle_quantite)

        # Mise à jour de la ligne sélectionnée dans le tableau
        self.tree.item(item_selectionne, values=(details_element['values'][0], details_element['values'][1], reference_interne, nouvelle_quantite))

        # Effacement de la case d'entrée et du bouton Valider après la mise à jour
        self.stock_entry.delete(0, 'end')
        self.stock_entry.insert(0, "")

        

    def affichage_tableau_prod(self):
        # Utiliser l'instance de la classe ERP
        self.erp.obtenir_informations_ordres_fabrication()
 
        # Afficher les valeurs récupérées pour le débogage
        print("Ordre fabrication:", self.erp.ordres_fabrication)
        print("Date ordre fabrication:", self.erp.dates_ordres_fabrication)
        print("Quantité à produire:", self.erp.quantite_a_produire)
        print("Quantité en production:", self.erp.qty_producing)
 
        # Effacer les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
 
        # Ajouter les nouvelles données obtenues à la Treeview
        for i in range(len(self.erp.ordres_fabrication)):
            # Utiliser anchor pour centrer le texte
            self.tree.insert("", "end", values=(self.erp.ordres_fabrication[i], self.erp.dates_ordres_fabrication[i],
                                                self.erp.qty_producing[i], self.erp.quantite_a_produire[i]))
 
    def update_table(self):
        # Effacer les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
 
        # Ajouter les nouvelles données obtenues à la Treeview après mise à jour
        for i in range(len(self.erp_instance.ordres_fabrication)):
            self.tree.insert("", "end", values=(self.erp.ordres_fabrication[i], self.erp.dates_ordres_fabrication[i],
                                                self.erp.quantite_a_produire[i], self.erp.qty_producing[i]))
 
    def sort_column_log(client, col):
        # Obtenez l'état actuel du tri pour la colonne spécifiée
        reverse = client.sort_order[col]
 
        # Inversez l'état du tri pour la prochaine fois
        client.sort_order[col] = not reverse
 
        # Obtenez les données actuelles de la Treeview
        data = [(client.tree.set(child, "Nom"), client.tree.set(child, "Prix"), client.tree.set(child, "Référence Interne"), client.tree.set(child, "Stock Disponible"))
                for child in client.tree.get_children("")]
 
        # Triez les données en fonction de la colonne spécifiée et de l'état du tri
        col_index = ["Nom", "Prix", "Référence Interne", "Stock Disponible"].index(col)
        data.sort(key=lambda x: x[col_index], reverse=reverse)
 
        # Effacez les éléments existants dans la Treeview
        for item in client.tree.get_children():
            client.tree.delete(item)
 
        # Ajoutez les données triées à la Treeview
        for item in data:
            client.tree.insert("", "end", values=item)
   
    def update_stock_prod(client):
        # Récupération de la quantité saisie dans la case d'entrée
        quantite = client.stock_entry.get()

        # Assurez-vous que la quantité est un nombre entier
        try:
            quantite = int(quantite)
        except ValueError:
            print("Veuillez saisir un nombre entier pour la quantité.")
            return

        # Stockage de la nouvelle quantité dans la variable new_stock
        client.new_stock = quantite

        # Obtenez la ligne sélectionnée
        item_selectionne = client.tree.selection()

        if not item_selectionne:
            print("Aucune ligne sélectionnée.")
            return

        # Obtenez le nom de l'article associé à la ligne sélectionnée
        nom_article = client.tree.item(item_selectionne, "values")[0]

        # Mise à jour du stock dans Odoo
        succes = client.erp.update_odoo_stock(nom_article, quantite)

        if succes:
            # Affichage d'un message de confirmation dans le terminal
            print(f"Stock de {quantite} articles de '{nom_article}' mis à jour avec succès dans Odoo.")
        else:
            # En cas d'échec de la mise à jour dans Odoo
            print(f"Échec de la mise à jour du stock pour '{nom_article}' dans Odoo.")

        # Effacement de la case d'entrée et du bouton Valider après la mise à jour
        client.stock_entry.delete(0, 'end')
 

#----------------------------------------------------------------------------------------------------
#     Méthodes page ADMIN
#----------------------------------------------------------------------------------------------------
        
#Création de la page Admin
    def pageAdmin(self):
        #self.Number_page = 1
        # Supprime les widgets de la page de connexion
        self.login_frame.place_forget()

        #Création de la page
        self.page_admin_frame = tk.Frame(self,bg="#DAD7D7")
        self.page_admin_frame.place(relx=0, rely=0.1, relwidth=1, relheight=0.8)
        #Creation bouton pour aller page prod
        self.Button_prod = tk.Button(self.page_admin_frame, text="Production",fg="black", bg="#DAD7D7", font=("Arial", 20), command=lambda: [self.pageProd(), self.Bouton_retour()])
        self.Button_prod.place(relx=0.3, rely=0.5, anchor="center")
        #Creation bouton pour aller page logistique
        self.Button_logis = tk.Button(self.page_admin_frame, text="Logistique",fg="black", bg="#DAD7D7", font=("Arial", 20), command=lambda: [self.pageLog(), self.Bouton_retour()])
        self.Button_logis.place(relx=0.7, rely=0.5, anchor="center")

#----------------------------------------------------------------------------------------------------
#     Méthodes gestion des BOUTONS
#----------------------------------------------------------------------------------------------------
        
    def Boutton_retour(self):
        #Creation bouton pour aller retourner menu admin
        self.Button_retour = tk.Button(self, text="Retour",fg="black", bg="#DAD7D7", font=("Arial", 20), command=self.Retour)
        self.Button_retour.place(relx=0.1, rely=0.9, anchor="sw")
 
    def Retour(self):
        #Fonction pour revenir sur le menu admin
        self.Button_retour.place_forget()
 
 
    def update_table(self):
        # Effacer les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
 
        # Ajouter les nouvelles données obtenues à la Treeview après mise à jour
        for i in range(len(self.erp_instance.ordres_fabrication)):
            self.tree.insert("", "end", values=(self.erp.ordres_fabrication[i], self.erp.dates_ordres_fabrication[i],
                                                self.erp.quantite_a_produire[i], self.erp.qty_producing[i]))


    def show_image_log(self, event):
        print("Méthode show_image_log appelée.")
        
        item = self.tree.selection()[0]
        article_name = self.tree.item(item, "values")[0]
        print("Article sélectionné:", article_name)
 
        # Assurez-vous que les informations des produits sont à jour
        self.erp.obtenir_photos_produits()
 
        article_index = self.get_article_index_log(article_name)
 
        # Récupérer l'image directement depuis Odoo
        image_data = self.erp.images_stock[article_index]
 
        # Supprimer tous les widgets
        for widget in self.page_log_frame.grid_slaves():
            widget.destroy()
 
        if image_data:
            img = Image.open(io.BytesIO(image_data))
             # Redimensionner l'image (ajustez la taille selon vos besoins)
            resized_img = img.resize((400, 400), Image.BILINEAR)
            # Convertir l'image redimensionnée en ImageTk.PhotoImage
            img = ImageTk.PhotoImage(resized_img)
 
            # Afficher l'image dans un Label
            image_label = Label(self.page_log_frame, image=img)
            image_label.photo = img
            image_label.place(relx=0.7, rely=0)
 
                
    def get_article_index_log(self, article_name):
        for i, article in enumerate(self.erp.articles_log):
            if article["name"] == article_name:
                return i
        return -1  # Retourne -1 si l'article n'est pas trouvé
