# I have created this file - Dip
from django.http import HttpResponse
from django.shortcuts import render


def ex1(request):
    s = '''Navigation Bar <br>
    <a href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9">Django Code With Harry Bhai</a><br>
    <a href="https://www.google.com/">Google</a><br>
    '''
    return HttpResponse(s)


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def analyze(request):
    djangotext = request.POST.get('text', 'default')

    removepunctuation = request.POST.get('removepunctuation', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    analyzed = djangotext
    purposes = []

    if removepunctuation == "on":
        punctuations = r"""!()-[]{};:'"\,<>./?@#$%^&*_~"""
        result = ""
        for char in analyzed:
            if char not in punctuations:
                result = result + char
        analyzed = result
        purposes.append('Removed Punctuations')

    if fullcaps == "on":
        result = ""
        for char in analyzed:
            result = result + char.upper()
        analyzed = result
        purposes.append('Uppercase')

    if newlineremover == "on":
        result = ""
        for char in analyzed:
            if char != "\n" and char != "\r":
                result = result + char
        analyzed = result
        purposes.append('Removed New Lines')

    if extraspaceremover == "on":
        result = ""
        for index, char in enumerate(analyzed):
            if index + 1 < len(analyzed):
                if not (analyzed[index] == " " and analyzed[index + 1] == " "):
                    result = result + char
            else:
                result = result + char
        analyzed = result
        purposes.append('Removed Extra Spaces')

    if charcount == "on":
        purposes.append(f'Character Count: {len(analyzed)}')

    purpose = ' | '.join(purposes) if purposes else 'No Operation Selected'

    params = {'purpose': purpose, 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
