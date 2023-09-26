from openpyxl import Workbook
import openpyxl

file_path = "MondayBot\PostDB.xlsx"
wb = openpyxl.load_workbook(file_path)

# Open the Excel file


# Access the first sheet
sheet = wb.active

for row in sheet.iter_rows(min_row=1, max_row=sheet.max_row, min_col=1, max_col=3):
    cell_a = row[0].value  # Column A
    cell_b = row[1].value  # Column B
    cell_c = row[2].value  # Column C
    pos_a = row[0].coordinate
    pos_b = row[1].coordinate
    pos_c = row[2].coordinate
    
    # Do something with the values from each column
    #print(f"{cell_a}, {cell_b}, {cell_c}, \n")
    if cell_b == "Ready" and cell_c != None:
        print(pos_b, pos_b,pos_b)
        print(type(pos_b) , type(cell_b))

        sheet[str(pos_b)] = "Posted"
        print("------------------ ",sheet[pos_b])
        print(row)
        
        
        
        
    
    
wb.save("data.xlsx") 
wb.close()