n=input("saisire votre mots de pass:")
na="Dev@2023"
tries=2
q="Hitman"
while n!=na:
    tries-=1
    print("Mot de pass incorrect")
    n=input("saisire votre mots de pass:")
    if tries==0 and n!=na:
        print("donner moi le nom d un film ")
        o=input("Le nom du film est:")
        if o==q:
            tries=3
            n=input("saisire votre mots de pass:")
        else :
            print("by")
            break 
if n==na:
    print("Bonjour!")    




