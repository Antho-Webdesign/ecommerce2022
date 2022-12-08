import datetime
from django.test import TestCase

from shop.models import Product

# Create your tests here.
class ShopTestCase(TestCase):

    def test_create_product(self):
        # Voir combien de produits il y a dans la base de données
        # Ajouter un produit
        # Valider la bonne incrementation du nombre de produits dans la base de données
        nb_products = Product()
        new_product_title = 'test'
        new_product_price = 100
        new_product_data_add = datetime.today()

        new_product = Product.objects.create(title=new_product_title, price=new_product_price, data_add=new_product_data_add)
        self.assertEqual(new_product.title, new_product_title)
        self.assertEqual(new_product.price, new_product_price)
        self.assertEqual(new_product.data_add, new_product_data_add)

        self.assertEqual(nb_products + 1, Product.objects.count())

    def test_update_product(self):
        # Voir combien de produits il y a dans la base de données
        # Ajouter un produit
        # Valider la bonne incrementation du nombre de produits dans la base de données
        nb_products = Product()
        new_product_title = 'test'
        new_product_price = 100
        new_product_data_add = datetime.today()

        new_product = Product.objects.create(title=new_product_title, price=new_product_price, data_add=new_product_data_add)
        self._extracted_from_test_update_product_11(new_product, new_product_title, new_product_price, new_product_data_add)

        self.assertEqual(nb_products + 1, Product.objects.count())

        # Modifier le produit
        # Valider la modification du produit
        new_product_title = 'test2'
        new_product_price = 200
        new_product_data_add = datetime.today()

        new_product.title = new_product_title
        new_product.price = new_product_price
        new_product.data_add = new_product_data_add

        self._extracted_from_test_update_product_11(new_product, new_product_title, new_product_price, new_product_data_add)

    # TODO Rename this here and in `test_update_product`
    def test_update_product(self, new_product, new_product_title, new_product_price, new_product_data_add):
        self.assertEqual(new_product.title, new_product_title)
        self.assertEqual(new_product.price, new_product_price)
        self.assertEqual(new_product.data_add, new_product_data_add)

    def test_delete_product(self):  
        # Voir combien de produits il y a dans la base de données
        # Ajouter un produit
        # Valider la bonne incrementation du nombre de produits dans la base de données
        nb_products = Product()
        new_product_title = 'test'
        new_product_price = 100
        new_product_data_add = datetime.today()

        new_product = Product.objects.create(title=new_product_title, price=new_product_price, data_add=new_product_data_add)
        self._extracted_from_test_update_product_11(new_product, new_product_title, new_product_price, new_product_data_add)

        self.assertEqual(nb_products + 1, Product.objects.count())

        # Supprimer le produit
        # Valider la suppression du produit
        new_product.delete()
        self.assertEqual(nb_products, Product.objects.count())

    def test_list_product(self):
        # Voir combien de produits il y a dans la base de données
        # Ajouter un produit
        # Valider la bonne incrementation du nombre de produits dans la base de données
        nb_products = Product()
        new_product_title = 'test'
        new_product_price = 100
        new_product_data_add = datetime.today()

        new_product = Product.objects.create(title=new_product_title, price=new_product_price, data_add=new_product_data_add)
        self._extracted_from_test_update_product_11(new_product, new_product_title, new_product_price, new_product_data_add)

        self.assertEqual(nb_products + 1, Product.objects.count())

        # Voir combien de produits il y a dans la base de données
        # Valider que le nombre de produits est le même
        self.assertEqual(nb_products + 1, Product.objects.count())

    def test_detail_product(self):
        # Voir combien de produits il y a dans la base de données
        # Ajouter un produit
        # Valider la bonne incrementation du nombre de produits dans la base de données
        nb_products = Product()
        new_product_title = 'test'
        new_product_price = 100
        new_product_data_add = datetime.today()

        new_product = Product.objects.create(title=new_product_title, price=new_product_price, data_add=new_product_data_add)
        self._extracted_from_test_update_product_11(new_product, new_product_title, new_product_price, new_product_data_add)

        self.assertEqual(nb_products + 1, Product.objects.count())

        # Voir combien de produits il y a dans la base de données
        # Valider que le nombre de produits est le même
        self.assertEqual(nb_products + 1, Product.objects.count())

        # Voir le détail d'un produit
        # Valider que le produit est le bon
        self.assertEqual(new_product, Product.objects.get(id=new_product.id))

    def test_search_product(self):
        # Voir combien de produits il y a dans la base de données
        # Ajouter un produit
        # Valider la bonne incrementation du nombre de produits dans la base de données
        nb_products = Product()
        new_product_title = 'test'
        new_product_price = 100
        new_product_data_add = datetime.today()

        new_product = Product.objects.create(title=new_product_title, price=new_product_price, data_add=new_product_data_add)
        self._extracted_from_test_update_product_11(new_product, new_product_title, new_product_price, new_product_data_add)

        self.assertEqual(nb_products + 1, Product.objects.count())

        # Voir combien de produits il y a dans la base de données
        # Valider que le nombre de produits est le même
        self.assertEqual(nb_products + 1, Product.objects.count())

        # Voir le détail d'un produit
        # Valider que le produit est le bon
        self.assertEqual(new_product, Product.objects.get(id=new_product.id))

        # Rechercher un produit
        # Valider que le produit est le bon
        self.assertEqual(new_product, Product.objects.get(title=new_product_title))

    def test_list_product_by_category(self):
        # Voir combien de produits il y a dans la base de données
        # Ajouter un produit
        # Valider la bonne incrementation du nombre de produits dans la base de données
        nb_products = Product()
        new_product_title = 'test'
        new_product_price = 100
        new_product_data_add = datetime.today()

        new_product = Product.objects.create(title=new_product_title, price=new_product_price, data_add=new_product_data_add)
        self._extracted_from_test_update_product_11(new_product, new_product_title, new_product_price, new_product_data_add)

        self.assertEqual(nb_products + 1, Product.objects.count())

        # Voir combien de produits il y a dans la base de données
        # Valider que le nombre de produits est le même
        self.assertEqual(nb_products + 1, Product.objects.count())

        # Voir le détail d'un produit
        # Valider que le produit est le bon
        self.assertEqual(new_product, Product.objects.get(id=new_product.id))

        # Rechercher un produit
        # Valider que le produit est le bon
        self.assertEqual(new_product, Product.objects.get(title=new_product_title))

        # Voir la liste des produits par catégorie
        # Valider que le produit est le bon
        self.assertEqual(new_product, Product.objects.get(category=new_product.category))

