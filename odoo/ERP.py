import xmlrpc.client
import base64
from datetime import datetime, timedelta
from io import BytesIO
from PIL import Image
 
class ERP:
    
#----------------------------------------------------------------------------------------------------
#     Constructeur
#----------------------------------------------------------------------------------------------------
    
    def __init__(self, db_name=None, ):
        self.odoo_ipaddr = "172.31.11.2"
        self.odoo_port = "8069"
        self.odoo_url = f'http://{self.odoo_ipaddr}:{self.odoo_port}'
        self.db_name = db_name
        self.password = ""
        self.common = xmlrpc.client.ServerProxy(f'{self.odoo_url}/xmlrpc/2/common', allow_none=True)
        self.models = xmlrpc.client.ServerProxy(f'{self.odoo_url}/xmlrpc/2/object', allow_none=True)
        self.uid = 0
 
        self.nom_article = []
        self.prix_article = []
        self.reference_interne = []
        self.stock_disponible = []
        self.images_stock = []
        self.ordres_fabrication = []
        self.dates_ordres_fabrication = []
        self.quantite_a_produire = []
        self.qty_producing = []

#----------------------------------------------------------------------------------------------------
#     Méthodes Gestion USER
#----------------------------------------------------------------------------------------------------

 
    def connexion(self, username=None , password=None):
        self.uid = self.common.authenticate(self.db_name, username, password, {})
        if self.uid:
            print('Connexion réussie. UID utilisateur:', self.uid)
            self.password = password
        else:
            print('Échec de la connexion.')
        return self.uid
 
    def deconnexion(self):
        if self.uid:
            #self.common.logout(self.db_name, self.uid, self.password)
            self.uid = 0
            print('Déconnexion réussie.')
        else:
            print('Aucun utilisateur connecté.')

#----------------------------------------------------------------------------------------------------
#     Méthodes READ
#----------------------------------------------------------------------------------------------------
            
    def obtenir_informations_produits(self):
        if self.uid:
            product_ids = self.models.execute_kw(
                self.db_name, self.uid, self.password,
                'product.product', 'search', [[]], {}
            )
            products = self.models.execute_kw(
                self.db_name, self.uid, self.password,
                'product.product', 'read', [product_ids],
                {'fields': ['name', 'list_price', 'default_code', 'qty_available', 'image_1920']}
            )

            for product in products:
                self.nom_article.append(product['name'])
                self.prix_article.append(product['list_price'])
                self.reference_interne.append(product['default_code'])
                self.stock_disponible.append(product['qty_available'])
        else:
            print('Échec de la connexion à Odoo.')

    def obtenir_informations_ordres_fabrication(self):
        if self.uid:
            orders_ids = self.models.execute_kw(
                self.db_name, self.uid, self.password,
                'mrp.production', 'search', [[]], {}
            )
            orders = self.models.execute_kw(
                self.db_name, self.uid, self.password,
                'mrp.production', 'read', [orders_ids],
                {'fields': ['name', 'date_planned_start', 'product_qty', 'qty_producing']}
            )
 
            for order in orders:
                self.ordres_fabrication.append(order['name'])
                self.dates_ordres_fabrication.append(order['date_planned_start'])
                self.quantite_a_produire.append(order['product_qty'])
                self.qty_producing.append(order['qty_producing'])
        else:
            print('Échec de la connexion à Odoo.')

    def obtenir_photos_produits(self):
        product_ids = self.models.execute_kw(
            self.db_name, self.uid, self.password,
            'product.product', 'search', [[]], {}
        )
        products = self.models.execute_kw(
            self.db_name, self.uid, self.password,
            'product.product', 'read', [product_ids],
            {'fields': ['name', 'image_1920']}
        )
 
        # Mettre à jour la liste des articles avec les noms des produits et les images
        self.articles_log = [{'name': product['name'], 'image': product['image_1920']} for product in products]
 
        # Mettre à jour la liste des images_stock avec les images des produits
        self.images_stock = [product['image_1920'] and base64.b64decode(product['image_1920']) for product in products]
#----------------------------------------------------------------------------------------------------
#     Méthodes WRITE
#----------------------------------------------------------------------------------------------------

    def modifier_stock_odoo(self, default_code, new_stock):
        if self.uid:
            product_id = self.models.execute_kw(
                self.db_name, self.uid, self.password,
                'product.product', 'search',
                [[['default_code', '=', default_code]]]
            )
            if product_id:
                quant_id = self.models.execute_kw(
                    self.db_name, self.uid, self.password,
                    'stock.quant', 'search',
                    [[['product_id', '=', product_id[0]]]]
                )
                if quant_id:
                    self.models.execute_kw(
                        self.db_name, self.uid, self.password,
                        'stock.quant', 'write',
                        [quant_id, {'quantity': new_stock}]
                    )
                    print(f"Stock mis à jour avec succès pour l'article avec le default_code '{default_code}'.")
                else:
                    print(f"Le produit avec le default_code '{default_code}' n'a pas de stock.")
            else:
                print(f"Le default_code '{default_code}' n'a pas été trouvé.")
        else:
            print('Échec de la connexion à Odoo.')
 
    def modifier_prod_quantite(self, ordre_fabrication, new_qty_producing):
        if self.uid:
            mo_id = self.models.execute_kw(
                self.db_name, self.uid, self.password,
                'mrp.production', 'search',
                [[['name', '=', ordre_fabrication]]]
            )
            if mo_id:
                self.models.execute_kw(
                    self.db_name, self.uid, self.password,
                    'mrp.production', 'write',
                    [mo_id, {'qty_producing': new_qty_producing}]
                )
                print(f"Quantité en cours de production mise à jour avec succès pour l'ordre de fabrication '{ordre_fabrication}'.")
            else:
                print(f"L'ordre de fabrication '{ordre_fabrication}' n'a pas été trouvé.")
        else:
            print('Échec de la connexion à Odoo.')

#----------------------------------------------------------------------------------------------------
#     Méthodes TEST
#----------------------------------------------------------------------------------------------------
 
    def afficher_variables(self):
        if self.nom_article:
            print("Nom des articles :", self.nom_article[0])
        if self.prix_article:
            print("Prix des articles :", self.prix_article[0])
        if self.reference_interne:
            print("Référence interne :", self.reference_interne[0])
        if self.stock_disponible:
            print("Stock disponible :", self.stock_disponible[0])
        if self.ordres_fabrication:
            print("Nom des articles :", self.ordres_fabrication[0])
        if self.dates_ordres_fabrication:
            print("Prix des articles :", self.dates_ordres_fabrication[0])
        if self.quantite_a_produire:
            print("Référence interne :", self.quantite_a_produire[0])
        if self.qty_producing:
            print("Stock disponible :", self.qty_producing[0])
 
#----------------------------------------------------------------------------------------------------
#     Application 
#----------------------------------------------------------------------------------------------------
 
if __name__ == "__main__":
    erp_instance = ERP(db_name='db_cybervest')
 
    # tentative requete avant connexion     
    erp_instance.obtenir_informations_produits()
    
    erp_instance.connexion(username='alexandre', password='jslpdl')

    print("--------------------------")
    
    erp_instance.obtenir_informations_ordres_fabrication()

    erp_instance.obtenir_informations_produits()
 
    erp_instance.afficher_variables()
 
    erp_instance.modifier_stock_odoo()


