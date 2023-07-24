from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
#    return HttpResponse('Hello')
#    return render(request, 'home.html', {'hithere': 'This is me'})
    return render(request, 'home.html')

def eggs(request):
    return HttpResponse('<h1>Eggs are great!!!<h1>')

# def count(request):
#    return render(request, 'count.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    return render(request, 'count.html', {'fulltext':fulltext, 'count': len(wordlist), 'worddictionary' : worddictionary.items() })

def about(request):
    return render(request, 'about.html')
