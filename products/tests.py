# products/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product
from django.core.files.uploadedfile import SimpleUploadedFile

class PixelAndPaperTests(TestCase):
    def setUp(self):
        """Set up test data for all test methods"""
        self.client = Client()
        
        # Create test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com'
        )
        
        # Create a test file
        self.test_file = SimpleUploadedFile(
            name='test_file.pdf',
            content=b'file_content',
            content_type='application/pdf'
        )
        
        # Create test product with correct fields
        self.product = Product.objects.create(
            title='Test Product',
            description='Test Description',
            price=99.99,
            file=self.test_file,
            slug='test-product',
            category='test-category',
            image='product_images/test-image.jpg'
        )

    def test_home_page(self):
        """Test home page loads correctly"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/home.html')

    def test_product_list(self):
        """Test product list page loads correctly"""
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_list.html')

    def test_product_detail(self):
        """Test product detail page loads correctly"""
        response = self.client.get(f'/products/{self.product.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_product_list_contains_product(self):
        """Test that the product list contains our test product"""
        response = self.client.get('/products/')
        self.assertContains(response, self.product.title)

class ProductModelTests(TestCase):
    def setUp(self):
        """Set up test data"""
        self.test_file = SimpleUploadedFile(
            name='test_file.pdf',
            content=b'file_content',
            content_type='application/pdf'
        )

    def test_product_creation(self):
        """Test creating a new product"""
        product = Product.objects.create(
            title='Test Product',
            description='Test Description',
            price=99.99,
            file=self.test_file,
            slug='test-product',
            category='test-category',
            image='product_images/test-image.jpg'
        )
        self.assertTrue(isinstance(product, Product))
        self.assertEqual(str(product), product.title)

    def test_product_str_method(self):
        """Test the string representation of the Product model"""
        product = Product.objects.create(
            title='Test Product',
            description='Test Description',
            price=99.99,
            file=self.test_file,
            slug='test-product',
            category='test-category',
            image='product_images/test-image.jpg'
        )
        self.assertEqual(str(product), 'Test Product')

    def test_product_fields(self):
        """Test product field values"""
        product = Product.objects.create(
            title='Test Product',
            description='Test Description',
            price=99.99,
            file=self.test_file,
            slug='test-product',
            category='test-category',
            image='product_images/test-image.jpg'
        )
        self.assertEqual(product.title, 'Test Product')
        self.assertEqual(product.description, 'Test Description')
        self.assertEqual(float(product.price), 99.99)
        self.assertEqual(product.slug, 'test-product')
        self.assertEqual(product.category, 'test-category')
        self.assertTrue(product.file)

    def tearDown(self):
        """Clean up test files"""
        for product in Product.objects.all():
            if product.file:
                product.file.delete()
            if product.image:
                product.image.delete()