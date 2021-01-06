import ezsheets
ss=ezsheets.Spreadsheet('1k1qs4SSw6dQLMJC1QvA_UU_-vfgUHikkGvVuuAvlDRY')
sheet=ss[0]
columnemail=sheet.getColumn(3)
for i, value in enumerate(columnemail):
    print(columnemail[i])
    if columnemail[i]=='':
        break
