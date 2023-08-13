from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post
from accounts.models import User

class Test(TestCase):
    def setUp(self):
        # 가상의 client를 만들어서 사용합니다. 이때 DB는 비어있는 채로 시작합니다.
        self.client = Client()
        self.user_hojun = User.objects.create_user(
            username='leehojun', password='ilovedjango99))'
        )

    def test_create_test(self):
        '''
            title = models.CharField(max_length=100)
            content = models.TextField()
            head_image = models.ImageField(
                upload_to='blog/images/%Y/%m/%d/', blank=True)
            file_upload = models.FileField(
                upload_to='blog/files/%Y/%m/%d/', blank=True)
            created_at = models.DateTimeField(auto_now_add=True)
            updated_at = models.DateField(auto_now=True)

            # author = models.ForeignKey(User, on_delete=models.CASCADE)
            author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

            category = models.ForeignKey(
                'Category', null=True, blank=True, on_delete=models.SET_NULL)

            tags = models.ManyToManyField('Tag', blank=True)
        '''
        post_001 = Post.objects.create(
            title = '첫 번째 포스트입니다.',
            content = 'Hello World.',
            author = self.user_hojun
        )
        self.assertEqual(Post.objects.count(), 1)
        response = self.client.get('/blog/')
        soup = BeautifulSoup(response.content, 'html.parser')
        body = soup.body
        self.assertIn('첫 번째 포스트입니다.', body.text)
        self.assertIn('Hello World.', body.text)
