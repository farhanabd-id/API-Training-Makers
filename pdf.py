from flask import Flask, request

app=Flask(__name__)
@app.route('/pdf-viewer', methods=['GET'])
def designerPdfViewer():

    p =request.json['height']
    x =request.args.get("word")

    words = ["a","b","c","d","e",'f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    elemen = []
    kamus = {}
    for i in range(len(words)):
        for j in range(len(p)):
            if i == j:
                kamus[words[i]] = p[j]
    for item in x:
        elemen.append(kamus.get(item))
    hasil = max(elemen)*len(elemen)
    # return max(elemen)*len(elemen)
    return {"height" : hasil }

# print(designerPdfViewer([1,3,1,3,1,4,1,3,2,5,5,5,5,1,1,5,5,1,5,2,5,5,5,5,5,5],"torn"))
