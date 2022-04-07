from faker import Faker

fake = Faker(locale='zh_CN')


with open(r'testdata','w',encoding='utf-8') as f:
    test_list = []
    test_list.append(fake.name())
    test_list.append(fake.address())
    # test_list.append(fake.date_time())
    test_list.append(fake.phone_number())
    test_list.append(fake.ssn())
    test_list.append(fake.password())
    # name = fake.name()
    # addres = fake.address()
    # time = fake.date_time()
    # ssn = fake.ssn()
    # phone = fake.phone_number()
    # password = fake.password()
    # bs = fake.job()   #职位
    # txt = print('',name,'\n',addres,'\n',time,'\n',ssn,'\n',phone,'\n',password,'\n',bs)
    print("-----------------------------------------------------------------------------")

for i in range(200):
    # print(fake.phone_number())
    print(fake.name(),'\t',fake.phone_number(),'\t',fake.pystr(),'\t',fake.numerify())


