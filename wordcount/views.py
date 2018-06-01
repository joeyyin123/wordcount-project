from django.http import HttpResponse
from django.shortcuts import render
import operator
def homepage(request):
    #return HttpResponse('hello')
    return render(request, 'home.html',{'Hithere': 'this is me'})

def eggs(request):
    #return HttpResponse('Eggs are great!')
    return HttpResponse('<h1>eggs are great</h1>')
def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    #print(fulltext)
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1
        else:
            #add to the worddictionary
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

            #return render(request, 'count.html',{'fulltext': fulltext,'count': len(wordlist),'worddictionary': worddictionary.items()})
    return render(request, 'count.html',{'fulltext': fulltext,'count': len(wordlist),'sortedwords': sortedwords})
def about(request):
    return render(request, 'about.html')
