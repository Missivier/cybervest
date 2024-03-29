import io
import sys
import os
from odoo.ERP import ERP
from PIL import Image, ImageTk
from tkinter import Tk, Label, Entry, Button, Frame, ttk
import tkinter as tk
from tkinter import messagebox
from tkinter import Canvas
 
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
        self.activated_admin = 0

        #Creation de la page self
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

        # Associer la fonction de redimensionnement à l'événement de redimensionnement de la fenêtre
        self.bind("<Configure>", self.redimensionner_image)

        # Bloquer le redimensionnement de la fenêtre
        self.resizable(False, False)

        # Initialiser et placer l'indicateur de connexion
        self.indicateur_connexion_label = Label(self, bg='yellow', fg='black', width=2, height=1)
        self.indicateur_connexion_label.place(relx=0.10, rely=0.01)
        self.text_connexion = tk.Label(self,bg='#296589', text="Etat de la connection: ", width=20, height=1)
        self.text_connexion.place(relx=0.01, rely=0.01)

        # Vérifier l'état de la connexion initiale et puis périodiquement
        self.verifier_connexion_odoo()
        #---------------------------------------------------------------------------------------------------------------
        # Mise en place du logo
        logo_path = "images/Logo1.png"
        self.image_pil_2 = Image.open(logo_path)
        self.image_tk_2 = ImageTk.PhotoImage(self.image_pil_2)
        self.canvas_logo = tk.Canvas(self, width=self.image_tk_2.width(), height=self.image_tk_2.height())
        self.canvas_logo.place(relx=0.03, rely=0.85, anchor='center')
        self.canvas_logo.create_image(0, 0, anchor=tk.NW, image=self.image_tk_2)
        self.iconphoto(True, self.image_tk_2)

        # Mise en place du logo UIMM
        logo_path_2 = "images/logo-uimm-250x250.jpg"
        self.image_pil_3 = Image.open(logo_path_2)
        self.image_tk_3 = ImageTk.PhotoImage(self.image_pil_3)
        self.canvas_logo_2 = tk.Canvas(self, width=self.image_tk_3.width(), height=self.image_tk_3.height())
        self.canvas_logo_2.place(relx=0.08, rely=0.85, anchor='center')
        self.canvas_logo_2.create_image(0, 0, anchor=tk.NW, image=self.image_tk_3)
        #---------------------------------------------------------------------------------------------------------------

        # Création d'un bouton pour quitter l'application
        bouton_quit = tk.Button(self, text="Quitter", bg="#DAD7D7", font=("Arial", 12), command=self.destroy)
        bouton_quit.place(relx=1, rely=0.90, anchor='se')  # Positionne le bouton en bas à droite
        

        #Afficher La page de login
        self.login_page()

    def verifier_connexion_odoo(self):
        # Utiliser verifier_disponibilite_odoo pour la vérification initiale
        if self.erp.verifier_disponibilite_odoo():
           self.indicateur_connexion_label.config(bg='green')
        else:
            self.indicateur_connexion_label.config(bg='red')

        # Après la connexion, utiliser est_connecte pour vérifier l'état de la connexion
        if self.erp.uid and self.erp.est_connecte():
            self.indicateur_connexion_label.config(bg='green')

        elif self.erp.uid:
            self.indicateur_connexion_label.config(bg='red')

        # Planifier la prochaine vérification
        self.after(3000, self.verifier_connexion_odoo)
        
    def deconnexion(self):
            if self.Number_page == 1:
                self.page_prod_frame.place_forget()
            elif self.Number_page == 2:
                self.page_log_frame.place_forget()
            elif self.Number_page == 3:
                self.page_admin_frame.place_forget()

            if self.activated_admin == 1:
                self.button_return.place_forget()
                self.label_admin.place_forget()
                self.activated_admin = 0

            self.bouton_quit.place_forget()
            self.label_user.place_forget()
            self.update()
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
    def connexion(self):
        # Récupérer les informations de connexion de l'utilisateur
        username = self.entry_username.get()
        password = self.entry_password.get()

        # Connexion avec les informations fournies
        resultat_connexion = self.erp.connexion(username, password)
        #resultat_connexion = 0
        # Vérifier le résultat de la connexion
        if resultat_connexion == 9:
            self.user = "Production"
            self.login_frame.place_forget()
            self.update()
            self.pageProd()
            self.user_current()

        elif resultat_connexion == 10:
            self.user = "Logistique"
            self.login_frame.place_forget()
            self.update()
            self.pageLog()
            self.user_current()

        elif resultat_connexion == 13:
            self.user = "Administateur"
            self.login_frame.place_forget()
            self.update()
            self.pageAdmin()
            self.user_current()

        else:
            #Afficher un message d'erreur si l'identification échoue
            messagebox.showerror("Erreur", "Identifiant ou mot de passe incorrect")

    #Création de la page login
    def login_page(self):
       
        # Création de la frame pour la page login
        self.login_frame = tk.Frame(self, bg="#c2bebd")
        self.login_frame.place(relx=0.5, rely=0.3, relwidth=0.2, relheight=0.2, anchor="center")

        # Création du border_frame à l'intérieur du login_frame
        self.border_frame = tk.Frame(self.login_frame, bg="#DAD7D7")
        self.border_frame.place(relx=0.013, rely=0.02, relwidth=0.975, relheight=0.96)

        # Création de tous les widgets à l'intérieur du border_frame
        self.label_username = tk.Label(self.login_frame, text="Nom d'utilisateur:", bg="#DAD7D7")
        self.label_password = tk.Label(self.login_frame, text="Mot de passe:", bg="#DAD7D7")

        self.entry_username = tk.Entry(self.login_frame)
        self.entry_password = tk.Entry(self.login_frame, show="*")
        self.button_login = tk.Button(self.login_frame, text="Connexion", command=lambda: self.connexion())

        # Placement des widgets à l'intérieur du login_frame
        self.label_username.place(relx=0.2, rely=0.2, anchor='center')
        self.label_password.place(relx=0.2, rely=0.45, anchor='center')
        self.entry_username.place(relx=0.7, rely=0.2, relwidth=0.5, relheight=0.15, anchor='center')
        self.entry_password.place(relx=0.7, rely=0.45, relwidth=0.5, relheight=0.15, anchor='center')
        self.button_login.place(relx=0.5, rely=0.8, relwidth=0.5, relheight=0.2, anchor='center')
#----------------------------------------------------------------------------------------------------
#     Méthodes page PRODUCTION
#----------------------------------------------------------------------------------------------------
        #bg="#EAF9FF"
    #Creation de la page Production
    def pageProd(self):
        self.Number_page = 1

    # Création de la page
        self.page_prod_frame = tk.Frame(self, bg="")
        self.page_prod_frame.place(relx=0, rely=0, relwidth=1, relheight=0.6)

         # Création d'un bouton pour déconnexion l'application
        self.bouton_quit = tk.Button(self.page_prod_frame, text="Déconnexion", bg="#DAD7D7", font=("Arial", 12), command= self.deconnexion)  
        self.bouton_quit.place(relx=1, rely=0.05, anchor='se')  # Positionne le bouton en haut à droite
        
        # Création du label dans le cadre self.page_prod_frame
        label = Label(self.page_prod_frame, text="Production", font=('Helvetica', 24), bg="#EAF9FF")
        label.place(relx = 0.46, rely = 0.05)
        
        # Création de la grille pour afficher les articles
        self.tree = ttk.Treeview(self.page_prod_frame, columns=("Numéro d'OF", "Date", "Quantité réalisé", "Quantité à produire"), show="headings")
 
        # Configuration des en-têtes de colonnes
        self.tree.heading("Numéro d'OF", text="Numéro d'OF", command=lambda: self.sort_column("Numéro d'OF", False))
        self.tree.heading("Date", text="Date", command=lambda: self.sort_column("Date", False))
        self.tree.heading("Quantité réalisé", text="Quantité réalisé", command=lambda: self.sort_column("Quantité réalisé", False))
        self.tree.heading("Quantité à produire", text="Quantité à produire", command=lambda: self.sort_column("Quantité à produire", False))
 
        # Ajout des colonnes avec une largeur augmentée de 50%
        self.tree.column("Numéro d'OF", width=int(150 * 1.5), anchor="center")
        self.tree.column("Date", width=int(150 * 1.5), anchor="center")
        self.tree.column("Quantité réalisé", width=int(150 * 1.5), anchor="center")
        self.tree.column("Quantité à produire", width=int(150 * 1.5), anchor="center")
 
        self.tree.place(relx=0.26, rely=0.15)
 
        # Appeler la méthode pour obtenir les informations des produits et afficher le tableau
        self.affichage_tableau_prod()

        # Ajout de la case d'entrée pour la quantité d'articles à retirer
        self.stock_entry_label_prod = Label(self.page_prod_frame, text="Quantité réalisé")
        self.stock_entry_label_prod.place(relx=0.5, rely=0.6, anchor='center')
 
        self.stock_entry_prod = Entry(self.page_prod_frame)
        self.stock_entry_prod.place(relx=0.455, rely=0.62)
 
        # Ajout du bouton Valider
        self.validate_stock_button = tk.Button(self.page_prod_frame, text="Valider", command=self.update_stock_prod)
        self.validate_stock_button.place(relx=0.50, rely=0.7, relwidth= 0.15, anchor='center')

 
    def affichage_tableau_prod(self):
        # Utiliser l'instance de la classe ERP
        self.erp.obtenir_informations_ordres_fabrication()
        
        # Afficher les valeurs récupérées pour le débogage
        print("OF:", self.erp.ordres_fabrication)
        print("Date ordre fabrication:", self.erp.dates_ordres_fabrication)
        print("Quantité réalisé", self.erp.quantite_a_produire)
        print("Quantité à produire:", self.erp.qty_producing)
 
        # Effacer les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
 
        # Ajouter les nouvelles données obtenues à la Treeview
        for i in range(len(self.erp.ordres_fabrication)):
            # Utiliser anchor pour centrer le texte
            self.tree.insert("", "end", values=(self.erp.ordres_fabrication[i], self.erp.dates_ordres_fabrication[i],
                                                self.erp.qty_producing[i], self.erp.quantite_a_produire[i]))

    def update_stock_prod(self):
        # Récupération de la quantité saisie dans la case d'entrée
        quantite = self.stock_entry_prod.get()

        # Assurez-vous que la quantité est un nombre entier
        try:
            quantite = int(quantite)
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir un nombre entier pour la quantité.")
            return

        # Obtenez la ligne sélectionnée
        item_selectionne = self.tree.selection()

        if not item_selectionne:
            messagebox.showerror("Erreur", "Aucune ligne sélectionnée.")
            return

        details_element = self.tree.item(item_selectionne)
        reference_interne = details_element['values'][0]  # Référence Interne
        qty_prod = float(details_element['values'][2])    # Quantité en production actuelle
        quantite_a_produire = float(details_element['values'][3])  # Quantité à produire

        nouvelle_quantite = quantite + qty_prod

        # Vérifiez si la quantité saisie est acceptable
        if nouvelle_quantite > quantite_a_produire:
            messagebox.showerror("Erreur", "La quantité saisie est supérieure à la quantité à produire.")
            return
        elif nouvelle_quantite < 0:
            messagebox.showerror("Erreur", "Impossible de créer une quantité produite négative.")
            return

        # Mise à jour du stock dans Odoo seulement si la quantité est correcte
        self.erp.modifier_quantite_produite(reference_interne, nouvelle_quantite)

        # Mise à jour de l'affichage
        self.affichage_tableau_prod()

        # Afficher un message de confirmation après la mise à jour réussie
        if nouvelle_quantite < quantite_a_produire:
            messagebox.showinfo("Mise à jour réussie", f"{quantite} stock affecté avec succès sur la référence '{reference_interne}'.")
        elif nouvelle_quantite == quantite_a_produire:
            messagebox.showinfo("Mise à jour réussie", f"{quantite} stock affecté avec succès sur la référence '{reference_interne}'. Fin de la production sur celle-ci.")

        # Effacement de la case d'entrée et du bouton Valider après la mise à jour
        self.stock_entry_prod.delete(0, 'end')
        self.stock_entry_prod.insert(0, "")

        # Mise à jour de la ligne sélectionnée dans le tableau
        self.tree.item(item_selectionne, values=(
            details_element['values'][0],  # Numéro d'OF reste inchangé
            details_element['values'][1],  # Date reste inchangée
            nouvelle_quantite,             # Quantité en production mise à jour
            details_element['values'][3])) # Quantité à produire reste inchangée

    def update_table_prod(self):
        # Effacer les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
 
        # Ajouter les nouvelles données obtenues à la Treeview après mise à jour
        for i in range(len(self.erp_instance.ordres_fabrication)):
            self.tree.insert("", "end", values=(self.erp.ordres_fabrication[i], self.erp.dates_ordres_fabrication[i],
                                                self.erp.quantite_a_produire[i], self.erp.qty_producing[i]))
    
#----------------------------------------------------------------------------------------------------
#     Méthodes page LOGISTIQUE
#----------------------------------------------------------------------------------------------------

    def pageLog(self):
        self.Number_page = 2
        
        self.page_log_frame = tk.Frame(self, bg="")
        self.page_log_frame.place(relx=0, rely=0, relwidth=1, relheight=0.8)
    
        #Création d'un bouton pour déconnexion l'application
        self.bouton_quit = tk.Button(self.page_log_frame, text="Déconnexion", bg="#DAD7D7", font=("Arial", 12), command= self.deconnexion)  
        self.bouton_quit.place(relx=1, rely=0.05, anchor='se')  # Positionne le bouton en haut à droite

        self.label = Label(self.page_log_frame, text="Logistique", font=('Helvetica', 24), bg="#EAF9FF")
        self.label.place(relx = 0.46, rely = 0.05)
        
        # Ajout de la case d'entrée pour la quantité d'articles à retirer
        self.stock_entry_label = Label(self.page_log_frame, text="Affectation stock:")
        self.stock_entry_label.place(relx=0.46, rely=0.6, anchor='center')
 
        self.stock_entry = Entry(self.page_log_frame)
        self.stock_entry.place(relx=0.535, rely=0.6,anchor='center')
 
        # Ajout du bouton Valider
        self.validate_stock_button = tk.Button(self.page_log_frame, text="Valider", command=self.update_stock_log)
        self.validate_stock_button.place(relx=0.503, rely=0.64, anchor='center', relwidth= 0.15)

        # Création de la grille pour afficher les articles
        self.tree = ttk.Treeview(self.page_log_frame, columns=("Nom", "Prix", "Référence Interne", "Stock Disponible"), show="headings")
 
        # Configuration des en-têtes de colonnes
        self.tree.heading("Nom", text="Nom", command=lambda: self.sort_column_log("Nom", False))
        self.tree.heading("Prix", text="Prix", command=lambda: self.sort_column_log("Prix", False))
        self.tree.heading("Référence Interne", text="Référence Interne", command=lambda: self.sort_column_log("Référence Interne", False))
        self.tree.heading("Stock Disponible", text="Stock Disponible", command=lambda: self.sort_column_log("Stock Disponible", False))
 
        # Ajout des colonnes avec une largeur augmentée de 50%
        self.tree.column("Nom", width=int(150 * 1.5), anchor="center")
        self.tree.column("Prix", width=int(150 * 1.5), anchor="center")
        self.tree.column("Référence Interne", width=int(150 * 1.5), anchor="center")
        self.tree.column("Stock Disponible", width=int(150 * 1.5), anchor="center")
 
        self.tree.place(relx=0.27, rely=0.15)
 
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
        quantite_str = self.stock_entry.get()

        # Assurez-vous que la quantité est un nombre entier
        try:
            quantite = int(quantite_str)
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez saisir un nombre entier pour la quantité.")
            return

        # Obtenez la ligne sélectionnée
        item_selectionne = self.tree.selection()

        # Vérifiez si un élément est sélectionné
        if not item_selectionne:
            messagebox.showerror("Erreur", "Aucune ligne sélectionnée.")
            return

        # Accéder aux détails de l'élément sélectionné dans le Treeview
        details_element = self.tree.item(item_selectionne, 'values')
        reference_interne = details_element[2]  # Référence Interne
        stock_disponible = float(details_element[3])  # Stock Disponible

        nouvelle_quantite = stock_disponible + quantite

        # Vérifier si la nouvelle quantité est valide (non négative)
        if nouvelle_quantite < 0:
            messagebox.showerror("Erreur", "La quantité résultante ne peut pas être négative.")
            return

        # Mise à jour du stock dans Odoo
        self.erp.modifier_stock_odoo(reference_interne, nouvelle_quantite)

        # Mettre à jour l'affichage sans ajouter une nouvelle ligne
        self.tree.item(item_selectionne, values=(details_element[0],
                                                details_element[1],
                                                reference_interne,
                                                nouvelle_quantite))

        # Afficher un message de confirmation après la mise à jour réussie
        messagebox.showinfo("Mise à jour réussie", f"Le stock de {quantite} unités a été ajouté avec succès pour l'article {reference_interne}.")

        # Effacement de la case d'entrée et du bouton Valider après la mise à jour
        self.stock_entry.delete(0, 'end')

    def update_table(self):
            # Effacer les éléments existants dans la Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)
    
            # Ajouter les nouvelles données obtenues à la Treeview après mise à jour
            for i in range(len(self.erp_instance.ordres_fabrication)):
                self.tree.insert("", "end", values=(self.erp.ordres_fabrication[i], self.erp.dates_ordres_fabrication[i],
                                                    self.erp.quantite_a_produire[i], self.erp.qty_producing[i]))
    
    def sort_column_log(self, col):
        # Obtenez l'état actuel du tri pour la colonne spécifiée
        reverse = self.sort_order[col]
 
        # Inversez l'état du tri pour la prochaine fois
        self.sort_order[col] = not reverse
 
        # Obtenez les données actuelles de la Treeview
        data = [(self.tree.set(child, "Nom"), self.tree.set(child, "Prix"), self.tree.set(child, "Référence Interne"), self.tree.set(child, "Stock Disponible"))
                for child in self.tree.get_children("")]
 
        # Triez les données en fonction de la colonne spécifiée et de l'état du tri
        col_index = ["Nom", "Prix", "Référence Interne", "Stock Disponible"].index(col)
        data.sort(key=lambda x: x[col_index], reverse=reverse)
 
        # Effacez les éléments existants dans la Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
 
        # Ajoutez les données triées à la Treeview
        for item in data:
            self.tree.insert("", "end", values=item)
   

#----------------------------------------------------------------------------------------------------
#     Méthodes page ADMIN
#----------------------------------------------------------------------------------------------------
        
#Création de la page Admin
    def pageAdmin(self):
        self.Number_page = 3

        self.page_admin_frame = tk.Frame(self, bg="")
        self.page_admin_frame.place(relx=0, rely=0, relwidth=1, relheight=0.8)
    
        #Création d'un bouton pour déconnexion l'application
        self.bouton_quit = tk.Button(self.page_admin_frame, text="Déconnexion", bg="#DAD7D7", font=("Arial", 12), command= self.deconnexion)  
        self.bouton_quit.place(relx=1, rely=0.05, anchor='se')  # Positionne le bouton en haut à droite

        self.label = Label(self.page_admin_frame, text="Menu Admin", font=('Helvetica', 24), bg="#EAF9FF")
        self.label.place(relx = 0.46, rely = 0.05)

        #Creation bouton pour aller page prod
        self.Button_prod = tk.Button(self.page_admin_frame, text="Production",fg="black", bg="#DAD7D7", font=("Arial", 20), command= self.shown_prod_page)
        self.Button_prod.place(relx=0.3, rely=0.5, anchor="center")
        #Creation bouton pour aller page logistique
        self.Button_logis = tk.Button(self.page_admin_frame, text="Logistique",fg="black", bg="#DAD7D7", font=("Arial", 20), command= self.shown_log_page)
        self.Button_logis.place(relx=0.7, rely=0.5, anchor="center")

    def affiche_admin(self):
        self.label_admin = Label(self, text="Menu Admin", font=('Helvetica', 14), bg="#EAF9FF")
        self.label_admin.place(relx = 0.475, rely = 0.9)

        self.button_return = tk.Button(self, text="Retour", font=('Helvetica', 14), bg="#EAF9FF", command= self.returned)
        self.button_return.place(relx=0.9, rely=0.90, anchor='se')

        self.activated_admin = 1

    def shown_prod_page(self):
        self.page_admin_frame.place_forget()
        self.update()
        self.affiche_admin()
        self.pageProd()
    
    def shown_log_page(self):
        self.page_admin_frame.place_forget()
        self.update()
        self.affiche_admin()
        self.pageLog()
    
    def returned(self):
        if self.Number_page == 1:
            self.page_prod_frame.place_forget()
            
        elif self.Number_page == 2:
            self.page_log_frame.place_forget()

        self.activated_admin = 0
        self.label_admin.place_forget()    
        self.button_return.place_forget()
        self.update()
        self.pageAdmin()

#----------------------------------------------------------------------------------------------------
#     Méthodes gestion des BOUTONS
#----------------------------------------------------------------------------------------------------

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
            image_label.place(relx=0.75, rely=0.1)
 
                
    def get_article_index_log(self, article_name):
        for i, article in enumerate(self.erp.articles_log):
            if article["name"] == article_name:
                return i
        return -1  # Retourne -1 si l'article n'est pas trouvé
    
    def user_current(self):
        # Création Label de l'utilisateur en cours
        self.label_user = tk.Label (self, text = "Utilisateur : " + self.user)
        self.label_user.place(relx=0, rely= 0.05)
          
