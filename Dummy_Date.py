from email.mime import image
from itertools import product
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
import django
django.setup()


from products.models import Products,Brand,Category
import random
from faker import Faker

def seed_Brand(n):
    fake=Faker()
    image=['1.png','2.png' ,'3.png' ,'4.png' ,'5.png']
    
    for _ in range(n):
        name=fake.name()
        imge=f"Brands/{image[random.randint(0,4)]}"

        Brand.objects.create(
            name=name,
            img=imge,
            category=Category.objects.get(id=random.randint(6,11))
        )
    print (f"scussuflly saeeded {n} Brand")



def seed_Category(n):
    fake=Faker()
    image=['1.png','2.png' ,'3.png' ,'4.png' ,'5.png']
    
    for _ in range(n):
        name=fake.name()
        imge=f"Category/{image[random.randint(0,5)]}"

        Category.objects.create(
            name=name,
            img=imge
        )

    print (f"scussuflly saeeded {n} Category")


def seed_Products(n):
    fake=Faker()
    image=['1.jpeg','2.jpg' ,'3.jpg' ,'4.jpg' ,'5.jpg','6.jpg','7.jpg']
    flag_type=["New","Sale","Feature"]
    
    for _ in range(n):
        name=fake.name()
        sub=fake.text(max_nb_chars=500)
        Sku=random.randint(1000,100000)
        imge=f"Products/{image[random.randint(0,6)]}"
        descretion=fake.text(max_nb_chars=5000)
        pricee=random.randint(100,3000)
        flag=flag_type[random.randint(0,2)]
        quantity=random.randint(1,200)

     

        Products.objects.create(
            name=name,
            sku=Sku, 
            img=imge,
            subtitle=sub,
            descriptin=descretion,
            flag=flag,
            price=pricee,
            brand=Brand.objects.get(id=random.randint(4,8)),
            category=Category.objects.get(id=random.randint(6,11)),
            quantity=quantity,
            
           
        )
    print (f"scussuflly saeeded {n} Brand")







# seed_Category(5)

# seed_Brand(5)

seed_Products(200)




