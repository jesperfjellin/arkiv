with open('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/test/data_cleaned.csv', 'w', encoding='utf-8') as out_file:
    with open('C:/Kartografi_Jesper/Python/veger_under_konstruksjon/test/data_test.csv', 'r', encoding='utf-8') as in_file:
        # Skip the first line in the input file
        next(in_file)
        for line in in_file:
            new_line = ""
            while "LINESTRING Z" in line:
                start_index = line.index("LINESTRING Z")
                end_index = line.index(")", start_index)
                linestring = line[start_index:end_index+1]
                new_line += linestring
                line = line[end_index+1:]
            while "typeVeg_sosi:" in line:
                start_index = line.index("typeVeg_sosi:")
                end_index = line.index(",", start_index)
                vegtype = line[start_index:end_index]
                new_line += vegtype
                line = line[end_index+1:]
            if new_line:
                out_file.write(new_line + '\n')
            else:
                print("No LINESTRING Z or typeVeg_sosi found in the line.")
