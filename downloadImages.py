from simple_image_download import simple_image_download as simpImg

respImgs = simpImg.simple_image_download

keywords = ["building workers"]

for kword in keywords:
    respImgs().download(keywords=kword, limit=100)

