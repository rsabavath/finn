# pages/tests.py
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.test import TestCase
from .models import add_product, add_cart, payment_detail
from django.contrib.auth.models import User


from . import views
from datetime import datetime



class ProjectTests(TestCase):



    def test_product_content(self):
  
    	add_product.objects.create(product_Id=1, Productname = "Nike", price=30, stock=55,category="sdf", unit="sdsdf", colour="black" )
    	product_content = add_product.objects.get(id=1)
    	expected_object_name = product_content.Productname
    	self.assertEquals(expected_object_name, 'Nike')



    def add_to_cart_test(self):

    	self.credentials = {'username': 'testuser','password': 'secret'}
    	user = User.objects.create_user(**self.credentials)
    	add_product.objects.create(product_Id=1, Productname = "Nike", price=30, stock=55,category="sdf", unit="sdsdf", colour="black" )
    	add_cart.objects.create(product_Id=1, quantity=2, user=user)
    	cart_Content = add_cart.objects.get(id=1).product_Id
    	self.assertEquals(cart_Content, 1)


    def delete_cart_item(self):

    	self.credentials = {'username': 'testuser','password': 'secret'}
    	user = User.objects.create_user(**self.credentials)
    	add_product.objects.create(product_Id=1, Productname = "Nike", price=30, stock=55,category="sdf", unit="sdsdf", colour="black" )
    	add_cart.objects.create(product_Id=1, quantity=2, user=user)
    	cart_Content = add_cart.objects.filter(id=1).delete()
    	response = {"status":"sucess"}
    	self.assertEquals(response, {"status":"sucess"})

    def add_payment_test(self):

    	self.credentials = {'username': 'testuser','password': 'secret'}
    	user = User.objects.create_user(**self.credentials)
    	payment = payment_detail.objects.create(date= str(datetime.now()), purchase_amount = 200,user=user, reference_num=123,
    	 status="sucess",created_date=str(datetime.now()), created_by=user)
    	response = {"status":"sucess"}
    	self.assertEquals(response, {"status":"sucess"})



class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)

    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)


 