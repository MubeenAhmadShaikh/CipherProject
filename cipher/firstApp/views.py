from django.shortcuts import render
from django.http import HttpResponse
from firstApp.ciphers.hillCipher import encode, decode
from firstApp.ciphers.affineCipher import affineEnc, affineDec
import numpy as np
# Create your views here.
def hillEncrypt(request):
    context={}
    if request.method == 'POST':
        message = request.POST['message'] 
        key = request.POST['key'] 
        nn_matrix = list(map(int,key.split()))
        total_cells =  len(nn_matrix)
        row_cells = int(total_cells**0.5)
        keymatrix = [nn_matrix[i:i+row_cells] for i in range(0, total_cells, row_cells)]

        # TEFBQNJUHIDDULEZROCBLJKGUAONPXIFXUUB
        print(message, keymatrix)
        encoded = encode(message, keymatrix)
        print(encoded)
        context.update({'encoded':encoded})
    return render(request,'firstApp/hill-encrypt.html',context)

def hillDecrypt(request):
    context={}
    if request.method == 'POST':
        message = request.POST['message'] 
        key = request.POST['key'] 
        nn_matrix = list(map(int,key.split()))
        total_cells =  len(nn_matrix)
        row_cells = int(total_cells**0.5)
        keymatrix = [nn_matrix[i:i+row_cells] for i in range(0, total_cells, row_cells)]

        # TEFBQNJUHIDDULEZROCBLJKGUAONPXIFXUUB
        decoded = decode(message, keymatrix)
        final = list(decoded)
        if final[-1] == 'X':
            final.pop()
            decoded = str("".join(final))
        context.update({'decoded':decoded})
    return render(request,'firstApp/hill-decrypt.html',context)

def affineEncrypt(request):
    context={}
    if request.method == 'POST':
        plaintext = request.POST['message'].lower()
        plaintext = "".join(plaintext.split(" "))
        a = int(request.POST['a']) 
        b = int(request.POST['b'])  
        key = (a,b)
        encoded = affineEnc(str(plaintext),key)
        context.update({'encoded':encoded})
    return render(request,'firstApp/affine-encrypt.html',context)

def affineDecrypt(request):
    context={}
    if request.method == 'POST':
        cyphertext = request.POST['message']
        a = int(request.POST['a']) 
        b = int(request.POST['b'])  
        key = (a,b)
        decoded = affineDec(cyphertext,key)
        context.update({'decoded':decoded})
    return render(request,'firstApp/affine-decrypt.html',context)