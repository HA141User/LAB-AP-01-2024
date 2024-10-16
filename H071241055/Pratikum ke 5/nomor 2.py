def acronym(string):
    try:
        data_list = string.split()
        # print(data_list)
        for i in data_list:
            akronim = i[0].upper()
            print(akronim,end="")
    except:
        print("Peringatan Kesalahan")

nkri = "Negara Kesatuan Republik esia"
acronym(nkri)


