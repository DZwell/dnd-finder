import openpyxl

wb = openpyxl.load_workbook('test.xlsx')
sheet = wb.get_sheet_by_name('Sheet1')

def get_item_codes():
  item_codes = []
  row = 1
  cell_has_item_code = True

  while cell_has_item_code:
    cell = sheet['A' + str(row)]

    if cell.value:
      item_codes.append(cell.value)
      row += 1
    else:
      cell_has_item_code = False
    
  return item_codes

