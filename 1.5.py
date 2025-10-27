total_systems=int(input("enter the total number of systems in the lab:"))
#percent distribution
dell_percent=36
lenovo_percent=34
acer_percent=28
samsung_percent=2
#count per brand using integer rounding
dell_count=total_systems*dell_percent//100
lenovo_count=total_systems*lenovo_percent//100
acer_count=total_systems*acer_percent//100
samsung_count=total_systems*samsung_percent//100
#print results using sep
print("total systems:",total_systems)
print("Dell:",dell_count,sep="\t")
print("Lenovo:",lenovo_count,sep="\t")
print("Acer:",acer_count,sep="\t")
print("Samsung:",samsung_count,sep="\t")
