from django.shortcuts import render

def homePage(request):
    c = {}
    try:
        if request.POST.get("num1") == "":
            return render(request, "index.html", {"error":True})


        if request.method=="POST":
            n1 = int(request.POST.get("num1"))
            if n1%2==0:
                print(f"{n1} is Even Number")
                c = "is Even Number"
            else:
                print(f"{n1} is Odd Number")
                c = "is Odd Number"
        c = {
             "c":c,
             "n1":n1,
            }
            
    except:
        print("You Made Invalid Operation......")
    return render(request, "index.html", c)