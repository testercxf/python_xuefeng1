import hashlib
import xlrd
from xlutils.copy import copy



# world = 'CF60745DEB38563041A383F1BA63AAA6'
magic = "@godLoveU$"
# user_uuid = "usr_pajtqwgozpmb"
password = "123456"
time = "2021-10-13 10:07:36"
def md5_password(user_uuid):
    passq = magic + user_uuid + password+time
    d = passq+str(len(passq)*23)
    md5 = hashlib.md5()
    md5.update(d.encode("utf-8"))
    md5_p = md5.hexdigest().upper()
    return md5_p


class OperationExcel():
    file = "C:/Users/28918/Desktop/userinfo.xlsx"

    def read_excel(self,row):
        wb = xlrd.open_workbook(self.file, "rb")
        sheet1 = wb.sheet_by_index(0)
        return sheet1.cell_value(row, 0)

    def write_value(self, row, value):
            '''写入excel数据'''
            read_data = xlrd.open_workbook(self.file)
            write_data = copy(read_data)
            sheet_data = write_data.get_sheet(0)
            sheet_data.write(row, 2, value)
            write_data.save(self.file)

    def mian(self):
        wb = xlrd.open_workbook(self.file, "rb")
        sheet1 = wb.sheet_by_index(0)
        rowNum = sheet1.nrows
        for i in range(rowNum):
            uuid = str(self.read_excel(i))
            uuid = uuid.replace("text:'", "")
            uuid = uuid.replace("'", "")
            password = md5_password(uuid)
            self.write_value(i, password)
            i = i+1


if __name__ == '__main__':
    oe = OperationExcel()
    print(oe.read_excel(0))
    print(oe.mian())